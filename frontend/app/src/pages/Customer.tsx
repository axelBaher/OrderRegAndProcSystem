// CustomersPage.tsx
import React from "react";
// import {useNavigate} from "react-router-dom";
// import {Button, Modal, Input} from "rsuite";

const CustomerPage: React.FC = () => {
    // const navigate = useNavigate();
    // const [isModalOpen, setIsModalOpen] = useState(false);
    // const [customerIdInput, setCustomerIdInput] = useState("");
    //
    // const handleOpenModal = () => {
    //     setIsModalOpen(true);
    // };
    //
    // const handleCloseModal = () => {
    //     setIsModalOpen(false);
    //     setCustomerIdInput(""); // Очищаем input после закрытия
    // };

    // const handleViewDetails = () => {
    //     if (customerIdInput) {
    //         const customerId = parseInt(customerIdInput, 10);
    //         if (!isNaN(customerId)) {
    //             navigate(`/customers/${customerId}`); // Переходим на страницу деталей
    //             handleCloseModal();
    //         } else {
    //             // Обработка ошибки: некорректный ввод ID
    //             alert("Please enter a valid numeric ID.");
    //
    //
    //         }
    //
    //     }
    // };

    return (
        <div>
            <h1>Customers</h1>

            {/*<Button onClick={handleOpenModal}>View Customer Details</Button>*/}

            {/*<Modal open={isModalOpen} onClose={handleCloseModal}>*/}
            {/*    <Modal.Header>*/}
            {/*        <Modal.Title>Enter Customer ID</Modal.Title>*/}
            {/*    </Modal.Header>*/}
            {/*    <Modal.Body>*/}
            {/*        <Input*/}
            {/*            placeholder="Enter customer ID"*/}
            {/*            value={customerIdInput}*/}
            {/*            onChange={setCustomerIdInput}*/}
            {/*        />*/}
            {/*    </Modal.Body>*/}
            {/*    <Modal.Footer>*/}
            {/*        <Button onClick={handleCloseModal} appearance="subtle">*/}
            {/*            Cancel*/}
            {/*        </Button>*/}
            {/*        /!*<Button onClick={handleViewDetails} appearance="primary">*!/*/}
            {/*        /!*    View Details*!/*/}
            {/*        /!*</Button>*!/*/}
            {/*    </Modal.Footer>*/}
            {/*</Modal>*/}
        </div>
    );
};
export default CustomerPage;