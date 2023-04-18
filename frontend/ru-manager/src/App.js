import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Landing from './Pages/landing'
import Home from './Pages/home'

function App() {
  return(
  <Router>
    <Routes>
      <Route exact path='/'     element={<Landing/>}/>
      <Route exact path='/home' element={<Home/>}/>
    </Routes>
  </Router>
  )
}

export default App;
