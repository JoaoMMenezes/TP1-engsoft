import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css'

import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Accordion from 'react-bootstrap/Accordion';

// Funcionalidades:
//      - Acrescentar crédito a um usuário de nível 0
//      - Redirect to > Cadastrar um usuário de nível 0

const teste = (e) => {
    e.preventDefault();
    console.log('foi')
}


function HomeU1() {
    return(
        <div className="app">
            <div className="box mt-2">
                <h1 className="mt-4" >Administrador 1</h1>
                <Accordion className="w-75 mt-4 mb-4">
                    <Accordion.Item eventKey="0">
                        <Accordion.Header className="w-100" ><b>Adicionar Crédito:</b></Accordion.Header>
                        <Accordion.Body>
                            <Form className="mt-1" onSubmit={teste}>
                                <Form.Label>Adicionar crédito a um usuário:</Form.Label>
                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Matrícula:</InputGroup.Text>
                                    <Form.Control
                                        aria-label="Matrícula"
                                        aria-describedby="basic-addon2"
                                    />
                                </InputGroup>

                                <InputGroup className="mb-3">
                                    <InputGroup.Text>Fichas</InputGroup.Text>
                                    <Form.Control 
                                        maxlength="0"
                                        type="number"
                                        aria-label="Valor em reais" 
                                        placeholder="Ex: 18"
                                    />
                                </InputGroup>
                                <div className="d-grid gap-2">
                                    <Button type="submit" variant="outline-primary">Adicionar</Button>{''}
                                </div>
                            </Form>
                        </Accordion.Body>
                    </Accordion.Item>
                    <Accordion.Item eventKey="1">
                        <Accordion.Header className="w-100" ><b>Cadastrar Novo Usuário</b></Accordion.Header>
                        <Accordion.Body>
                            <Form className="mt-1" onSubmit={teste}>
                                <Form.Label>Dados do novo usuário:</Form.Label>
                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Matrícula:</InputGroup.Text>
                                    <Form.Control
                                        type="number"
                                        aria-label="Matrícula"
                                        aria-describedby="basic-addon2"
                                    />
                                </InputGroup>

                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Senha:</InputGroup.Text>
                                    <Form.Control
                                        type="number"
                                        placeholder="Apenas números (ex:123456)"
                                        aria-label="Senha"
                                        aria-describedby="basic-addon2"
                                    />
                                </InputGroup>

                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Nome:</InputGroup.Text>
                                    <Form.Control
                                        aria-label="Nome"
                                        aria-describedby="basic-addon2"
                                    />
                                </InputGroup>

                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Nível Fump:</InputGroup.Text>
                                    <Form.Select aria-label="Default select example">
                                        <option value={5.60}>Não assistido</option>
                                        <option value={0}>1</option>
                                        <option value={1}>2</option>
                                        <option value={1}>3</option>
                                        <option value={2}>4-A</option>
                                        <option value={2.90}>4-B</option>
                                    </Form.Select>
                                </InputGroup>

                                <InputGroup className="mb-3">
                                    <InputGroup.Text id="basic-addon1">Email:</InputGroup.Text>
                                    <Form.Control
                                        type="email"
                                        placeholder="exemplo@ufmg.br"
                                        aria-label="Nome"
                                        aria-describedby="basic-addon2"
                                    />
                                </InputGroup>

                                <div className="d-grid gap-2">
                                    <Button type="submit" variant="outline-primary">Cadastrar</Button>{''}
                                </div>
                            </Form>
                        </Accordion.Body>
                    </Accordion.Item>
                </Accordion>
                
            </div>
        </div>
    )
}

export default HomeU1