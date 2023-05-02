import React, { useContext, useState } from "react";
import api from "../../Services/api";

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import InputGroup from 'react-bootstrap/InputGroup';
import LogoutNav from "../../Components/LogoutNav";

// Funcionalidades:
//      - Apresentar uma tabela dos usuários que usaram os restaurantes em X tempos

function HomeU2()  {
  const [data1, setData1] = useState("00-00-0000")
  const [data2, setData2] = useState("00-00-0000")

  const handleGetFinance = (e) => {
    e.preventDefault();
    console.log("data1:", data1)
    console.log("data2:", data2)
    api.post('/user2/getfinance', {
      DataInicio: data1,
      DataFinal: data2
    })
    .then(
      res => console.log(res)
    )
    .catch(
      error => {
        console.log(error)
        alert("Datas inseridas estão inválidas")
      }
    )
  }

  return(
    <>
      <LogoutNav/>
      <div className="app">
        <div className="box mt-2">
          <h1 className="mt-4 mb-5">Administrador Fump</h1>
          <text>Pesquisar fluxo de clientes nos restaurantes informando duas datas distintas:</text>
          <Form onSubmit={handleGetFinance} className="form mt-2">
              <InputGroup className="dates mb-2">
                <InputGroup.Text className="w-25" id="basic-addon1">Início:</InputGroup.Text>
                <Form.Control
                  onChange={(e) => setData1(e.target.value)}
                  placeholder="dd-mm-aaaa"
                  aria-label="Matrícula"
                  aria-describedby="basic-addon2"
                />
              </InputGroup>

              <InputGroup className="dates mb-2">
                <InputGroup.Text className="w-25" id="basic-addon1">Fim:</InputGroup.Text>
                <Form.Control
                  onChange={(e) => setData2(e.target.value)}
                  placeholder="dd-mm-aaaa"
                  aria-label="Matrícula"
                  aria-describedby="basic-addon2"
                />
              </InputGroup>

              <div className="d-grid gap-2">
                <Button type="submit" variant="outline-primary">Pesquisar</Button>{''}
              </div>
          </Form>
        </div>
      </div>
    </>
  )
}

export default HomeU2