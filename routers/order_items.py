from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user

from schemas import (
    OrderItemCreate,
    OrderItemUpdate
)

from crud import (
    create_order_item,
    get_all_order_items,
    get_order_item_by_id,
    get_order_items_by_order,
    update_order_item,
    delete_order_item,
    search_order_item,
    get_order_items_pagination
)

router = APIRouter(
    prefix="/order-items",
    tags=["Order Items"]
)


@router.post("/")
def add_order_item(
    order_item: OrderItemCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_order_item(
        db,
        order_item
    )



@router.get("/")
def all_order_items(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_all_order_items(db)



@router.get("/{order_item_id}")
def order_item_by_id(
    order_item_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    order_item = get_order_item_by_id(
        db,
        order_item_id
    )

    if order_item is None:
        raise HTTPException(
            status_code=404,
            detail="Order Item Not Found"
        )

    return order_item


@router.get("/order/{order_id}")
def items_by_order(
    order_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_order_items_by_order(
        db,
        order_id
    )


@router.put("/{order_item_id}")
def edit_order_item(
    order_item_id: int,
    order_item: OrderItemUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated = update_order_item(
        db,
        order_item_id,
        order_item
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Order Item Not Found"
        )

    return {
        "message": "Order Item Updated Successfully",
        "data": updated
    }
    

@router.delete("/{order_item_id}")
def remove_order_item(
    order_item_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = delete_order_item(
        db,
        order_item_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Order Item Not Found"
        )

    return deleted


@router.get("/search/")
def search_items(
    order_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return search_order_item(
        db,
        order_id
    )


@router.get("/pagination/")
def order_items_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_order_items_pagination(
        db,
        skip,
        limit
    )
    