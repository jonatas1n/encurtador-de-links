import React from 'react'
import './App.css';

import {
  BrowserRouter as Router,
  Redirect,
  Route,
  Switch
} from 'react-router-dom'

import Home from './components/Home/index'
import GoTo from './components/GoTo/index'
import NotFound from './components/NotFound/index'
import ShowLink from './components/ShowLink/index'

function App() {
  return (

    <Router>
      <Switch>
        <Route exact path={'/'} component={Home}/>
        <Route exact path={'/show/:link'} component={ShowLink}/>
        <Route path={'/not-found'} component={NotFound}/>
        <Route exact path={'/:short'} component={GoTo}/>
        <Redirect to={'/not-found'} />
      </Switch>
    </Router>
  )
}

export default App;