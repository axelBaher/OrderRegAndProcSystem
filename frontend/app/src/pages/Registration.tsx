import React, {useContext, useState} from "react";
import {Form, Button} from "rsuite";
import axiosInstance from "../api/axiosInstance";
import {Notify} from "../utils/Notify";
import {AuthContext} from "../components/AuthContext";

const RegisterForm = () => {
    const authContext = useContext(AuthContext);
    if (!authContext) {
        throw new Error("AuthContext is not provided");
    }
    const {handleLogin} = authContext;
    const [formValue, setFormValue] = useState({
        login: "",
        password: "",
        first_name: "",
        last_name: "",
        patronymic: "",
        nickname: "",
        sex: true,
    });

    const handleSubmit = async () => {
        try {
            const response = await axiosInstance.post("https://127.0.0.1:8000/register", {
                login: formValue.login,
                password: formValue.password,
                customer_data: {
                    first_name: formValue.first_name,
                    last_name: formValue.last_name,
                    patronymic: formValue.patronymic,
                    nickname: formValue.nickname,
                    sex: formValue.sex,
                },
            });
            handleLogin(response.data);
            Notify.Success("Successful registration");
        } catch (error) {
            Notify.Error("Registration failed");
        }
    };

    return (
        <Form fluid>
            <Form.Group>
                <Form.ControlLabel>Логин</Form.ControlLabel>
                <Form.Control
                    name="login"
                    value={formValue.login}
                    onChange={(value) => setFormValue({...formValue, login: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Пароль</Form.ControlLabel>
                <Form.Control
                    name="password"
                    type="password"
                    value={formValue.password}
                    onChange={(value) => setFormValue({...formValue, password: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Имя</Form.ControlLabel>
                <Form.Control
                    name="first_name"
                    value={formValue.first_name}
                    onChange={(value) => setFormValue({...formValue, first_name: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Фамилия</Form.ControlLabel>
                <Form.Control
                    name="last_name"
                    value={formValue.last_name}
                    onChange={(value) => setFormValue({...formValue, last_name: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Отчество</Form.ControlLabel>
                <Form.Control
                    name="patronymic"
                    value={formValue.patronymic}
                    onChange={(value) => setFormValue({...formValue, patronymic: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Никнейм</Form.ControlLabel>
                <Form.Control
                    name="nickname"
                    value={formValue.nickname}
                    onChange={(value) => setFormValue({...formValue, nickname: value})}
                />
            </Form.Group>
            <Form.Group>
                <Form.ControlLabel>Пол</Form.ControlLabel>
                <Form.Control
                    name="sex"
                    checked={formValue.sex}
                    onChange={(value) => setFormValue({...formValue, sex: value})}
                    type="checkbox"
                />
            </Form.Group>
            <Form.Group>
                <Button appearance="primary" onClick={handleSubmit}>
                    Register
                </Button>
            </Form.Group>
        </Form>
    );
};

export default RegisterForm;