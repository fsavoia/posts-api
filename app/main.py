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

include_router = [posts.router, auth.router, users.router]

for include in include_router:
    app.include_router(include)


@app.get("/")
def root():
    return {"message": "Hello World"}
