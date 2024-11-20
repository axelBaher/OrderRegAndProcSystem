#   region IMPORT
from typing import Type
from sqlalchemy.orm import Session
from faker import Faker

from backend.app import models as m

#   endregion
fake = Faker(["en_US", "en_PH"])


#   region READ_CUSTOMER
def db_get_customer_list(db: Session) -> list[Type[m.Customer]] | None:
    customer_list = db.query(m.Customer).filter(m.Customer.deleted == 0).all()
    # from sqlalchemy.sql import text
    # from sqlalchemy import select
    # customer_list = db.execute(select(m.Customer)).scalars().all()
    # customer_list = db.execute(text("select * from customer")).fetchone()    # print(customer_list)
    # customer_list = db.execute(text("select * from customer")).fetchmany()   # print([row._mapping for row in customer_list])
    return customer_list


def db_get_customer_by_id(customer_id: int, db: Session) -> Type[m.Customer] | None:
    customer = db.query(m.Customer).filter(m.Customer.id == customer_id,
                                           m.Customer.deleted == 0).first()
    return customer


def db_get_customer_address_list(customer_id: int, db: Session) -> list[Type[m.CustomerAddress]] | None:
    address_list = db.query(m.CustomerAddress).join(m.Customer).filter(m.CustomerAddress.customer_id == customer_id,
                                                                       m.CustomerAddress.deleted == 0).all()
    return address_list


def db_get_customer_address(customer_id: int, address_id: int, db: Session) -> Type[m.CustomerAddress] | None:
    address = db.query(m.CustomerAddress).join(m.Customer).filter(m.CustomerAddress.customer_id == customer_id,
                                                                  m.CustomerAddress.id == address_id,
                                                                  m.CustomerAddress.deleted == 0).first()
    return address


def db_get_customer_contact_list(customer_id: int, db: Session) -> list[Type[m.CustomerContact]] | None:
    contact_list = db.query(m.CustomerContact).join(m.Customer).filter(m.CustomerContact.customer_id == customer_id,
                                                                       m.CustomerContact.deleted == 0).all()
    return contact_list


def db_get_customer_contact(customer_id: int, contact_id: int, db: Session) -> Type[m.CustomerContact] | None:
    contact = db.query(m.CustomerContact).join(m.Customer).filter(m.CustomerContact.customer_id == customer_id,
                                                                  m.CustomerContact.id == contact_id,
                                                                  m.CustomerContact.deleted == 0).first()
    return contact


def db_get_customer_order_list(customer_id: int, db: Session) -> list[Type[m.Order]] | None:
    order_list = db.query(m.Order).filter(m.Order.customer_id == customer_id, m.Order.deleted == 0).all()
    return order_list


def db_get_customer_order(customer_id: int, order_id: int, db: Session) -> Type[m.Order] | None:
    order = db.query(m.Order).join(m.Customer).filter(m.Order.id == order_id, m.Customer.id == customer_id,
                                                      m.Order.deleted == 0).first()
    return order


def db_get_order_item_list(customer_id: int, order_id: int, db: Session) -> (list[Type[m.OrderItem]] | None):
    order_item_list = db.query(m.OrderItem).filter(m.OrderItem.order_id == order_id).join(m.Order).filter(
        m.Order.customer_id == customer_id, m.Order.deleted == 0).all()
    return order_item_list


def db_get_order_payment(customer_id: int, order_id: int, db: Session) -> Type[m.Payment] | None:
    payment = db.query(m.Payment).join(m.Order).filter(
        m.Order.customer_id == customer_id, m.Payment.order_id == order_id, m.Payment.deleted == 0).first()
    return payment


def db_get_order_shipment(customer_id: int, order_id: int, db: Session) -> Type[m.Shipment] | None:
    shipment = db.query(m.Shipment).join(m.Order).filter(
        m.Order.customer_id == customer_id, m.Shipment.order_id == order_id, m.Shipment.deleted == 0).first()
    return shipment


#   endregion

#   region CREATE_CUSTOMER
def db_create_customer(customer_data: dict, db: Session) -> m.Customer:
    new_customer = m.Customer(**customer_data)
    db.add(new_customer)
    db.commit()
    return new_customer


