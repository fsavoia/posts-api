import models
from config import AppConfig
from database import engine
from fastapi import FastAPI
from routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=AppConfig.APP_TITLE.value,
    description=AppConfig.APP_DESCRIPTION.value,
    version=AppConfig.APP_VERSION.value,
    contact={
        "name": AppConfig.CONTACT_NAME.value,
        "email": AppConfig.CONTACT_EMAIL.value,
    },
    license_info={
        "name": AppConfig.LICENSE_NAME.value,
        "url": AppConfig.LICENSE_URL.value,
    },
)

# Include routers
include_router = [posts.router, auth.router, users.router]

for include in include_router:
    app.include_router(include)


@app.get("/")
def root():
    """
    Root endpoint to check if the API is running.
    """
    return {"message": "Welcome to Blog API"}
