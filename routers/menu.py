from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user

from schemas import (
    MenuItemCreate,
    MenuItemUpdate
)

from crud import (
    create_menu_item,
    get_menu_item_by_id,
    get_all_menu_items,
    get_menu_by_restaurant,
    update_menu_item,
    delete_menu_item,
    search_menu_item,
    get_menu_pagination
)

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


@router.post("/")
def add_menu_item(
    menu: MenuItemCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_menu_item(db, menu)


@router.get("/")
def all_menu_items(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_all_menu_items(db)


@router.get("/{menu_id}")
def menu_item_by_id(
    menu_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    menu = get_menu_item_by_id(
        db,
        menu_id
    )

    if menu is None:
        raise HTTPException(
            status_code=404,
            detail="Menu Item Not Found"
        )

    return menu


@router.get("/restaurant/{restaurant_id}")
def menu_by_restaurant(
    restaurant_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_menu_by_restaurant(
        db,
        restaurant_id
    )


@router.put("/{menu_id}")
def edit_menu_item(
    menu_id: int,
    menu: MenuItemUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated = update_menu_item(
        db,
        menu_id,
        menu
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Menu Item Not Found"
        )

    return {
        "message": "Menu Item Updated Successfully",
        "data": updated
    }
    

@router.delete("/{menu_id}")
def remove_menu_item(
    menu_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = delete_menu_item(
        db,
        menu_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Menu Item Not Found"
        )

    return deleted


@router.get("/search/")
def search_menu(
    item_name: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return search_menu_item(
        db,
        item_name
    )


@router.get("/pagination/")
def menu_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_menu_pagination(
        db,
        skip,
        limit
    )
    