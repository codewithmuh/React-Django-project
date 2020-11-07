import 'bootstrap/dist/css/bootstrap.min.css';


import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter, Switch, Route, Link } from 'react-router-dom';

import Home from './screens/home';
import ListOfThings from './screens/list';

ReactDOM.render((
  <BrowserRouter>
    <div>
      <nav className="container  bg-primary">
        <ul className="nav mt-2 mb-2">
          <li className="nav-item">
            <Link className="nav-link text-white" to="/">Home</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link text-white" to="/list">List</Link>
          </li>
        </ul>
      </nav>
    
      <Switch>
        <Route exact path="/list" component={ ListOfThings } />
        <Route component={ Home } />
      </Switch>
    </div>
  </BrowserRouter>
), document.getElementById('root'));