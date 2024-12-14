// CustomerDetails.tsx
import React, {useEffect} from "react";
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
import GenericTable, {saveData} from "../components/GenericTable";
import {jwtDecode} from 'jwt-decode';
import {useLocation, useNavigate} from "react-router-dom";

export function getDecodedAccessToken(token: string | null): any {
    try {
        if (!token) return {};
        return jwtDecode(token);
    } catch (Error) {
        return null;
    }
}

export function getCustomerID(): number {
    const token = getDecodedAccessToken(localStorage.getItem("token"));
    try {
        if (!token) return 0;
        return token.customer_id;
    } catch (Error) {
        return -1;
    }
}

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
const GET_fetchCustomer = async (): Promise<Customer[]> => {
    try {
        const response = await axiosInstance.get<Customer>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}`);
        return [response.data];
    } catch (e) {
        console.log(e)
        throw e
    }
};
const GET_fetchCustomerAddressList = async (): Promise<Address[]> => {
    try {
        const response = await axiosInstance.get<Address[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/addresses`);
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};
const GET_fetchCustomerContactList = async (): Promise<Contact[]> => {
    try {
        const response = await axiosInstance.get<Contact[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/contacts`);
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const GET_fetchCustomerOrderList = async (): Promise<Order[]> => {
    try {
        const response = await axiosInstance.get<Order[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/orders`);
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const CustomerDetailsPage: React.FC = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const token = localStorage.getItem("token");
    const customerID = getCustomerID();
    const addressID = -1;
    const contactID = -1;
    const orderID = -1;
    // console.log("Loc. key: " + location.key);
    useEffect(() => {
        if ((location.key === "default") && (!token)) {
            navigate("/login");
        }
    }, [location.key, token, navigate]);
    return (
        <div>
            <GenericTable fetchData={GET_fetchCustomer} columns={customerColumns} queryKey={["customer"]} tableTitle={"Customer"}
                          saveData={(data) => saveData(`/customers/${customerID}`, data)}/>
            <GenericTable fetchData={GET_fetchCustomerAddressList} columns={addressColumns} queryKey={["addresses"]}
                          tableTitle={"Addresses"}
                          saveData={(data) => saveData(`/customers/${customerID}/addresses/${addressID}`, data)}/>
            <GenericTable fetchData={GET_fetchCustomerContactList} columns={contactColumns} queryKey={["contacts"]}
                          tableTitle={"Contacts"}
                          saveData={(data) => saveData(`/customers/${customerID}/contacts/${contactID}`, data)}/>
            <GenericTable fetchData={GET_fetchCustomerOrderList} columns={orderColumns} queryKey={["orders"]} tableTitle={"Orders"}
                          saveData={(data) => saveData(`/customers/${customerID}/orders/${orderID}`, data)}/>
        </div>
    )
};

export default CustomerDetailsPage;