from __future__ import annotations

import decimal

from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, UniqueConstraint, DateTime, DECIMAL
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.db.base import Base
from backend.db.session import Engine


# class Test(Base):
#     __tablename__ = 'test'
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String, index=True)
#     also_text = Column(String, index=True)


class Customer(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    last_name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    patronymic: Mapped[str] = mapped_column(type_=String(length=255), nullable=True)
    nickname: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    sex: Mapped[bool] = mapped_column(type_=Boolean, nullable=False)

    addresses: Mapped[list["CustomerAddress"]] = relationship(argument="CustomerAddress", back_populates="customer")
    contacts: Mapped[list["CustomerContact"]] = relationship(argument="CustomerContact", back_populates="customer")
    orders: Mapped[list["Order"]] = relationship(argument="Order", back_populates="customer")

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class CustomerAddress(Base):
    __tablename__ = "customer_address"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    address: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class CustomerContact(Base):
    __tablename__ = "customer_contact"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    contact: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    note: Mapped[str] = mapped_column(type_=String(length=255), nullable=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    total: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)

    items: Mapped[list["OrderItem"]] = relationship(argument="OrderItem", back_populates="order")

    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    total: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), type_=Integer)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    code: Mapped[str] = mapped_column(type_=String(length=255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    price: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)

    order_id: Mapped[list["OrderItem"]] = relationship(argument="OrderItem", back_populates="product")

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Shipment(Base):
    __tablename__ = "shipment"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    datetime: Mapped[datetime] = mapped_column(type_=DateTime, nullable=False)
    tracking_number: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    shipment_type: Mapped[int] = mapped_column(type_=Integer, nullable=False)

    # Shipment <---> Order

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Warehouse(Base):
    __tablename__ = "warehouse"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)

    # Warehouse <-> Product

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Payment(Base):
    __tablename__ = "payment"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)

    # Payment <-> Order
    # Payment <-> Customer (???)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)
