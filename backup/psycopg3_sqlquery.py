import psycopg
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from psycopg.rows import dict_row


app = FastAPI(
    title="Blog API",
    description="API used to control posts in a blog",
    version="0.0.1",
    contact={
        "name": "Felipe Savoia",
        "email": "savoia@fsavoia.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    response = exec_db_cmd("SELECT * FROM posts")
    return {"data": response}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    sql = "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *"
    params = (post.title, post.content, post.published)
    response = exec_db_cmd(sql, params)
    return {"data": response}


@app.get("/posts/{id}")
def get_post(id: int):
    sql = "SELECT * FROM posts WHERE id = %s"
    params = (str(id),)
    response = exec_db_cmd(sql, params)
    if len(response) < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"data": response}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    sql = "DELETE FROM posts WHERE ID = %s RETURNING *"
    params = (str(id),)
    response = exec_db_cmd(sql, params)
    if len(response) < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"data": response}


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    sql = "UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *"
    params = (
        post.title,
        post.content,
        post.published,
        str(id),
    )
    response = exec_db_cmd(sql, params)
    if len(response) < 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"data": response}


def exec_db_cmd(command, params=None):
    try:
        with psycopg.connect("host=db dbname=fastapi user=admin password=123qwe", row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                if params:
                    cur.execute(command, params)
                else:
                    cur.execute(command)
                records = cur.fetchall()
                conn.commit()
        return records
    except psycopg.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
