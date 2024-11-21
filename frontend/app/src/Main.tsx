import {Routes, Route} from "react-router-dom";
import CustomersPage from "./pages/Customers";
import OrdersPage from "./pages/Orders";

const Main = () => {
    return (
        <Routes>
            <Route path="/customers" element={<CustomersPage/>}/>
            <Route path="/orders" element={<OrdersPage/>}/>
        </Routes>
    );
}
export default Main;