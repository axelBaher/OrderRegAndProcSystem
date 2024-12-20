// Login.tsx
import React, {useContext, useState} from "react";
import {Form, Button} from "rsuite";
import axiosInstance from "../api/axiosInstance";
import {Notify} from "../utils/Notify";
import {AuthContext} from "../components/AuthContext";
import {useNavigate} from 'react-router-dom';

const LoginForm = () => {
    const authContext = useContext(AuthContext);
    const navigate = useNavigate();
    if (!authContext) {
        throw new Error("AuthContext is not provided");
    }
    const {handleLogin} = authContext;
    const [formValue, setFormValue] = useState({
        login: "",
        password: "",
    });

    const handleSubmit = async () => {
        try {
            const response = await axiosInstance.post(`https://127.0.0.1:8000/login`, {
                login: formValue.login,
                password: formValue.password,
            });
            // console.log("isAuth-LoginForm-BeforeSubmit: " + authContext?.isAuthenticated);
            handleLogin(response.data);
            Notify.Success("Login successfully!");
            // console.log("isAuth-LoginForm-AfterSubmit: " + authContext?.isAuthenticated);
            navigate("/customer");
        } catch (error) {
            Notify.Success("Login failed!");
        }
    };

    return (
        <Form fluid>
            <Form.Group>
                <Form.ControlLabel>Login</Form.ControlLabel>
                <Form.Control
                    name="login"
                    value={formValue.login}
                    onChange={(value) => setFormValue({...formValue, login: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Password</Form.ControlLabel>
                <Form.Control
                    name="password"
                    type="password"
                    value={formValue.password}
                    onChange={(value) => setFormValue({...formValue, password: value})}
                />
            </Form.Group>
            <Form.Group>
                <Button appearance="primary" onClick={handleSubmit}>
                    Login
                </Button>
            </Form.Group>
        </Form>
    );

};

export default LoginForm;