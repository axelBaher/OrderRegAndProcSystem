import {Button, ButtonToolbar, Modal, Form} from "rsuite";
import React, {useState} from "react";
import axiosInstance from "../../api/axiosInstance";
import {Notify} from "../../utils/Notify";

export function AddressAddModal(props: {
    parentID: any, refetch: (props?: any) => any, show: any, onCancel: any, onSubmit: any
}) {
    const [formValue, setFormValue] = useState({
        address: ""
    });

    const handleSubmit = async () => {
        try {
            await axiosInstance.post(`https://127.0.0.1:8000/customers/${props.parentID}/addresses`, {
                address: formValue.address
            });
            await props.refetch();
            props.onSubmit();
            Notify.Success("New address is added");
        } catch (error) {
            Notify.Error("Error while adding new address, try again");
        }
    };

    return (
        <Modal open={props.show}>
            <Modal.Header>
                <Modal.Title>Add new address</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form fluid>
                    <Form.Group>
                        <Form.ControlLabel>Address</Form.ControlLabel>
                        <Form.Control
                            name="address"
                            value={formValue.address}
                            onChange={(value) => setFormValue({...formValue, address: value})}
                        />
                    </Form.Group>
                </Form>
            </Modal.Body>
            <Modal.Footer>
                <ButtonToolbar>
                    <Button onClick={props.onCancel} appearance="subtle">
                        Cancel
                    </Button>
                    <Button onClick={handleSubmit} appearance="primary">
                        Add
                    </Button>
                </ButtonToolbar>
            </Modal.Footer>
        </Modal>
    )
}

