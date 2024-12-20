import {Button, ButtonToolbar, Modal, Form} from "rsuite";
import React, {useState} from "react";
import axiosInstance from "../../api/axiosInstance";
import {Notify} from "../../utils/Notify";

export function ContactAddModal(props: {
    parentID: any, refetch: (props?: any) => any, show: any, onCancel: any, onSubmit: any
}) {
    const [formValue, setFormValue] = useState({
        contact: ""
    });

    const handleSubmit = async () => {
        try {
            await axiosInstance.post(`https://127.0.0.1:8000/customers/${props.parentID}/contacts`, {
                contact: formValue.contact
            });
            await props.refetch();
            props.onSubmit();
            Notify.Success("New contact is added");
        } catch (error) {
            Notify.Error("Error while adding new contact, try again");
        }
    };

    return (
        <Modal open={props.show}>
            <Modal.Header>
                <Modal.Title>Add new contact</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form fluid>
                    <Form.Group>
                        <Form.ControlLabel>Contact</Form.ControlLabel>
                        <Form.Control
                            name="contact"
                            value={formValue.contact}
                            onChange={(value) => setFormValue({...formValue, contact: value})}
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

