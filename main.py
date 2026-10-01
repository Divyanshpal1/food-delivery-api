from fastapi import FastAPI

from database import Base, engine
import models


from auth import router as auth_router
from routers.users import router as user_router
from routers.restaurants import router as restaurant_router
from routers.menu import router as menu_router
from routers.orders import router as order_router
from routers.order_items import router as order_item_router
from routers.payments import router as payment_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Online Food Delivery Management System API",
    description="Advanced FastAPI Project using MySQL, SQLAlchemy ORM and JWT Authentication",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Online Food Delivery Management System API",
        "status": "Running Successfully"
    }



app.include_router(auth_router)
app.include_router(user_router)
app.include_router(restaurant_router)
app.include_router(menu_router)
app.include_router(order_router)
app.include_router(order_item_router)
app.include_router(payment_router)