import React from "react";
import axiosInstance from "../api/axiosInstance";
import {Order, orderColumns} from "../components/types"
import GenericTable from "../components/GenericTable";
import {getCustomerID} from "./CustomerDetails";


const fetchOrders = async (): Promise<Order[]> => {
    try {
        const response = await axiosInstance.get<Order[]>(
            `https://127.0.0.1:8000/customers/${getCustomerID()}/orders`);
        return response.data;
    } catch (e) {
        console.log(e)
        throw e
    }
};

const OrdersPage: React.FC = () => {
    return (
        <GenericTable fetchData={fetchOrders}
                      columns={orderColumns}
                      queryKey={["orders"]}
                      tableTitle={"Orders"}/>
    )
};

export default OrdersPage;