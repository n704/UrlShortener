import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import ShortenList from './components/dashboard/ShortenList'
class App extends Component {
  render() {
    return (
      <div className="App" style={{ alignContent: 'center'}}>
        <ShortenList />
      </div>
    );
  }
}

export default App;
