from __future__ import annotations

from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, Mapped, mapped_column
from backend.db.base import Base
from backend.db.session import Engine


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

    customer: Mapped["Customer"] = relationship(argument="Customer", back_populates="addresses")

    customer_id: Mapped["Customer"] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class CustomerContact(Base):
    __tablename__ = "customer_contact"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    type: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    contact: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    note: Mapped[str] = mapped_column(type_=String(length=255), nullable=True)

    customer: Mapped["Customer"] = relationship(argument="Customer", back_populates="contacts")

    customer_id: Mapped["Customer"] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Warehouse(Base):
    __tablename__ = "warehouse"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)

    items: Mapped[list["WarehouseItem"]] = relationship(argument="WarehouseItem", back_populates="warehouse")

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class WarehouseItem(Base):
    __tablename__ = "warehouse_item"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    code: Mapped[str] = mapped_column(type_=String(length=255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    price: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)
    count: Mapped[int] = mapped_column(type_=Integer, nullable=False)

    order_item: Mapped["OrderItem"] = relationship(argument="OrderItem", back_populates="warehouse_item")
    warehouse: Mapped["Warehouse"] = relationship(argument="Warehouse", back_populates="items")

    warehouse_id: Mapped["Warehouse"] = mapped_column(ForeignKey("warehouse.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    description: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    total: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)

    items: Mapped[list["OrderItem"]] = relationship(argument="OrderItem", back_populates="order")
    shipment: Mapped["Shipment"] = relationship(argument="Shipment", back_populates="order")
    payment: Mapped["Payment"] = relationship(argument="Payment", back_populates="order")
    customer: Mapped["Order"] = relationship(argument="Customer", back_populates="orders")

    customer_id: Mapped["Customer"] = mapped_column(ForeignKey("customer.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class OrderItem(Base):
    __tablename__ = "order_item"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    quantity: Mapped[int] = mapped_column(type_=Integer, nullable=False)
    total: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)

    order: Mapped["Order"] = relationship(argument="Order", back_populates="items")
    assembly_point_item: Mapped["AssemblyPointItem"] = relationship(argument="AssemblyPointItem", back_populates="order_item")
    warehouse_item: Mapped["WarehouseItem"] = relationship(argument="WarehouseItem", back_populates="order_item")

    order_id: Mapped["Order"] = mapped_column(ForeignKey("order.id"), type_=Integer)
    warehouse_item_id: Mapped["WarehouseItem"] = mapped_column(ForeignKey("warehouse_item.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Shipment(Base):
    __tablename__ = "shipment"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    datetime: Mapped[datetime] = mapped_column(type_=DateTime, nullable=False)
    tracking_number: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    shipment_type: Mapped[int] = mapped_column(type_=Integer, nullable=False)

    order: Mapped["Order"] = relationship(argument="Order", back_populates="shipment")
    assembly_point: Mapped["AssemblyPoint"] = relationship(argument="AssemblyPoint", back_populates="shipment")

    order_id: Mapped["Order"] = mapped_column(ForeignKey("order.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class AssemblyPoint(Base):
    __tablename__ = "assembly_point"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)

    assembly_point: Mapped[list["AssemblyPointItem"]] = relationship(argument="AssemblyPointItem",
                                                                     back_populates="assembly_point")
    shipment: Mapped["Shipment"] = relationship(argument="Shipment", back_populates="assembly_point")

    shipment_id: Mapped[list["Shipment"]] = mapped_column(ForeignKey("shipment.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class AssemblyPointItem(Base):
    __tablename__ = "assembly_point_item"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)

    assembly_point: Mapped["AssemblyPoint"] = relationship(argument="AssemblyPoint", back_populates="assembly_point")
    order_item: Mapped["OrderItem"] = relationship(argument="OrderItem", back_populates="assembly_point_item")

    assembly_point_id: Mapped["AssemblyPoint"] = mapped_column(ForeignKey("assembly_point.id"), type_=Integer)
    order_item_id: Mapped["OrderItem"] = mapped_column(ForeignKey("order_item.id"), type_=Integer)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


class Payment(Base):
    __tablename__ = "payment"
    id: Mapped[int] = mapped_column(type_=Integer, primary_key=True, autoincrement=True)
    payment_data: Mapped[DateTime] = mapped_column(type_=DateTime, nullable=False)
    amount: Mapped[float] = mapped_column(type_=DECIMAL(precision=10, scale=2), nullable=False)
    currency: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    transaction_id: Mapped[str] = mapped_column(type_=String(length=255), nullable=False)
    type: Mapped[int] = mapped_column(type_=Integer, nullable=False)

    order: Mapped["Order"] = relationship(argument="Order", back_populates="payment")

    order_id: Mapped["Order"] = mapped_column(ForeignKey("order.id"), type_=Integer)
    # Payment <-> Customer (???)

    deleted: Mapped[bool] = mapped_column(type_=Boolean, default=False)


Base.metadata.drop_all(Engine)
Base.metadata.create_all(Engine)
