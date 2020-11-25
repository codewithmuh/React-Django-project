import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css'
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';
import { NavLink } from 'react-router-dom';



import Home from './screens/home';
import ListOfThings from './screens/list';
import Layout from './layout';
import TestComp from './components/testcomp';

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
</style>




ReactDOM.render((
  // <BrowserRouter>
  //   <div>
  //     <nav className="container" style={{borderColor: '#f3f3f3'}}>
  //     <h3 className='mt-5 ml-4'>Sample App</h3>

  //       <ul className="nav mt-2 mb-2 ml-4">
  //         <li className="nav-item">
  //           <NavLink className="nav-link" activeClassName='navgalink' exact to="/" >Summary</NavLink>
  //         </li>
  //         <li className="nav-item">
  //           <NavLink className="nav-link"  activeClassName='navgalink' exact to="/list">Orders list</NavLink>
  //         </li>
  //       </ul>
  //     </nav>
    
  //     <Switch>
  //       <Route exact path="/list" component={ ListOfThings } />
  //       <Route component={ Home } />
  //     </Switch>
  //   </div>
  // </BrowserRouter>
  <Layout />
), document.getElementById('root'));