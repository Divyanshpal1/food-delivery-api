from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user

from schemas import (
    RestaurantCreate,
    RestaurantUpdate
)

from crud import (
    create_restaurant,
    get_all_restaurants,
    get_restaurant_by_id,
    update_restaurant,
    delete_restaurant,
    search_restaurant,
    get_restaurants_pagination
)

router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurants"]
)



@router.post("/")
def add_restaurant(
    restaurant: RestaurantCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_restaurant(
        db,
        restaurant
    )


@router.get("/")
def all_restaurants(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_all_restaurants(db)


@router.get("/{restaurant_id}")
def restaurant_by_id(
    restaurant_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    restaurant = get_restaurant_by_id(
        db,
        restaurant_id
    )

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Not Found"
        )

    return restaurant



@router.put("/{restaurant_id}")
def edit_restaurant(
    restaurant_id: int,
    restaurant: RestaurantUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated = update_restaurant(
        db,
        restaurant_id,
        restaurant
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Not Found"
        )

    return {
        "message": "Restaurant Updated Successfully",
        "data": updated
    }
    

@router.delete("/{restaurant_id}")
def remove_restaurant(
    restaurant_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = delete_restaurant(
        db,
        restaurant_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant Not Found"
        )

    return deleted



@router.get("/search/")
def search(
    restaurant_name: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return search_restaurant(
        db,
        restaurant_name
    )


@router.get("/pagination/")
def pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_restaurants_pagination(
        db,
        skip,
        limit
    )