// AuthContext.tsx
import React, {createContext, useState} from "react";
import {Notify} from "../utils/Notify";

interface AuthContextProps {
    children: React.ReactNode;
}

interface AuthContextValue {
    // isAuthenticated: boolean;
    token: string | null;
    handleLogin: (token: string) => void;
    handleLogout: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

const AuthProvider = ({children}: AuthContextProps) => {
    // const [isAuthenticated, setIsAuthenticated] = useState(false);
    const [token, setToken] = useState(localStorage.getItem("token"));

    const handleLogin = (token: string) => {
        setToken(token);
        localStorage.setItem("token", token);
    };

    const handleLogout = () => {
        setToken(null);
        localStorage.removeItem("token");
        Notify.Success("Logout successfully!");
    };

    return (
        // <AuthContext.Provider value={{isAuthenticated, token, handleLogin, handleLogout}}>
        <AuthContext.Provider value={{token, handleLogin, handleLogout}}>
            {children}
        </AuthContext.Provider>
    );

};

export {AuthProvider, AuthContext};