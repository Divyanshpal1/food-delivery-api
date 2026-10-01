from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=10)
    password: str = Field(..., min_length=8, max_length=72)
    address: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone: str
    address: str
    created_at: datetime

    class Config:
        from_attributes = True


class RestaurantCreate(BaseModel):
    restaurant_name: str = Field(..., min_length=1)
    owner_name: str
    phone: str = Field(..., min_length=10, max_length=10)
    email: EmailStr
    address: str
    status: str = "Open"


class RestaurantUpdate(BaseModel):
    restaurant_name: Optional[str] = None
    owner_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    status: Optional[str] = None


class RestaurantResponse(BaseModel):
    id: int
    restaurant_name: str
    owner_name: str
    phone: str
    email: EmailStr
    address: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class MenuItemCreate(BaseModel):
    restaurant_id: int
    item_name: str = Field(..., min_length=1)
    description: str
    price: float = Field(..., gt=0)
    category: str
    availability: bool = True


class MenuItemUpdate(BaseModel):
    item_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None
    availability: Optional[bool] = None


class MenuItemResponse(BaseModel):
    id: int
    restaurant_id: int
    item_name: str
    description: str
    price: float
    category: str
    availability: bool

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    total_amount: float = Field(..., gt=0)


class OrderUpdate(BaseModel):
    order_status: str


class OrderResponse(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    total_amount: float
    order_status: str
    order_date: datetime

    class Config:
        from_attributes = True


class OrderItemCreate(BaseModel):
    order_id: int
    menu_item_id: int
    quantity: int = Field(..., gt=0)
    price: float = Field(..., gt=0)


class OrderItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0)


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    menu_item_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True


class PaymentCreate(BaseModel):
    order_id: int
    payment_method: str
    payment_status: str
    transaction_id: str


class PaymentUpdate(BaseModel):
    payment_status: str


class PaymentResponse(BaseModel):
    id: int
    order_id: int
    payment_method: str
    payment_status: str
    transaction_id: str
    payment_date: datetime

    class Config:
        from_attributes = True