#   region IMPORT
import random
import itertools
from faker import Faker

from sqlalchemy.orm import Session
from backend.app import models as m
from backend.app.schemas import *

#   endregion


fake = Faker(["en_US", "en_PH"])


def db_clear_database(db: Session) -> None:
    db.query(m.CustomerAddress).delete()
    db.query(m.CustomerContact).delete()
    db.query(m.AssemblyPointItem).delete()
    db.query(m.AssemblyPoint).delete()
    db.query(m.Shipment).delete()
    db.query(m.OrderItem).delete()
    db.query(m.WarehouseItem).delete()
    db.query(m.Payment).delete()
    db.query(m.Warehouse).delete()
    db.query(m.Order).delete()
    db.query(m.Customer).delete()
    db.commit()


# noinspection PyTypeChecker
def db_fill_database(db: Session, db_count: int = 3) -> None:
    def db_fill_customers(count: int = 1) -> None:
        for _ in range(count):
            customer_sex = random.choice([True, False])
            customer = m.Customer(
                first_name=fake.first_name_male() if customer_sex else fake.first_name_female(),
                last_name=fake.last_name_male() if customer_sex else fake.last_name_female(),
                patronymic=(fake.middle_name_male() if customer_sex else fake.middle_name_female())
                if fake.locale() == "ru_RU" else "",
                nickname=fake.user_name(),
                sex=customer_sex,
            )
            customer.login = customer.nickname
            customer.password = "sys"
            customers.append(customer)

    def db_fill_addresses(customer_idx: int, count: int = 1) -> None:
        for _ in range(count):
            address = m.CustomerAddress(
                address=fake.address(),
                customer_id=customers[customer_idx].id
            )
            addresses.append(address)

    def db_fill_contacts(customer_idx: int, count: int = 1) -> None:
        for _ in range(count):
            contact_type = random.randint(1, 2)
            contact = m.CustomerContact(
                type=contact_type,
                contact=fake.email() if contact_type == 1 else fake.phone_number(),
                note=fake.sentence(),
                customer_id=customers[customer_idx].id
            )
            contacts.append(contact)

    def db_fill_warehouses(count: int = 1) -> None:
        for _ in range(count):
            warehouse = m.Warehouse()
            warehouses.append(warehouse)

    def db_fill_warehouse_items(warehouse_idx: int, count: int = 1) -> None:
        for _ in range(count):
            warehouse_item = m.WarehouseItem(
                name=fake.random_object_name(),
                code=fake.zipcode_plus4(),
                description=fake.sentence(nb_words=(random.randint(1, 5))),
                price=round(random.uniform(1, 1000), 2),
                quantity=random.randint(1, 1000),
                warehouse_id=warehouses[warehouse_idx].id
            )
            warehouse_items.append(warehouse_item)

    def db_fill_orders(customer_idx: int, count: int = 1) -> None:
        for _ in range(count):
            order = m.Order(
                code=fake.zipcode(),
                total=0,
                customer_id=customers[customer_idx].id
            )
            orders.append(order)

    def db_fill_order_items(order_idx: int, warehouse_item_idx: int, count: int = 1) -> None:
        for _ in range(count):
            quantity = random.randint(1, min(10, warehouse_items[warehouse_item_idx].quantity))
            order_item = m.OrderItem(
                quantity=quantity,
                total=0,
                order_id=orders[order_idx].id,
                warehouse_item_id=warehouse_items[warehouse_item_idx].id
            )
            order_item.total += warehouse_items[warehouse_item_idx].price * order_item.quantity
            orders[order_idx].total += order_item.total
            warehouse_items[warehouse_item_idx].quantity -= quantity

            order_items.append(order_item)

    def db_fill_shipments(order_idx: int, count: int = 1) -> None:
        shipment_types = [1, 2, 3, 4, 5]
        for _ in range(count):
            shipment = m.Shipment(
                datetime=fake.date_time_between(start_date="-30d", end_date="now"),
                tracking_number=fake.uuid4(),
                shipment_type=random.choice(shipment_types),
                order_id=orders[order_idx].id
            )
            shipments.append(shipment)

    def db_fill_assembly_points() -> None:
        def db_init_assembly_points(c: int = 1) -> None:
            for _ in range(c):
                assembly_point = m.AssemblyPoint(
                    name=f"Assembly Point {fake.city()}",
                )
                assembly_points.append(assembly_point)

        db_init_assembly_points(c=round(len(shipments) / len(warehouses)))

        assembly_points_cycle = itertools.cycle(assembly_points)
        for ship in shipments:
            ass_point = next(assembly_points_cycle)
            assembly_point_shipment = m.AssemblyPointShipment(
                assembly_point=ass_point,
                shipment=ship
            )
            assembly_point_shipments.append(assembly_point_shipment)

    def db_fill_payments(order_idx: int, count: int = 1) -> None:
        for _ in range(count):
            # noinspection PyTypeChecker
            payment = m.Payment(
                payment_data=fake.date_time_between(start_date="-30d", end_date="now"),
                amount=round(random.uniform(10, 10000), 2),
                currency=(random.choice(list(CurrencyCode))).value,
                transaction_id=fake.uuid4(),
                method=(random.choice(list(PaymentMethod))).value,
                order_id=orders[order_idx].id
            )
            payments.append(payment)

    customers = list()
    db_fill_customers(count=db_count)
    db.add_all(customers)
    db.flush()

    addresses = list()
    for cust_idx, cust in enumerate(customers):
        db_fill_addresses(customer_idx=cust_idx, count=db_count)
    db.add_all(addresses)
    db.flush()

    contacts = list()
    for cust_idx, cust in enumerate(customers):
        db_fill_contacts(customer_idx=cust_idx, count=db_count)
    db.add_all(contacts)
    db.flush()

    warehouses = list()
    db_fill_warehouses(count=db_count)
    db.add_all(warehouses)
    db.flush()

    warehouse_items = list()
    for whouse_idx, whouse in enumerate(warehouses):
        db_fill_warehouse_items(warehouse_idx=whouse_idx, count=db_count)
    db.add_all(warehouse_items)
    db.flush()

    orders = list()
    for cust_idx, cust in enumerate(customers):
        db_fill_orders(customer_idx=cust_idx, count=db_count)
    db.add_all(orders)
    db.flush()

    order_items = list()
    for (ord_idx, ordr), (whouse_itm_idx, whouse_itm) in zip(enumerate(orders), enumerate(warehouse_items)):
        db_fill_order_items(order_idx=ord_idx, warehouse_item_idx=whouse_itm_idx)
    db.add_all(order_items)
    db.flush()

    # for ord_c in range(orders_count):
    #     for wh_items_c in range(warehouse_items_count):
    #         quantity = random.randint(1, min(10, warehouse_items[wh_items_c].count))
    #         order_item = m.OrderItem(
    #             quantity=quantity,
    #             order_id=orders[ord_c].id,
    #             warehouse_item_id=warehouse_items[wh_items_c].id
    #         )
    #         order_item.total = order_item.quantity * warehouse_items[wh_items_c].price
    #         order_items.append(order_item)
    #         warehouse_items[wh_items_c].count -= order_item.quantity
    #     orders[ord_c].total = sum(order_item.total for order_item in order_items if order_item.order_id == orders[ord_c].id)

    shipments = list()
    for ord_idx, ordr in enumerate(orders):
        db_fill_shipments(order_idx=ord_idx)
    db.add_all(shipments)
    db.flush()

    assembly_points = list()
    assembly_point_shipments = list()
    db_fill_assembly_points()
    db.add_all(assembly_points)
    db.add_all(assembly_point_shipments)
    db.flush()

    # for _ in range(count):
    #     for i in range(count):
    #         for j in range(count):
    #             assembly_point_item = m.AssemblyPointItem(
    #                 assembly_point_id=assembly_points[i].id,
    #                 order_item_id=order_items[j].id
    #             )
    #             assembly_point_items.append(assembly_point_item)
    # db.add_all(assembly_point_items)
    # db.flush()

    payments = list()
    for ord_idx, ordr in enumerate(orders):
        db_fill_payments(order_idx=ord_idx)
    db.add_all(payments)

    db.commit()
