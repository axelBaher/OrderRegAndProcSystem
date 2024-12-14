#   region IMPORT
from fastapi import APIRouter, Depends, status
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel

from backend.app.crud.crud_security import *
from backend.app.dependencies import get_db, security
from backend.app.expection_handler import handle_exceptions

#   endregion
SecurityRouter = APIRouter()


#   region READ_SECURITY
def get_current_customer(token: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    customer_id = verify_token(token.credentials)
    if not customer_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    customer = db.query(m.Customer).filter(m.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return customer


# @SecurityRouter.get(
#     path="/protected",
#     status_code=status.HTTP_200_OK)
# def protected_endpoint(current_user: m.Customer = Depends(get_current_customer)):
#     return {"message": "Hello, authenticated user!"}


#   endregion

#   region CREATE_SECURITY
@SecurityRouter.post(
    path="/register",
    status_code=status.HTTP_201_CREATED)
def register_customer(login: str, password: str, customer_data: dict, db: Session = Depends(get_db)):
    """
    {"first_name": "John", "last_name": "Doe", "patronymic": "Smith", "nickname": "johndoe", "sex": true}
    """
    return handle_exceptions(db=db, query_func=db_register_customer,
                             query_args={"login": login, "password": password, "customer_data": customer_data},
                             expected_status_code=status.HTTP_201_CREATED)


class LoginForm(BaseModel):
    login: str
    password: str


@SecurityRouter.post(
    path="/login",
    status_code=status.HTTP_200_OK)
def login_customer(login_form: LoginForm, db: Session = Depends(get_db)):
    token = db_login_customer(login=login_form.login, password=login_form.password, db=db)
    return token
#   endregion
