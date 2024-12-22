import {deleteData, TableColumn} from "./GenericTable";
import PlusIcon from "@rsuite/icons/Trash";
import {IconButton} from "rsuite";
import React from "react";
import {useQuery} from "@tanstack/react-query";

export type EntityType = "Customers" | "Orders" | "Addresses" | "Contacts"

export class Customer {
    id: number | undefined;
    first_name: string | undefined;
    last_name: string | undefined;
    patronymic: string | undefined;
    nickname: string | undefined;
    sex: boolean | undefined;
    deleted: boolean | undefined;
    eType: EntityType | undefined = "Customers";
}

export class Order {
    id: number | undefined;
    customer_id: number | undefined;
    total: number | undefined;
    code: string | undefined;
    deleted: boolean | undefined;
    eType: EntityType | undefined = "Orders";
}

export class Address {
    id: number | undefined;
    customer_id: number | undefined;
    address: string | undefined;
    deleted: boolean | undefined;
    eType: EntityType | undefined = "Addresses";
}

export class Contact {
    id: number | undefined;
    customer_id: number | undefined;
    type: number | undefined;
    contact: string | undefined;
    note: string | undefined;
    deleted: boolean | undefined;
    eType: EntityType | undefined = "Contacts";
}

export const customerColumns: TableColumn<Customer>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false, visible: false},
    {title: "First Name", dataKey: "first_name", width: 200, fixed: true, editable: true},
    {title: "Last Name", dataKey: "last_name", width: 200, fixed: true, editable: true},
    {title: "Patronymic", dataKey: "patronymic", width: 200, fixed: true, editable: true},
    {title: "Nickname", dataKey: "nickname", width: 200, fixed: true, editable: true},
    {
        title: "Sex",
        dataKey: "sex",
        width: 100,
        fixed: true,
        editable: false,
        render: (customer: Customer) => (customer.sex ? "Male" : "Female"),
    },
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (customer: Customer) => (customer.deleted ? "Deleted" : "Not Deleted"),
        visible: false
    },
];

export const addressColumns: TableColumn<Address>[] = [
    {
        title: "", dataKey: "id", width: 70, align: "center", fixed: true, editable: false,
        render: (address: any, refetch?: (props: any) => any) => {
            return <IconButton size={"xs"} icon={<PlusIcon/>}
                               onClick={() => {
                                   // const {refetch} = useQuery<any>({
                                   //     queryKey: ["Address"]
                                   // });
                                   deleteData({...address, eType: "Addresses"}, refetch).then();
                               }}>Delete</IconButton>
        }
    },
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false, visible: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false, visible: false},
    {title: "Address", dataKey: "address", width: 200, fixed: true, editable: true},
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (address: Address) => (address.deleted ? "Deleted" : "Not Deleted"),
        visible: false
    },
];

export const contactColumns: TableColumn<Contact>[] = [
    {
        title: "", dataKey: "id", width: 70, align: "center", fixed: true, editable: false,
        render: (contact: any, refetch?: (props: any) => any) => {
            return <IconButton size={"xs"} icon={<PlusIcon/>}
                               onClick={() => {
                                   deleteData({...contact, eType: "Contacts"}, refetch).then();
                               }}>Delete</IconButton>
        }
    },
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false, visible: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false, visible: false},
    {
        title: "Contact Type",
        dataKey: "type",
        width: 100,
        fixed: true,
        editable: true,
        render: (contact: Contact) => (contact.type === 1 ? "Phone" : contact.type === 2 ? "Email" : "Unknown"),
    },
    {title: "Contact", dataKey: "contact", width: 200, fixed: true, editable: true},
    {title: "Note", dataKey: "note", width: 200, fixed: true, editable: true},
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (contact: Contact) => (contact.deleted ? "Deleted" : "Not Deleted"),
        visible: false
    },
];

export const orderColumns: TableColumn<Order>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false, visible: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false, visible: false},
    {title: "Total", dataKey: "total", width: 100, fixed: true, editable: false},
    {title: "Code", dataKey: "code", width: 100, fixed: true, editable: false},
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (order: Order) => (order.deleted ? "Deleted" : "Not Deleted"),
        visible: false
    },
];
