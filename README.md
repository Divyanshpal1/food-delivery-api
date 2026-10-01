# 🍔 Online Food Delivery Api

## Project Description

The Online Food Delivery Management System is a backend REST API developed using FastAPI and MySQL. It allows users to register, log in, manage restaurants, menu items, orders, order items, and payments securely using JWT Authentication.

---

# Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy ORM
- JWT Authentication
- Passlib (Password Hashing)
- Pydantic
- Uvicorn

---

# Project Features

## User Module

- User Registration
- User Login
- JWT Authentication
- Get Profile
- Update Profile
- Delete User

---

## Restaurant Module

- Add Restaurant
- Get All Restaurants
- Get Restaurant By ID
- Update Restaurant
- Delete Restaurant
- Search Restaurant
- Pagination

---

## Menu Module

- Add Menu Item
- Get All Menu Items
- Get Menu By ID
- Update Menu Item
- Delete Menu Item
- Search Menu
- Menu By Restaurant
- Pagination

---

## Orders Module

- Place Order
- Get All Orders
- Get Order By ID
- Update Order Status
- Delete Order
- Search Orders
- Orders By User
- Pagination

---

## Order Items Module

- Add Order Item
- Get All Order Items
- Get Order Item By ID
- Update Order Item
- Delete Order Item
- Search Order Items
- Items By Order
- Pagination

---

## Payments Module

- Add Payment
- Get All Payments
- Get Payment By ID
- Update Payment
- Delete Payment
- Search Payments
- Payments By Order
- Pagination

---

# Authentication

This project uses JWT Authentication.

After login, copy the generated access token.

Click **Authorize** in Swagger UI.

Enter:

Bearer <your_token>

Now all protected APIs can be accessed.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/online-food-delivery.git
```

## Move into Project Folder

```bash
cd online-food-delivery
```

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Configuration

Create MySQL Database

```sql
CREATE DATABASE food_delivery_db;
```

Update your database connection in

database.py

Example

```python
DATABASE_URL = "mysql+pymysql://root:password@localhost/food_delivery_db"
```

---

# Run Project

```bash
uvicorn main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# Folder Structure

```
OnlineFoodDelivery/
│
├── routers/
│   ├── users.py
│   ├── restaurants.py
│   ├── menu.py
│   ├── orders.py
│   ├── order_items.py
│   └── payments.py
│
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── oauth2.py
├── auth.py
├── utils.py
├── main.py
├── requirements.txt
└── README.md
```

---

# API Modules

- Users
- Restaurants
- Menu
- Orders
- Order Items
- Payments

---

# Author

**Name:** Divyansh Pal



Python | FastAPI | SQLAlchemy | MySQL

---

# License

This project is developed for learning purpose.