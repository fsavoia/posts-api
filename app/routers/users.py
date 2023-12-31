from typing import List

import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)) -> list:
    """Get the list of all active users

    Returns:
    list: Returns a list converted to Json by FastAPI
    """
    data = db.query(models.User).all()
    print(f"type: {type(data)}")

    return data


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    data = db.query(models.User).filter(models.User.id == id).first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {id} does not exist",
        )

    return data


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse,
)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    data = models.User(**user.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
