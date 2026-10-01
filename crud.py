from sqlalchemy.orm import Session

from models import User, Restaurant, MenuItem, Order, OrderItem, Payment

from schemas import (
    UserRegister,
    UserUpdate,
    RestaurantCreate,
    RestaurantUpdate,
    MenuItemCreate,
    MenuItemUpdate,
    OrderCreate,
    OrderUpdate,
    OrderItemCreate,
    OrderItemUpdate,
    PaymentCreate,
    PaymentUpdate
)

from utils import hash_password


def create_user(db: Session, user: UserRegister):

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=hash_password(user.password),
        address=user.address
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(db: Session, user_id: int):

    return db.query(User).filter(
        User.id == user_id
    ).first()


def get_user_by_email(db: Session, email: str):

    return db.query(User).filter(
        User.email == email
    ).first()


def get_all_users(db: Session):

    return db.query(User).all()


def get_users_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(User).offset(skip).limit(limit).all()


def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate
):

    db_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if db_user is None:
        return None

    if user.full_name is not None:
        db_user.full_name = user.full_name

    if user.phone is not None:
        db_user.phone = user.phone

    if user.address is not None:
        db_user.address = user.address

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    user_id: int
):

    db_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if db_user is None:
        return None

    db.delete(db_user)
    db.commit()

    return {
        "message": "User Deleted Successfully"
    }



def create_restaurant(
    db: Session,
    restaurant: RestaurantCreate
):

    new_restaurant = Restaurant(
        restaurant_name=restaurant.restaurant_name,
        owner_name=restaurant.owner_name,
        phone=restaurant.phone,
        email=restaurant.email,
        address=restaurant.address,
        status=restaurant.status
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return new_restaurant


def get_restaurant_by_id(
    db: Session,
    restaurant_id: int
):

    return db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()


def get_all_restaurants(db: Session):

    return db.query(Restaurant).all()


def get_restaurants_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Restaurant).offset(skip).limit(limit).all()


def search_restaurant(
    db: Session,
    restaurant_name: str
):

    return db.query(Restaurant).filter(
        Restaurant.restaurant_name.ilike(f"%{restaurant_name}%")
    ).all()


def update_restaurant(
    db: Session,
    restaurant_id: int,
    restaurant: RestaurantUpdate
):

    db_restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if db_restaurant is None:
        return None

    if restaurant.restaurant_name is not None:
        db_restaurant.restaurant_name = restaurant.restaurant_name

    if restaurant.owner_name is not None:
        db_restaurant.owner_name = restaurant.owner_name

    if restaurant.phone is not None:
        db_restaurant.phone = restaurant.phone

    if restaurant.email is not None:
        db_restaurant.email = restaurant.email

    if restaurant.address is not None:
        db_restaurant.address = restaurant.address

    if restaurant.status is not None:
        db_restaurant.status = restaurant.status

    db.commit()
    db.refresh(db_restaurant)

    return db_restaurant


def delete_restaurant(
    db: Session,
    restaurant_id: int
):

    db_restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if db_restaurant is None:
        return None

    db.delete(db_restaurant)
    db.commit()

    return {
        "message": "Restaurant Deleted Successfully"
    }
    

def create_menu_item(
    db: Session,
    menu: MenuItemCreate
):

    new_menu = MenuItem(
        restaurant_id=menu.restaurant_id,
        item_name=menu.item_name,
        description=menu.description,
        price=menu.price,
        category=menu.category,
        availability=menu.availability
    )

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return new_menu


def get_menu_item_by_id(
    db: Session,
    menu_id: int
):

    return db.query(MenuItem).filter(
        MenuItem.id == menu_id
    ).first()


def get_all_menu_items(db: Session):

    return db.query(MenuItem).all()


def get_menu_by_restaurant(
    db: Session,
    restaurant_id: int
):

    return db.query(MenuItem).filter(
        MenuItem.restaurant_id == restaurant_id
    ).all()


def get_menu_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(MenuItem).offset(skip).limit(limit).all()


def search_menu_item(
    db: Session,
    item_name: str
):

    return db.query(MenuItem).filter(
        MenuItem.item_name.ilike(f"%{item_name}%")
    ).all()


def update_menu_item(
    db: Session,
    menu_id: int,
    menu: MenuItemUpdate
):

    db_menu = db.query(MenuItem).filter(
        MenuItem.id == menu_id
    ).first()

    if db_menu is None:
        return None

    if menu.item_name is not None:
        db_menu.item_name = menu.item_name

    if menu.description is not None:
        db_menu.description = menu.description

    if menu.price is not None:
        db_menu.price = menu.price

    if menu.category is not None:
        db_menu.category = menu.category

    if menu.availability is not None:
        db_menu.availability = menu.availability

    db.commit()
    db.refresh(db_menu)

    return db_menu


