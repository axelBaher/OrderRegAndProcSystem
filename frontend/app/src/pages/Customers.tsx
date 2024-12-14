import React from "react";
import axiosInstance from "../api/axiosInstance";
import {Customer, customerColumns} from "../components/types"
import GenericTable from "../components/GenericTable";


const fetchCustomers = async (): Promise<Customer[]> => {
    try {
        const response = await axiosInstance.get<Customer[]>(
            "https://127.0.0.1:8000/customers");
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const CustomersPage: React.FC = () => {
    return (
        <GenericTable fetchData={fetchCustomers}
                      columns={customerColumns}
                      queryKey={["customers"]}
                      tableTitle={"Customers"}/>
    )
};

export default CustomersPage;