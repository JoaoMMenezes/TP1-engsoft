import React from "react";
import "./home_u0.css"
import {HiCurrencyDollar, HiUserCircle} from 'react-icons/hi'
import axios from "axios";

// Funcionalidades: 
//      - Ver saldo
//      - Ver cardápio

function HomeU0() {
    // Get Saldo
    var saldo = "0,00"
    axios.post("/user0/getbalance").then(
        (response) => saldo = response.saldo    // CONFIRMAR
    ).catch(
        (error) => console.log(error)
    )

    // Cardápio estático
    const cardapio = ["Arroz", "Feijão", "Tiras de Frango"]

    return(
        <div className="app">
            <div className="homeu0">
                <h2><HiUserCircle className="icon"/>Nome User </h2>
                <h2><HiCurrencyDollar className="icon"/> {saldo} </h2>
                <ul aria-label="Cardápio:">
                    { cardapio.map ((item) => <li> {item} </li>)}
                </ul>
            </div>
        </div>
    )
}

export default HomeU0