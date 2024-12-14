// Main.tsx
import {Routes, Route} from "react-router-dom";
import CustomerDetails from "./pages/CustomerDetails";
import LoginForm from "./pages/Login";
import RegisterForm from "./pages/Registration";
import CustomersPage from "./pages/Customers";
import OrdersPage from "./pages/Orders";

const Main = () => {
    return (
        <Routes>
            <Route path="/customers" element={<CustomersPage/>}/>
            <Route path="/orders" element={<OrdersPage/>}/>
            <Route path="/customer" element={<CustomerDetails/>}/>
            <Route path="/login" element={<LoginForm/>}/>
            <Route path="/register" element={<RegisterForm/>}/>
        </Routes>
    );
}
export default Main;