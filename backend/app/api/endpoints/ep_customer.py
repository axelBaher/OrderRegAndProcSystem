#   region IMPORT
from fastapi import APIRouter, Depends, status

from backend.app.crud.crud_customer import *
from backend.app.dependencies import get_db
from backend.app.expection_handler import handle_exceptions

#   endregion
CustomerRouter = APIRouter()


#   region READ_CUSTOMER
@CustomerRouter.get(
    path="",
    status_code=status.HTTP_200_OK
)
def get_customer_list(db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_list, query_args={})


@CustomerRouter.get(
    path="/{customer_id}",
    status_code=status.HTTP_200_OK
)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_by_id, query_args={"customer_id": customer_id})


@CustomerRouter.get(
    path="/{customer_id}/addresses",
    status_code=status.HTTP_200_OK
)
def get_customer_address_list(customer_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_address_list, query_args={"customer_id": customer_id})


@CustomerRouter.get(
    path="/{customer_id}/addresses/{address_id}",
    status_code=status.HTTP_200_OK
)
def get_customer_address(customer_id: int, address_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_address,
                             query_args={"customer_id": customer_id, "address_id": address_id})


@CustomerRouter.get(
    path="/{customer_id}/contacts",
    status_code=status.HTTP_200_OK
)
def get_customer_contact_list(customer_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_contact_list, query_args={"customer_id": customer_id})


@CustomerRouter.get(
    path="/{customer_id}/contacts/{contact_id}",
    status_code=status.HTTP_200_OK
)
def get_customer_contact(customer_id: int, contact_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_contact,
                             query_args={"customer_id": customer_id, "contact_id": contact_id})


@CustomerRouter.get(
    path="/{customer_id}/orders",
    status_code=status.HTTP_200_OK
)
def get_customer_order_list(customer_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_order_list, query_args={"customer_id": customer_id})


@CustomerRouter.get(
    path="/{customer_id}/orders/{order_id}",
    status_code=status.HTTP_200_OK
)
def get_customer_order(customer_id: int, order_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_customer_order,
                             query_args={"customer_id": customer_id, "order_id": order_id})


@CustomerRouter.get(
    path="/{customer_id}/orders/{order_id}/order_items",
    status_code=status.HTTP_200_OK
)
def get_order_item_list(customer_id: int, order_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_order_item_list,
                             query_args={"customer_id": customer_id,
                                         "order_id": order_id})


@CustomerRouter.get(
    path="/{customer_id}/orders/{order_id}/payment",
    status_code=status.HTTP_200_OK
)
def get_order_payment(customer_id: int, order_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_order_payment,
                             query_args={"customer_id": customer_id, "order_id": order_id})


@CustomerRouter.get(
    path="/{customer_id}/orders/{order_id}/shipment",
    status_code=status.HTTP_200_OK
)
def get_order_shipment(customer_id: int, order_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_get_order_shipment,
                             query_args={"customer_id": customer_id, "order_id": order_id})


#   endregion

