import {Routes, Route} from "react-router-dom";
import CustomersPage from "./pages/Customers";
import OrdersPage from "./pages/Orders";
import CustomerDetails from "./pages/CustomerDetails";

const Main = () => {
    return (
        <Routes>
            <Route path="/customers" element={<CustomersPage/>}/>
            <Route path="/orders" element={<OrdersPage/>}/>
            <Route path="/customer" element={<CustomerDetails/>}/>
        </Routes>
    );
}
export default Main;