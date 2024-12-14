// ProtectedPage.tsx
import React from "react";
import axiosInstance from "../api/axiosInstance";

const ProtectedPage = () => {
    const token = localStorage.getItem("token");

    if (!token) {
        return <div>You are not authorized!</div>;
    }

    axiosInstance.defaults.headers.common["Authorization"] = `Bearer ${token}`;

    const fetchData = async () => {
        try {
            const response = await axiosInstance.get("https://127.0.0.1:8000/protected");
            return response.data;
        } catch (error) {
            return null;
        }
    };

    return (
        <div>
            <>
                <h1>Protected page</h1>
                {fetchData().then((data) => (
                    <div>{data.message}</div>
                ))}
            </>
        </div>
    );
};

export default ProtectedPage;