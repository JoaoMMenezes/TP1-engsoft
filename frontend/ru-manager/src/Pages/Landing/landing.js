import React, { useState } from "react";
import api from "../../Services/api";
import './landing.css'

import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import { useNavigate } from "react-router-dom";

function Landing() {
  const [user, setUser] = useState(null)
  const [password, setPassorwd] = useState(null)
  const navigate = useNavigate()

  const handleLogin = (e) => {
    //Prevent page reload
    e.preventDefault();  

    console.log('user', user)
    console.log('password', password)
    
    // Tenta logar no backend
    api.post("/login", {
      Matricula: user,
      Senha: password
    })
    .then(  
      response => {
        console.log(response.data.sucesso)
        if (response.data.sucesso) {
          localStorage.setItem('userName', response.data.name)
          localStorage.setItem('userId', response.data.matricula)
          if (response.data.tipo === 2) {                   //Confirmar se é int ou string
            navigate('/home-u2')
          } else if (response.data.tipo === 1){             //Confirmar se é int ou string
            navigate('/home-u1')
          } else {
            navigate('/home-u0')
          } 
        }
        else {
          alert('Erro em efetuar login!')
        }
      }
    )
    .catch(
      error => console.log(error)
    )
  };



  return (
    <div className="app">
      <div className="login-form">
        <h1 className="title">Entrar</h1>
        <Form className="mt-1" onSubmit={handleLogin}>
           <InputGroup className="mb-3">
            <InputGroup.Text className="w-25" id="basic-addon1">Usuário:</InputGroup.Text>
            <Form.Control
                onChange={(e) => setUser(e.target.value)}
                aria-label="Matrícula"
                aria-describedby="basic-addon2"
            />
          </InputGroup>
          <InputGroup className="mb-3">
            <InputGroup.Text className="w-25">Senha:</InputGroup.Text>
            <Form.Control 
                onChange={(e) => setPassorwd(e.target.value)}
                type="password"
                aria-label="Senha" 
            />
          </InputGroup>
          <div className="d-grid gap-2">
              <Button 
                // onClick={() => {
                //   localStorage.setItem('userId', user)
                //   navigate('/home-u0')
                //   }}
                type="submit"
                variant="outline-primary" 
                >Login</Button>{''}
          </div>
        </Form>
      </div>
    </div>
  );
}

export default Landing