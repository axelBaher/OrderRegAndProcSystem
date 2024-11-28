import React from "react";
import {
    Customer,
    Address,
    Contact,
    customerColumns,
    addressColumns,
    contactColumns,
    Order,
    orderColumns
} from "../components/types";
import axiosInstance from "../api/axiosInstance";
import GenericTable from "../components/GenericTable";


// const fetchCustomerDetails = async () => {
//     const [customerData, addressData, contactData
//     ] = await Promise.all([
//         axiosInstance.get("https://127.0.0.1:8000/customers/1"),
//         axiosInstance.get("https://127.0.0.1:8000/customers/1/addresses"),
//         axiosInstance.get("https://127.0.0.1:8000/customers/1/contacts"),
//     ]);
//
//     return {
//         customer: customerData.data,
//         address: addressData.data,
//         contact: contactData.data
//     };
// };
const fetchCustomer = async (): Promise<Customer[]> => {
    try {
        const response = await axiosInstance.get<Customer>(
            "https://127.0.0.1:8000/customers/1");
        return [response.data];
    } catch (e) {
        console.log(e)
        throw e
    }
};
const fetchCustomerAddress = async (): Promise<Address[]> => {
    try {
        const response = await axiosInstance.get<Address[]>(
            "https://127.0.0.1:8000/customers/1/addresses");
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};
const fetchCustomerContact = async (): Promise<Contact[]> => {
    try {
        const response = await axiosInstance.get<Contact[]>(
            "https://127.0.0.1:8000/customers/1/contacts");
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const fetchCustomerOrder = async (): Promise<Order[]> => {
    try {
        const response = await axiosInstance.get<Order[]>(
            "https://127.0.0.1:8000/customers/1/orders");
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const CustomerDetailsPage: React.FC = () => {
    return (
        <div>
        <GenericTable fetchData={fetchCustomer} columns={customerColumns} queryKey={["customer"]} tableTitle={"Customer"}/>
        <GenericTable fetchData={fetchCustomerAddress} columns={addressColumns} queryKey={["addresses"]} tableTitle={"Addresses"}/>
        <GenericTable fetchData={fetchCustomerContact} columns={contactColumns} queryKey={["contacts"]} tableTitle={"Contacts"}/>
        <GenericTable fetchData={fetchCustomerOrder} columns={orderColumns} queryKey={["orders"]} tableTitle={"Orders"}/>
        </div>
    )
};

export default CustomerDetailsPage;