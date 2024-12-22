// Navigation.tsx
import {Nav, Navbar} from "rsuite";
import React, {useState} from "react";
import {To, useNavigate} from "react-router-dom";
// import {useLocation} from "react-router-dom";
// import {AuthContext} from "./AuthContext";
import LogoutConfirmModal from "./LogoutConfirmModal";
import {getDecodedAccessToken} from "../pages/CustomerDetails";

const Navigation = () => {
    // const authContext = React.useContext(AuthContext);
    const [showLogoutModal, setShowLogoutModal] = useState(false);
    // const location = useLocation();
    const useCustomNav = () => {
        const navigate = useNavigate();
        if (!getDecodedAccessToken(localStorage.getItem("token"))) return () => navigate("/login", {state: {isAuth: "False"}});
        return (to: To) => navigate(to, {state: {isAuth: "True"}});
    };
    // console.log("Location-state-isAuth: " + JSON.stringify(location.state.isAuth));
    const navigator = useCustomNav();

    const handleOpenLogoutModal = () => {
        setShowLogoutModal(true)
    };

    const handleCloseLogoutModal = () => {
        setShowLogoutModal(false)
    };

    const authNavItems = () => {
        // console.log("isAuth-inApp-authNavItems: " + authContext?.isAuthenticated);
        return (
            <>
                {/*<Nav.Item*/}
                {/*    onClick={() => {*/}
                {/*        navigator("/customers");*/}
                {/*    }}>*/}
                {/*    All customers</Nav.Item>*/}

                {localStorage.getItem("token") ? (
                    <>
                        <Nav.Item onClick={() => {
                            navigator("/customer")
                        }}>Customer Info</Nav.Item>
                        <Nav.Item onClick={handleOpenLogoutModal}>Logout</Nav.Item>
                    </>
                ) : (
                    <>
                        <Nav.Item onClick={() => navigator("/login")}>Login</Nav.Item>
                        <Nav.Item onClick={() => navigator("/register")}>Register</Nav.Item>
                    </>
                )}
            </>
        );
    };

    return (
        <Navbar>
            <Nav>
                <LogoutConfirmModal
                    show={showLogoutModal}
                    onCancel={handleCloseLogoutModal}
                    onConfirm={handleCloseLogoutModal}/>
                <>{authNavItems()}</>
            </Nav>
        </Navbar>
    );
}
export default Navigation;