#   region IMPORT
import datetime
import jwt
from passlib.context import CryptContext
from fastapi import HTTPException

from backend.app.crud.crud_customer import *


#   endregion
pwd_context = CryptContext(schemes=["scrypt"], default="scrypt")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def check_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def generate_token(customer_id):
    payload = {"customer_id": customer_id}
    expires_in = datetime.datetime.now() + datetime.timedelta(days=365*30)
    payload["exp"] = int(expires_in.timestamp())
    return jwt.encode(payload, "axelbaher", algorithm="HS256")


def verify_token(token):
    try:
        payload = jwt.decode(token, "axelbaher", algorithms=["HS256"])
        return payload["customer_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def db_register_customer(customer_data: dict, db: Session):
    print("CRUD")
    customer_data = customer_data["customer_data"]
    print(customer_data)
    customer = db.query(m.Customer).filter(m.Customer.login == customer_data["login"]).first()
    if customer:
        raise HTTPException(status_code=400, detail="User already exists")
    # hashed_password = hash_password(password=password)
    hashed_password = hash_password(password=customer_data["password"])
    # customer_data["login"] = login
    customer_data["password"] = hashed_password
    new_customer = m.Customer(**customer_data)
    db.add(new_customer)
    db.commit()
    return new_customer


def db_login_customer(login: str, password: str, db: Session):
    customer = db.query(m.Customer).filter(m.Customer.login == login).first()
    if not customer or not check_password(password, customer.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = generate_token(customer.id)
    return token
