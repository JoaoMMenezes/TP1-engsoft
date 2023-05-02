import React from "react";
import Nav from 'react-bootstrap/Nav';
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";
import './LogoutNav.css'

function LogoutNav() {
    const navigate = useNavigate()
    const logout = () => {
        localStorage.clear()
        navigate('/')
    }

    return (
      <Nav className="logoutNav mt-2">
        <Nav.Item>
            <Button className="logoutButton" onClick={logout} variant="outline-danger">Logout</Button>{' '}
        </Nav.Item>
        <Nav.Item>
            <div className="blob"></div>
        </Nav.Item>
      </Nav>
    );
}

export default LogoutNav