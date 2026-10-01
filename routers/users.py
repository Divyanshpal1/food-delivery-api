from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import UserRegister, UserLogin, UserUpdate
from crud import (
    create_user,
    get_user_by_email,
    get_user_by_id,
    update_user,
    delete_user
)
from utils import verify_password
from oauth2 import create_access_token
from dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = create_user(db, user)

    return {
        "message": "User Registered Successfully",
        "data": new_user
    }


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = get_user_by_email(db, user.email)

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    access_token = create_access_token(
        {
            "user_id": db_user.id,
            "email": db_user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/{user_id}")
def get_profile(
    user_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}")
def update_profile(
    user_id: int,
    user: UserUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated_user = update_user(
        db,
        user_id,
        user
    )

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Profile Updated Successfully",
        "data": updated_user
    }



@router.delete("/{user_id}")
def remove_user(
    user_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = delete_user(
        db,
        user_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return deleted