def delete_menu_item(
    db: Session,
    menu_id: int
):

    db_menu = db.query(MenuItem).filter(
        MenuItem.id == menu_id
    ).first()

    if db_menu is None:
        return None

    db.delete(db_menu)
    db.commit()

    return {
        "message": "Menu Item Deleted Successfully"
    }



def create_order(
    db: Session,
    order: OrderCreate
):

    new_order = Order(
        user_id=order.user_id,
        restaurant_id=order.restaurant_id,
        total_amount=order.total_amount,
        order_status="Pending"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def get_order_by_id(
    db: Session,
    order_id: int
):

    return db.query(Order).filter(
        Order.id == order_id
    ).first()


def get_all_orders(
    db: Session
):

    return db.query(Order).all()


def get_orders_by_user(
    db: Session,
    user_id: int
):

    return db.query(Order).filter(
        Order.user_id == user_id
    ).all()


def get_orders_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Order).offset(skip).limit(limit).all()


def search_order(
    db: Session,
    status: str
):

    return db.query(Order).filter(
        Order.order_status.ilike(f"%{status}%")
    ).all()


def update_order(
    db: Session,
    order_id: int,
    order: OrderUpdate
):

    db_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if db_order is None:
        return None

    if order.order_status is not None:
        db_order.order_status = order.order_status

    db.commit()
    db.refresh(db_order)

    return db_order


def cancel_order(
    db: Session,
    order_id: int
):

    db_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if db_order is None:
        return None

    db_order.order_status = "Cancelled"

    db.commit()
    db.refresh(db_order)

    return db_order


def delete_order(
    db: Session,
    order_id: int
):

    db_order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if db_order is None:
        return None

    db.delete(db_order)
    db.commit()

    return {
        "message": "Order Deleted Successfully"
    }
    

def create_order_item(
    db: Session,
    order_item: OrderItemCreate
):

    new_order_item = OrderItem(
        order_id=order_item.order_id,
        menu_item_id=order_item.menu_item_id,
        quantity=order_item.quantity,
        price=order_item.price
    )

    db.add(new_order_item)
    db.commit()
    db.refresh(new_order_item)

    return new_order_item


def get_order_item_by_id(
    db: Session,
    order_item_id: int
):

    return db.query(OrderItem).filter(
        OrderItem.id == order_item_id
    ).first()


def get_order_items_by_order(
    db: Session,
    order_id: int
):

    return db.query(OrderItem).filter(
        OrderItem.order_id == order_id
    ).all()


def get_all_order_items(
    db: Session
):

    return db.query(OrderItem).all()


def get_order_items_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(OrderItem).offset(skip).limit(limit).all()


def search_order_item(
    db: Session,
    order_id: int
):

    return db.query(OrderItem).filter(
        OrderItem.order_id == order_id
    ).all()


def update_order_item(
    db: Session,
    order_item_id: int,
    order_item: OrderItemUpdate
):

    db_order_item = db.query(OrderItem).filter(
        OrderItem.id == order_item_id
    ).first()

    if db_order_item is None:
        return None

    db_order_item.quantity = order_item.quantity

    db.commit()
    db.refresh(db_order_item)

    return db_order_item


def delete_order_item(
    db: Session,
    order_item_id: int
):

    db_order_item = db.query(OrderItem).filter(
        OrderItem.id == order_item_id
    ).first()

    if db_order_item is None:
        return None

    db.delete(db_order_item)
    db.commit()

    return {
        "message": "Order Item Deleted Successfully"
    }

def create_payment(
    db: Session,
    payment: PaymentCreate
):

    new_payment = Payment(
        order_id=payment.order_id,
        payment_method=payment.payment_method,
        payment_status=payment.payment_status,
        transaction_id=payment.transaction_id
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return new_payment


def get_payment_by_id(
    db: Session,
    payment_id: int
):

    return db.query(Payment).filter(
        Payment.id == payment_id
    ).first()


def get_payments_by_order(
    db: Session,
    order_id: int
):

    return db.query(Payment).filter(
        Payment.order_id == order_id
    ).all()


def get_all_payments(
    db: Session
):

    return db.query(Payment).all()


def get_payments_pagination(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return db.query(Payment).offset(skip).limit(limit).all()


def search_payment(
    db: Session,
    payment_method: str
):

    return db.query(Payment).filter(
        Payment.payment_method.ilike(f"%{payment_method}%")
    ).all()


def update_payment(
    db: Session,
    payment_id: int,
    payment: PaymentUpdate
):

    db_payment = db.query(Payment).filter(
        Payment.id == payment_id
    ).first()

    if db_payment is None:
        return None

    if payment.payment_status is not None:
        db_payment.payment_status = payment.payment_status

    db.commit()
    db.refresh(db_payment)

    return db_payment


def delete_payment(
    db: Session,
    payment_id: int
):

    db_payment = db.query(Payment).filter(
        Payment.id == payment_id
    ).first()

    if db_payment is None:
        return None

    db.delete(db_payment)
    db.commit()

    return {
        "message": "Payment Deleted Successfully"
    }
    