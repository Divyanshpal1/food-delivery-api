from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DECIMAL,
    Boolean,
    ForeignKey,
    Enum,
    TIMESTAMP
)

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    address = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())


    orders = relationship(
        "Order",
        back_populates="user",
        cascade="all, delete-orphan"
    )



class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_name = Column(String(100), nullable=False)
    owner_name = Column(String(100))
    phone = Column(String(10))
    email = Column(String(100))
    address = Column(Text)

    status = Column(
        Enum("Open", "Closed"),
        default="Open"
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    # Relationships
    menu_items = relationship(
        "MenuItem",
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )

    orders = relationship(
        "Order",
        back_populates="restaurant",
        cascade="all, delete-orphan"
    )



class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id", ondelete="CASCADE")
    )

    item_name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2), nullable=False)
    category = Column(String(50))
    availability = Column(Boolean, default=True)


    restaurant = relationship(
        "Restaurant",
        back_populates="menu_items"
    )

    order_items = relationship(
        "OrderItem",
        back_populates="menu_item",
        cascade="all, delete-orphan"
    )


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE")
    )

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id", ondelete="CASCADE")
    )

    total_amount = Column(DECIMAL(10, 2))

    order_status = Column(
        Enum(
            "Pending",
            "Preparing",
            "Out for Delivery",
            "Delivered",
            "Cancelled"
        ),
        default="Pending"
    )

    order_date = Column(
        TIMESTAMP,
        server_default=func.now()
    )


    user = relationship(
        "User",
        back_populates="orders"
    )

    restaurant = relationship(
        "Restaurant",
        back_populates="orders"
    )

    order_items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

    payment = relationship(
        "Payment",
        back_populates="order",
        uselist=False,
        cascade="all, delete-orphan"
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE")
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id", ondelete="CASCADE")
    )

    quantity = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    # Relationships
    order = relationship(
        "Order",
        back_populates="order_items"
    )

    menu_item = relationship(
        "MenuItem",
        back_populates="order_items"
    )


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        unique=True
    )

    payment_method = Column(
      Enum("UPI", "Credit Card", "Debit Card"),
    )

    payment_status = Column(
        Enum(
            "Pending",
            "Success",
            "Failed"
        ),
        default="Pending"
    )

    transaction_id = Column(String(100))

    payment_date = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    order = relationship(
        "Order",
        back_populates="payment"
    )