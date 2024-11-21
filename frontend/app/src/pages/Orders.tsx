import React from "react";
// import axiosInstance from "../api/axiosInstance";
// import {Order} from "../components/types"
// import GenericTable, {TableColumn} from "../components/GenericTable";


// const fetchOrders = async (): Promise<Order[]> => {
//     try {
//         const response = await axiosInstance.get<Order[]>(
//             "https://127.0.0.1:8000/customers/3/orders");
//         return response.data;
//     } catch (e) {
//         console.log(e)
//         throw e
//     }
// };
//
// const orderColumns: TableColumn<Order>[] = [
//     {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true},
//     {title: "Customer ID", dataKey: "customer_id", width: 100, fixed: true},
//     {title: "Total", dataKey: "total", width: 120, fixed: true},
//     {title: "Code", dataKey: "code", width: 70, fixed: true},
//     {
//         title: "Deleted",
//         dataKey: "deleted",
//         width: 100,
//         fixed: true,
//         render: (order: Order) => (order.deleted ? "Deleted" : "Not Deleted"),
//     },
// ];

const OrdersPage: React.FC = () => {
    return (
        <h1>ORDERS</h1>
        // <GenericTable fetchData={fetchOrders}
        //               columns={orderColumns}
        //               queryKey={["orders"]}
        //               tableTitle={"Orders"}/>
    )
};

export default OrdersPage;