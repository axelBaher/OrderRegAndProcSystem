// LogoutConfirmModal
import React, {useContext} from "react";
import {Modal, Button, ButtonToolbar} from "rsuite";
import {useNavigate} from "react-router-dom";
import {AuthContext} from "./AuthContext";

interface LogoutConfirmModalProps {
    show: boolean,
    onConfirm: () => void,
    onCancel: () => void;
}

const LogoutConfirmModal: React.FC<LogoutConfirmModalProps> = ({ show, onCancel }) => {
  const authContext = useContext(AuthContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    authContext?.handleLogout();
    onCancel();
    navigate("/login");
  };

  return (
    <Modal open={show} onClose={onCancel}>
      <Modal.Header>
        <Modal.Title>Confirm Logout</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        Are you sure you want to logout?
      </Modal.Body>
      <Modal.Footer>
        <ButtonToolbar>
          <Button onClick={onCancel} appearance="subtle">
            Cancel
          </Button>
          <Button onClick={handleLogout} appearance="primary">
            Logout
          </Button>
        </ButtonToolbar>
      </Modal.Footer>
    </Modal>
  );
};

export default LogoutConfirmModal;