def db_create_customer_address(customer_id: int, address_data: dict, db: Session) -> m.CustomerAddress | None:
    customer = db_get_customer_by_id(customer_id=customer_id, db=db)
    if customer is None:
        return None
    new_address = m.CustomerAddress(**address_data)
    new_address.customer_id = customer_id
    db.add(new_address)
    db.commit()
    return new_address


def db_create_customer_contact(customer_id: int, contact_data: dict, db: Session) -> m.CustomerContact | None:
    customer = db_get_customer_by_id(customer_id=customer_id, db=db)
    if customer is None:
        return None
    new_contact = m.CustomerContact(**contact_data)
    new_contact.customer_id = customer_id
    db.add(new_contact)
    db.commit()
    return new_contact


def db_create_customer_order(customer_id: int, order_data: dict, db: Session) -> m.Order | None:
    customer = db_get_customer_by_id(customer_id=customer_id, db=db)
    if customer is None:
        return None
    new_order = m.Order(**order_data)
    new_order.customer_id = customer_id
    new_order.total = 0.0
    db.add(new_order)
    db.commit()
    return new_order


def db_create_order_item(customer_id: int, order_id: int, warehouse_item_id: int,
                         order_item_data: dict, db: Session) -> m.OrderItem | None:
    order = db_get_customer_order(customer_id=customer_id, order_id=order_id, db=db)
    warehouse_item = db.query(m.WarehouseItem).filter(m.WarehouseItem.id == warehouse_item_id).first()
    if (order is None) or (warehouse_item is None) or (order_item_data["quantity"] > warehouse_item.quantity):
        return None
    new_order_item = m.OrderItem(**order_item_data)
    new_order_item.order_id = order_id
    new_order_item.warehouse_item_id = warehouse_item_id
    new_order_item.total = new_order_item.quantity * warehouse_item.price
    order.total += new_order_item.total
    warehouse_item.quantity -= order_item_data["quantity"]
    db.add(new_order_item)
    db.commit()
    return new_order_item


def db_create_order_payment(customer_id: int, order_id: int, payment_data: dict, db: Session) -> m.Payment | None:
    order = db_get_customer_order(customer_id=customer_id, order_id=order_id, db=db)
    order_payment = db_get_order_payment(customer_id=customer_id, order_id=order_id, db=db)
    if (order is None) or (order_payment is not None) or order.total == 0:
        return None
    new_payment = m.Payment(**payment_data)
    new_payment.order_id = order_id
    new_payment.amount = order.total
    db.add(new_payment)
    db.commit()
    return new_payment


def db_create_order_shipment(customer_id: int, order_id: int, shipment_data: dict, db: Session) -> m.Shipment | None:
    order = db_get_customer_order(customer_id=customer_id, order_id=order_id, db=db)
    order_shipment = db_get_order_shipment(customer_id=customer_id, order_id=order_id, db=db)
    order_payment = db_get_order_payment(customer_id=customer_id, order_id=order_id, db=db)
    if (order is None) or (order_payment is None) or (order_shipment is not None):
        return None
    new_shipment = m.Shipment(**shipment_data)
    new_shipment.order_id = order_id
    db.add(new_shipment)
    db.commit()
    return new_shipment


# endregion

