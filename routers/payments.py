from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database import get_db
from dependencies import get_current_user

from schemas import (
    PaymentCreate,
    PaymentUpdate
)

from crud import (
    create_payment,
    get_all_payments,
    get_payment_by_id,
    get_payments_by_order,
    update_payment,
    delete_payment,
    search_payment,
    get_payments_pagination
)

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


@router.post("/")
def add_payment(
    payment: PaymentCreate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_payment(
        db,
        payment
    )


@router.get("/")
def all_payments(
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_all_payments(db)


@router.get("/{payment_id}")
def payment_by_id(
    payment_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    payment = get_payment_by_id(
        db,
        payment_id
    )

    if payment is None:
        raise HTTPException(
            status_code=404,
            detail="Payment Not Found"
        )

    return payment


@router.get("/order/{order_id}")
def payments_by_order(
    order_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_payments_by_order(
        db,
        order_id
    )



@router.put("/{payment_id}")
def edit_payment(
    payment_id: int,
    payment: PaymentUpdate,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated = update_payment(
        db,
        payment_id,
        payment
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Payment Not Found"
        )

    return {
        "message": "Payment Updated Successfully",
        "data": updated
    }
    

@router.delete("/{payment_id}")
def remove_payment(
    payment_id: int,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    deleted = delete_payment(
        db,
        payment_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Payment Not Found"
        )

    return deleted


@router.get("/search/")
def search_payments(
    payment_method: str,
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return search_payment(
        db,
        payment_method
    )



@router.get("/pagination/")
def payments_pagination(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    current_user: dict = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return get_payments_pagination(
        db,
        skip,
        limit
    )
    
    