#   region CREATE_CUSTOMER
@CustomerRouter.post(
    path="",
    status_code=status.HTTP_201_CREATED
)
def create_customer(customer_data: dict, db: Session = Depends(get_db)):
    """
    {"first_name": "John", "last_name": "Doe", "patronymic": "Smith", "nickname": "johndoe", "sex": true}
    """
    return handle_exceptions(db=db, query_func=db_create_customer, query_args={"customer_data": customer_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/addresses",
    status_code=status.HTTP_201_CREATED
)
def create_customer_address(customer_id: int, address_data: dict, db: Session = Depends(get_db)):
    """
    {"address": "ул. Пушкина д. Колотушкина"}
    """
    return handle_exceptions(db=db, query_func=db_create_customer_address,
                             query_args={"customer_id": customer_id, "address_data": address_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/contacts",
    status_code=status.HTTP_201_CREATED
)
def create_customer_contact(customer_id: int, contact_data: dict, db: Session = Depends(get_db)):
    """
    {"type": 1, "contact": ajfjkl@email.yes "note": "Work email"}
    {"type": 2, "contact": 81234234544 "note": "Work phone number"}
    """
    return handle_exceptions(db=db, query_func=db_create_customer_contact,
                             query_args={"customer_id": customer_id, "contact_data": contact_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/orders",
    status_code=status.HTTP_201_CREATED
)
def create_customer_order(customer_id: int, order_data: dict, db: Session = Depends(get_db)):
    """
    {"code": "99999"}
    """
    return handle_exceptions(db=db, query_func=db_create_customer_order,
                             query_args={"customer_id": customer_id, "order_data": order_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/orders/{order_id}/order_items",
    status_code=status.HTTP_201_CREATED
)
def create_order_item(customer_id: int, order_id: int, warehouse_item_id: int,
                      order_item_data: dict, db: Session = Depends(get_db)):
    """
    {"quantity": 5}
    """
    return handle_exceptions(db=db, query_func=db_create_order_item,
                             query_args={"customer_id": customer_id, "order_id": order_id,
                                         "warehouse_item_id": warehouse_item_id, "order_item_data": order_item_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/orders/{order_id}/payment",
    status_code=status.HTTP_201_CREATED
)
def create_order_payment(customer_id: int, order_id: int, payment_data: dict, db: Session = Depends(get_db)):
    """
    {"currency": "RUB", "transaction_id": "zz9zzz99-9z9z-9999-zzzz-9zz99z99zz99", "method": 1}
    """
    return handle_exceptions(db=db, query_func=db_create_order_payment,
                             query_args={"customer_id": customer_id, "order_id": order_id, "payment_data": payment_data},
                             expected_status_code=status.HTTP_201_CREATED)


@CustomerRouter.post(
    path="/{customer_id}/orders/{order_id}/shipment",
    status_code=status.HTTP_201_CREATED
)
def create_order_shipment(customer_id: int, order_id: int, shipment_data: dict, db: Session = Depends(get_db)):
    """
    {"tracking_number": "9z9zz9z9-99zz-z9z9-9z9z-9zz9zz9z9999", "shipment_type": 1}
    """
    return handle_exceptions(db=db, query_func=db_create_order_shipment,
                             query_args={"customer_id": customer_id, "order_id": order_id, "shipment_data": shipment_data},
                             expected_status_code=status.HTTP_201_CREATED)


#   endregion

#   region UPDATE_CUSTOMER
@CustomerRouter.put(
    path="/{customer_id}",
    status_code=status.HTTP_200_OK
)
def update_customer(customer_id: int, customer_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_customer,
                             query_args={"customer_id": customer_id, "customer_data": customer_data})


@CustomerRouter.put(
    path="/{customer_id}/addresses/{address_id}",
    status_code=status.HTTP_200_OK
)
def update_customer_address(address_id: int, address_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_customer_address,
                             query_args={"address_id": address_id, "address_data": address_data})


@CustomerRouter.put(
    path="/{customer_id}/contacts/{contact_id}",
    status_code=status.HTTP_200_OK
)
def update_customer_contact(contact_id: int, contact_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_customer_contact,
                             query_args={"contact_id": contact_id, "contact_data": contact_data})


@CustomerRouter.put(
    path="/{customer_id}/orders/{order_id}",
    status_code=status.HTTP_200_OK
)
def update_customer_order(order_id: int, order_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_customer_order,
                             query_args={"order_id": order_id, "order_data": order_data})


@CustomerRouter.put(
    path="/{customer_id}/orders/{order_id}/order_items",
    status_code=status.HTTP_200_OK
)
def update_order_item(order_item_id: int, order_item_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_order_item,
                             query_args={"order_item_id": order_item_id, "order_item_data": order_item_data})


@CustomerRouter.put(
    path="/{customer_id}/orders/{order_id}/payment",
    status_code=status.HTTP_200_OK
)
def update_order_payment(payment_id: int, payment_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_order_payment,
                             query_args={"payment_id": payment_id, "payment_data": payment_data})


@CustomerRouter.put(
    path="/{customer_id}/orders/{order_id}/shipment",
    status_code=status.HTTP_200_OK
)
def update_order_shipment(shipment_id: int, shipment_data: dict, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_update_order_shipment,
                             query_args={"shipment_id": shipment_id, "shipment_data": shipment_data})


#   endregion

#   region DELETE_CUSTOMER
@CustomerRouter.delete(
    path="/{customer_id}"
)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(
        db=db,
        query_func=db_delete_customer,
        query_args={"customer_id": customer_id}
    )


@CustomerRouter.delete(
    path="/{customer_id}/addresses"
)
def delete_customer_address(customer_id: int, address_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_delete_customer_address,
                             query_args={"customer_id": customer_id, "address_id": address_id})


@CustomerRouter.delete(
    path="/{customer_id}/contacts"
)
def delete_customer_contact(customer_id: int, contact_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_delete_customer_contact,
                             query_args={"customer_id": customer_id, "contact_id": contact_id})


@CustomerRouter.delete(
    path="/{customer_id}/orders/{order_id}"
)
def delete_customer_order(customer_id: int, order_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_delete_customer_order,
                             query_args={"customer_id": customer_id, "order_id": order_id})


@CustomerRouter.delete(
    path="/{customer_id}/orders/{order_id}/order_items"
)
def delete_order_item(customer_id: int, order_id: int, order_item_id: int, db: Session = Depends(get_db)):
    return handle_exceptions(db=db, query_func=db_delete_order_item,
                             query_args={"customer_id": customer_id, "order_id": order_id, "order_item_id": order_item_id})


# @CustomerRouter.delete(
#     path="/{customer_id}/orders/{order_id}/payment"
# )
# def delete_order_payment(customer_id: int, order_id: int, payment_id: int, db: Session = Depends(get_db)):
#     pass
#
#
# @CustomerRouter.delete(
#     path="/{customer_id}/orders/{order_id}/shipment"
# )
# def delete_order_shipment(customer_id: int, order_id: int, shipment_id: int, db: Session = Depends(get_db)):
#     pass

#   endregion
