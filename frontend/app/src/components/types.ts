import {TableColumn} from "./GenericTable";

export interface Customer {
    id: number;
    first_name: string;
    last_name: string;
    patronymic: string;
    nickname: string;
    sex: boolean;
    deleted: boolean;
}

export interface Order {
    id: number;
    customer_id: number;
    total: number;
    code: string;
    deleted: boolean;
}

export interface Address {
    id: number;
    customer_id: number;
    address: string;
    deleted: boolean;
}

export interface Contact {
    id: number;
    customer_id: number;
    type: number;
    contact: string;
    note: string;
    deleted: boolean;
}

export interface Order {
    id: number;
    customer_id: number;
    total: number;
    code: string;
    deleted: boolean;
}

export interface CustomerDetails {
    id: number;
}

export const customerColumns: TableColumn<Customer>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false},
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
    },
];

export const addressColumns: TableColumn<Address>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false},
    {title: "Address", dataKey: "address", width: 200, fixed: true, editable: true},
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (address: Address) => (address.deleted ? "Deleted" : "Not Deleted"),
    },
];

export const contactColumns: TableColumn<Contact>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false},
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
    },
];

export const customerDetailsColumns: TableColumn<CustomerDetails>[] = [];

export const orderColumns: TableColumn<Order>[] = [
    {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true, editable: false},
    {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true, editable: false},
    {title: "Total", dataKey: "total", width: 100, fixed: true, editable: false},
    {title: "Code", dataKey: "code", width: 100, fixed: true, editable: false},
    {
        title: "Deleted",
        dataKey: "deleted",
        width: 100,
        fixed: true,
        editable: false,
        render: (order: Order) => (order.deleted ? "Deleted" : "Not Deleted"),
    },
];
