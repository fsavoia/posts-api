from typing import List

import models
import schemas
from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/posts", tags=["Users"])


@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db)):
    data = db.query(models.Post).all()
    return data


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse
)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    data = models.Post(**post.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


@router.get("/{id}", response_model=schemas.PostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    data = db.query(models.Post).filter(models.Post.id == id).first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    return data


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    data = db.query(models.Post).filter(models.Post.id == id)

    if data.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    data.delete(synchronize_session=False)
    db.commit()
    return data


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    data = db.query(models.Post).filter(models.Post.id == id)

    if data.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )

    data.update(post.dict(), synchronize_session=False)
    db.commit()
    return data.first()