#   region UPDATE_CUSTOMER
def db_update_customer(customer_id: int, customer_data: dict, db: Session) -> Type[m.Customer] | None:
    customer = db.query(m.Customer).filter(m.Customer.id == customer_id).first()
    if customer:
        updated = False
        for key, value in customer_data.items():
            if hasattr(customer, key):
                new_value = getattr(customer, key)
                if new_value != value:
                    setattr(customer, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(customer)
        return customer


def db_update_customer_address(address_id: int, address_data: dict, db: Session) -> Type[m.CustomerAddress] | None:
    address = db.query(m.CustomerAddress).filter(m.CustomerAddress.id == address_id).first()
    if address:
        updated = False
        for key, value in address_data.items():
            if hasattr(address, key):
                new_value = getattr(address, key)
                if new_value != value:
                    setattr(address, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(address)
        return address


def db_update_customer_contact(contact_id: int, contact_data: dict, db: Session) -> Type[m.CustomerContact] | None:
    contact = db.query(m.CustomerContact).filter(m.CustomerContact.id == contact_id).first()
    if contact:
        updated = False
        for key, value in contact_data.items():
            if hasattr(contact, key):
                new_value = getattr(contact, key)
                if new_value != value:
                    setattr(contact, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(contact)
        return contact


def db_update_customer_order(order_id: int, order_data: dict, db: Session) -> Type[m.Order] | None:
    order = db.query(m.Order).filter(m.Order.id == order_id).first()
    if order:
        updated = False
        for key, value in order_data.items():
            if hasattr(order, key):
                new_value = getattr(order, key)
                if new_value != value:
                    setattr(order, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(order)
        return order


def db_update_order_item(order_item_id: int, order_item_data: dict, db: Session) -> Type[m.OrderItem] | None:
    order_item = db.query(m.OrderItem).filter(m.OrderItem.id == order_item_id).first()
    if order_item:
        updated = False
        for key, value in order_item_data.items():
            if hasattr(order_item, key):
                new_value = getattr(order_item, key)
                if new_value != value:
                    setattr(order_item, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(order_item)
        return order_item


def db_update_order_payment(payment_id: int, payment_data: dict, db: Session) -> Type[m.Payment] | None:
    payment = db.query(m.Payment).filter(m.Payment.id == payment_id).first()
    if payment:
        updated = False
        for key, value in payment_data.items():
            if hasattr(payment, key):
                new_value = getattr(payment, key)
                if new_value != value:
                    setattr(payment, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(payment)
        return payment


def db_update_order_shipment(shipment_id: int, shipment_data: dict, db: Session) -> Type[m.Shipment] | None:
    shipment = db.query(m.Shipment).filter(m.Shipment.id == shipment_id).first()
    if shipment:
        updated = False
        for key, value in shipment_data.items():
            if hasattr(shipment, key):
                new_value = getattr(shipment, key)
                if new_value != value:
                    setattr(shipment, key, value)
                    updated = True
        if updated:
            db.commit()
            db.refresh(shipment)
        return shipment


# endregion

#   region DELETE_CUSTOMER
def db_delete_customer(customer_id: int, db: Session):
    customer = db_get_customer_by_id(customer_id=customer_id, db=db)
    if customer and (customer.addresses is None and customer.contacts is None and customer.orders is None):
        db.delete(customer)
        db.commit()
        return customer


def db_delete_customer_address(customer_id: int, address_id: int, db: Session):
    address = db_get_customer_address(customer_id=customer_id, address_id=address_id, db=db)
    if address:
        db.delete(address)
        db.commit()
        return address


def db_delete_customer_contact(customer_id: int, contact_id: int, db: Session):
    contact = db_get_customer_contact(customer_id=customer_id, contact_id=contact_id, db=db)
    if contact:
        db.delete(contact)
        db.commit()
        return contact


def db_delete_customer_order(customer_id: int, order_id: int, db: Session):
    order = db_get_customer_order(customer_id=customer_id, order_id=order_id, db=db)
    if order:
        if order.items is None:
            db.delete(order)
            db.commit()
            return order


def db_delete_order_item(customer_id: int, order_id: int, order_item_id: int, db: Session):
    order_item = db.query(m.OrderItem).filter(m.OrderItem.id == order_item_id).first()
    warehouse_item = db.query(m.WarehouseItem).filter(m.WarehouseItem.order_item == order_item).first()
    order = db.query(m.Order).filter(m.Order.customer_id == customer_id, m.Order.id == order_id).first()
    if order_item and warehouse_item:
        warehouse_item.quantity += order_item.quantity
        order.total -= order_item.total
        db.delete(order_item)
        db.commit()
        return order_item


def db_delete_order_payment(order_id: int, order_payment_id: int, db: Session):
    pass


def db_delete_order_shipment(shipment_id: int, shipment_data: dict, db: Session):
    pass

# endregion
