import models
from database import engine
from fastapi import FastAPI
from routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Blog API",
    description="API used to control posts in a blog",
    version="0.0.2",
    contact={
        "name": "Felipe Savoia",
        "email": "savoia@fsavoia.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
