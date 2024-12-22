import React, {useContext, useState} from "react";
import {Form, Button, SelectPicker} from "rsuite";
import axiosInstance from "../api/axiosInstance";
import {Notify} from "../utils/Notify";
import {AuthContext} from "../components/AuthContext";
import {useNavigate} from "react-router-dom";

const RegisterForm = () => {
    const authContext = useContext(AuthContext);
    if (!authContext) {
        throw new Error("AuthContext is not provided");
    }
    const {handleLogin} = authContext;
    const navigate = useNavigate();
    const [formValue, setFormValue] = useState({
        login: "",
        password: "",
        first_name: "",
        last_name: "",
        patronymic: "",
        nickname: "",
        sex: "",
    });

    const handleSubmit = async () => {
        try {
            const response = await axiosInstance.post("https://127.0.0.1:8000/register", {
                customer_data: {
                    login: formValue.login,
                    password: formValue.password,
                    first_name: formValue.first_name,
                    last_name: formValue.last_name,
                    patronymic: formValue.patronymic,
                    nickname: formValue.nickname,
                    sex: formValue.sex,
                },
            });
            handleLogin(response.data);
            navigate("/customer")
            Notify.Success("Successful registration");
        } catch (error) {
            Notify.Error("Registration failed");
        }
    };

    const selectData = [
        {
            label: "Male",
            value: 1
        },
        {
            label: "Female",
            value: 0
        }
    ]

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
            <Form.ControlLabel>Пол</Form.ControlLabel>
            {/*<Form.Control*/}
            {/*    as={"select"}*/}
            {/*    name="sex"*/}
            {/*    value={formValue.sex}*/}
            {/*    onChange={(e) => setFormValue({...formValue, sex: e.target.value})}*/}
            {/*>*/}
            {/*    <option value="Male">Male</option>*/}
            {/*    <option value="Female">Female</option>*/}
            {/*</Form.Control>*/}
            <Form.Group controlId="selectPicker">
                <Form.Control name="selectPicker" accepter={SelectPicker} data={selectData}
                              onChange={(value) => setFormValue({...formValue, sex: value})}/>
            </Form.Group>
            {/*<select*/}
            {/*    name="sex"*/}
            {/*    value={formValue.sex}*/}
            {/*    onChange={(e) => setFormValue({...formValue, sex: e.target.value})}*/}
            {/*>*/}
            {/*    <option value="Male">Male</option>*/}
            {/*    <option value="Female">Female</option>*/}
            {/*</select>*/}
            <Form.Group>
                <Button appearance="primary" onClick={handleSubmit}>
                    Register
                </Button>
            </Form.Group>
        </Form>
    );
};

export default RegisterForm;