import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Landing from './Pages/Landing/landing'
import HomeU0 from './Pages/Home_u0/home_u0'
import HomeU1 from './Pages//Home_u1/home_u1'
import HomeU2 from './Pages/Home_u2/home_u2'
import CadastroU0 from './Pages/Cadastro_u0/cadastro_u0'
import CadastroU1 from './Pages/Cadastro_u1/Cadastro_u1'

function App() {
  return(
  <Router>
    <Routes>
      <Route exact path='/'     element={<Landing/>}/>
      <Route exact path='/home-u0' element={<HomeU0/>}/>
      <Route exact path='/home-u1' element={<HomeU1/>}/>
      <Route exact path='/home-u2' element={<HomeU2/>}/>
      <Route exact path='/cadastro-u0' element={<CadastroU0/>}/>
      <Route exact path='/cadastro-u1' element={<CadastroU1/>}/>
    </Routes>
  </Router>
  )
}

export default App;
