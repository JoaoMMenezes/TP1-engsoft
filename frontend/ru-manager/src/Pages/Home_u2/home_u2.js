import React, { useState } from "react";
import api from "../../Services/api";
import './home_u2.css'

function HomeU2() {
  // React States
  const [errorMessages, setErrorMessages] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const errors = {
    data1: "invalid data1",
    data2: "invalid data2"
  };

  const handleSubmit = (event) => {
    //Prevent page reload
    event.preventDefault();  
    var { data1, data2 } = document.forms[0];
    console.log(data1,data2)
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
          <label>UsuÃ¡rio </label>
          <input type="text" name="data1" required />
          {renderErrorMessage("data1")}
        </div>
        <div className="input-container">
          <label>Senha </label>
          <input type="data2" name="data2" required />
          {renderErrorMessage("data2")}
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