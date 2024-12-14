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
import GenericTable from "../components/GenericTable";
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

function getCustomerID(): number {
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
const fetchCustomer = async (): Promise<Customer[]> => {
    try {
        const response = await axiosInstance.get<Customer>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}`);
        return [response.data];
    } catch (e) {
        // console.log(e)
        throw e
    }
};
const fetchCustomerAddress = async (): Promise<Address[]> => {
    try {
        const response = await axiosInstance.get<Address[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/addresses`);
        return response.data;
    } catch (e) {
        // console.log(e)
        throw e
    }
};
const fetchCustomerContact = async (): Promise<Contact[]> => {
    try {
        const response = await axiosInstance.get<Contact[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/contacts`);
        return response.data;
    } catch (e) {
        // console.log(e)
        throw e
    }
};

const fetchCustomerOrder = async (): Promise<Order[]> => {
    try {
        const response = await axiosInstance.get<Order[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/orders`);
        return response.data;
    } catch (e) {
        // console.log(e)
        throw e
    }
};

const CustomerDetailsPage: React.FC = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const token = localStorage.getItem("token");
    console.log("Loc. key: " + location.key);
    useEffect(() => {
    if ((location.key === "default") && (!token)) {
      navigate("/login");
    }
  }, [location.key, token, navigate]);
    return (
        <div>
            <GenericTable fetchData={fetchCustomer} columns={customerColumns} queryKey={["customer"]} tableTitle={"Customer"}/>
            <GenericTable fetchData={fetchCustomerAddress} columns={addressColumns} queryKey={["addresses"]}
                          tableTitle={"Addresses"}/>
            <GenericTable fetchData={fetchCustomerContact} columns={contactColumns} queryKey={["contacts"]}
                          tableTitle={"Contacts"}/>
            <GenericTable fetchData={fetchCustomerOrder} columns={orderColumns} queryKey={["orders"]} tableTitle={"Orders"}/>
        </div>
    )
};

export default CustomerDetailsPage;