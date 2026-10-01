from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user

from schemas import (
    OrderCreate,
    OrderUpdate
)

from crud import (
    create_order,
    get_all_orders,
    get_order_by_id,
    get_orders_by_user,
    update_order,
    cancel_order,
    search_order,
    get_orders_pagination
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def add_order(
    order: OrderCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_order(db, order)


@router.get("/")
def all_orders(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_all_orders(db)


@router.get("/{order_id}")
def order_by_id(
    order_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    order = get_order_by_id(
        db,
        order_id
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order Not Found"
        )

    return order



@router.get("/user/{user_id}")
def user_orders(
    user_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_orders_by_user(
        db,
        user_id
    )


@router.put("/{order_id}")
def edit_order(
    order_id: int,
    order: OrderUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated = update_order(
        db,
        order_id,
        order
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Order Not Found"
        )

    return {
        "message": "Order Updated Successfully",
        "data": updated
    }
    

@router.delete("/{order_id}")
def remove_order(
    order_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = cancel_order(
        db,
        order_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Order Not Found"
        )

    return deleted



@router.get("/search/")
def search_orders(
    status: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return search_order(
        db,
        status
    )


@router.get("/pagination/")
def orders_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_orders_pagination(
        db,
        skip,
        limit
    )
    