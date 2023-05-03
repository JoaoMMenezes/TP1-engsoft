import React, { useState } from "react";
import 'bootstrap/dist/css/bootstrap.min.css'

import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import Button from 'react-bootstrap/Button';
import Accordion from 'react-bootstrap/Accordion';
import api from "../../Services/api";
import LogoutNav from "../../Components/LogoutNav";

// Funcionalidades:
//      - Acrescentar crédito a um usuário de nível 0
//      - Redirect to > Cadastrar um usuário de nível 0

const teste = (e) => {
    e.preventDefault();
    console.log('foi')
}


function HomeU1() {
    // States de adicionar fichas
    const [matricula, setMatricula] = useState('')
    const [fichas, setFichas] = useState(0)

    // States de cadastro
    const [novaMatricula, setNovaMatricula] = useState()
    const [senha, setSenha] = useState()
    const [nome, setNome] = useState()
    const [valorFicha, setValorFicha] = useState()
    const [email, setEmail] = useState()

    // States de retirar fichas
    const [retirar, setRetirar] = useState('')

    const confirmar = () => {
        console.log('matricula', matricula)
        console.log('fichas', fichas)
        console.log('novaMatricula', novaMatricula)
        console.log('senha', senha)
        console.log('nome', nome)
        console.log('valorFicha', valorFicha)
        console.log('email', email )
    }

    const handleAdicionarCredito = (e) => {
        e.preventDefault();
        api.post('/user1/deposittoken', {
            Matricula: matricula,
            Amount: fichas
        })
        .then(
            res => {
                if (res.data.mensagem) {
                    alert('Compra realizada com sucesso!')
                } else {
                    alert('Erro ao realizar compra!')
                }
            }
        )
        .catch(
            error => {
                console.log(error)
                alert('Erro ao realizar compra!')
            }
        )
    }

    const handleRetirarCredito = (e) => {
        e.preventDefault();
        console.log(retirar)
        api.post('/user0/havelunch', {
            Matricula: retirar
        })
        .then(
            res => {
                if (res.data.mensagem) {
                    alert('Compra realizada com sucesso!')
                } else {
                    alert('Erro ao realizar compra!')
                }
            }
        )
        .catch(
            error => {
                console.log(error)
                alert('Erro ao realizar compra!')
            }
        )
    }

    const handleCadastro = (e) => {
        e.preventDefault();
        api.post('/user1/signin', {
            Matricula: novaMatricula,
            Senha: senha,
            Nome: nome,
            ValorFicha: valorFicha,
            Email: email
        })
        .then(
            res => {
                if (res.data.mensagem) {
                    alert('Cadastro realizado com sucesso!')
                } else {
                    alert('Erro ao realizar cadastro!')
                }
            }
        )
        .catch(
            error => {
                console.log(error)
                alert('Erro ao realizar cadastro!')
            }
        )
    }

    return(
        <>
            <LogoutNav/>
            <div className="app">
                <div className="box mt-2 mb-4">
                    <h1 className="mt-4" >Administrador 1</h1>
                    <Accordion className="w-75 mt-4 mb-4">
                        <Accordion.Item eventKey="0">
                            <Accordion.Header className="w-100" ><b>Adicionar Crédito:</b></Accordion.Header>
                            <Accordion.Body>
                                <Form className="mt-1" onSubmit={handleAdicionarCredito}>
                                    <Form.Label>Adicionar crédito a um usuário:</Form.Label>
                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Matrícula:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setMatricula(e.target.value)}
                                            aria-label="Matrícula"
                                            aria-describedby="basic-addon2"
                                            placeholder="Ex: 123456789"
                                        />
                                    </InputGroup>

                                    <InputGroup className="mb-3">
                                        <InputGroup.Text>Fichas</InputGroup.Text>
                                        <Form.Control 
                                            onChange={(e) => setFichas(e.target.value)}
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
                                <Form className="mt-1" onSubmit={handleCadastro}>
                                    <Form.Label>Dados do novo usuário:</Form.Label>
                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Matrícula:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setNovaMatricula(e.target.value)}
                                            type="number"
                                            aria-label="Matrícula"
                                            aria-describedby="basic-addon2"
                                            placeholder="Ex: 2024207272"
                                        />
                                    </InputGroup>

                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Senha:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setSenha(e.target.value)}
                                            type="number"
                                            placeholder="Apenas números (ex:123456)"
                                            aria-label="Senha"
                                            aria-describedby="basic-addon2"
                                        />
                                    </InputGroup>

                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Nome:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setNome(e.target.value)}
                                            aria-label="Nome"
                                            aria-describedby="basic-addon2"
                                            placeholder="Ex: Lucas Martins Palhares"
                                        />
                                    </InputGroup>

                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Valor pago por ficha:</InputGroup.Text>
                                        {/* <Form.Select onChange={(choice) => setValorFicha(choice.value)} aria-label="Default select example">
                                            <option value={5.60}>Não assistido</option>
                                            <option value={0}>1</option>
                                            <option value={1}>2</option>
                                            <option value={1}>3</option>
                                            <option value={2}>4-A</option>
                                            <option value={2.90}>4-B</option>
                                        </Form.Select> */}
                                        <Form.Control
                                            onChange={(e) => setValorFicha(e.target.value)}
                                            aria-label="Nome"
                                            aria-describedby="basic-addon2"
                                            placeholder="5.60 / 2.90 / 2 / 1 / 0"
                                        />
                                    </InputGroup>

                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Email:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setEmail(e.target.value)}
                                            type="email"
                                            placeholder="exemplo@ufmg.br"
                                            aria-label="Nome"
                                            aria-describedby="basic-addon2"
                                        />
                                    </InputGroup>

                                    <div className="d-grid gap-2">
                                        <Button onClick={confirmar} type="submit" variant="outline-primary">Cadastrar</Button>{''}
                                    </div>
                                </Form>
                            </Accordion.Body>
                        </Accordion.Item>
                        <Accordion.Item eventKey="2">
                            <Accordion.Header className="w-100" ><b>Cobrar almoço manualmente</b></Accordion.Header>
                            <Accordion.Body>
                                <Form className="mt-1" onSubmit={handleRetirarCredito}>
                                    <Form.Label>Retirar crédito do usuário:</Form.Label>
                                    <InputGroup className="mb-3">
                                        <InputGroup.Text id="basic-addon1">Matrícula:</InputGroup.Text>
                                        <Form.Control
                                            onChange={(e) => setRetirar(e.target.value)}
                                            aria-label="Matrícula"
                                            aria-describedby="basic-addon2"
                                            placeholder="Ex: 123456789"
                                        />
                                    </InputGroup>
                                    <div className="d-grid gap-2">
                                        <Button type="submit" variant="outline-primary">Retirar</Button>{''}
                                    </div>
                                </Form>
                            </Accordion.Body>
                        </Accordion.Item>
                    </Accordion>
                    
                </div>
            </div>
        </>
    )
}

export default HomeU1