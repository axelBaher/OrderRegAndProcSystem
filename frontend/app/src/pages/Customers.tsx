import React from "react";
// import axiosInstance from "../api/axiosInstance";
// import {Customer} from "../components/types"
// import GenericTable, {TableColumn} from "../components/GenericTable";


// const fetchCustomers = async (): Promise<Customer[]> => {
//     try {
//         const response = await axiosInstance.get<Customer[]>(
//             "https://127.0.0.1:8000/customers");
//         return response.data;
//     } catch (e) {
//         console.log(e)
//         throw e
//     }
// };

// const customerColumns: TableColumn<Customer>[] = [
//     {title: "ID", dataKey: "id", width: 70, align: "center", fixed: true},
//     {title: "First Name", dataKey: "first_name", width: 200, fixed: true},
//     {title: "Last Name", dataKey: "last_name", width: 200, fixed: true},
//     {title: "Patronymic", dataKey: "patronymic", width: 200, fixed: true},
//     {title: "Nickname", dataKey: "nickname", width: 200, fixed: true},
//     {
//         title: "Sex",
//         dataKey: "sex",
//         width: 100,
//         fixed: true,
//         render: (customer: Customer) => (customer.sex ? "Male" : "Female"),
//     },
//     {
//         title: "Deleted",
//         dataKey: "deleted",
//         width: 100,
//         fixed: true,
//         render: (customer: Customer) => (customer.deleted ? "Deleted" : "Not Deleted"),
//     },
// ];

const CustomersPage: React.FC = () => {
    return (
        <h1>HI</h1>
        // <GenericTable fetchData={fetchCustomers}
        //               columns={customerColumns}
        //               queryKey={["customers"]}
        //               tableTitle={"Customers"}/>
    )
};

export default CustomersPage;