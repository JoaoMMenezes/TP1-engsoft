import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Landing from './Pages/Landing/landing'
import HomeU0 from './Pages/Home_u0/home_u0'
import HomeU1 from './Pages//Home_u1/home_u1'
import HomeU2 from './Pages/Home_u2/home_u2'
import { UserProvider } from './Services/UserContext';

import Nav from 'react-bootstrap/Nav';

function TabsExample() {
  return (
    <Nav variant="tabs">
      <Nav.Item>
        <Nav.Link href="/">login</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link href="/home-u0">home_u0</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link href="/home-u1">home_u1</Nav.Link>
      </Nav.Item>
      <Nav.Item>
        <Nav.Link href="/home-u2">home_u2</Nav.Link>
      </Nav.Item>
    </Nav>
  );
}


function App() {
  return(
    <Router>
      <TabsExample/>
      <UserProvider>
          <Routes>
              <Route exact path='/'     element={<Landing/>}/>
              <Route exact path='/home-u0' element={<HomeU0/>}/>
              <Route exact path='/home-u1' element={<HomeU1/>}/>
              <Route exact path='/home-u2' element={<HomeU2/>}/>
          </Routes>
      </UserProvider>
    </Router>
  )
}

export default App;
