
import React, { useState } from "react";
import api from "../../Services/api";

// Funcionalidades:
//      - Apresentar uma tabela dos usuários que usaram os restaurantes em X tempos
//      - Apresentar os dados de compra de crédito registrados pelos usuários nível 1 (?)

function HomeU2()  {
  // React States
  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const errors = {
    uname: "invalid username",
    pass: "invalid password"
  };

  const handleSubmit = (event) => {
    //Prevent page reload
    event.preventDefault();  
    var { data1, data2 } = document.forms[0];
    console.log(data1, data2 )

    // Find user login info
    api.post("/user2/getfinance", {
        DataInicio: data1.value,
        DataFinal: data2.value
    })
    .then(
      response => console.log(response)
    )
    .catch(
      error => console.log(error)
    )
    console.log("--------------")

  };

  // Generate JSX code for error message
  const renderErrorMessage = (name) =>
  name === errorMessages.name && (
    <div className="error">{errorMessages.message}</div>
  );
  // JSX code for login form
  const renderForm = (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <div className="input-container">
          <label>Usuário </label>
          <input type="text" name="uname" required />
          {renderErrorMessage("uname")}
        </div>
        <div className="input-container">
          <label>Senha </label>
          <input type="password" pattern="[0-9]*" inputmode="numeric" name="pass" required />
          {renderErrorMessage("pass")}
        </div>
        <div className="button-container">
          <input type="submit" />
        </div>
      </form>
    </div>
  );

  return (
    <div className="app">
      <div className="login-form">
        <div className="title">Entrar</div>
        {isSubmitted ? <div>User is successfully logged in</div> : renderForm}
      </div>
    </div>
  );
}

export default HomeU2


