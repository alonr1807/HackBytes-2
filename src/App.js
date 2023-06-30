import React, { useState } from 'react';
import logo from './logo.png';
import './App.css';

function App() {
  const [textBoxValue, setTextBoxValue] = useState('');

  const handleTextBoxChange = (event) => {
    setTextBoxValue(event.target.value);
  };

  // send to bard api to find materials
  const handleButtonClick = () => {
    console.log('Stored value:', textBoxValue);
  };

  return (
    <div className="App">
      <header className="App-header">
      <img src={logo} className="logo"/>
        <h1>Ecopact</h1>
        
      </header>
      <div className="text-box">
          <input type="text" 
          placeholder="Enter your item" 
          value={textBoxValue}
          onChange={handleTextBoxChange}
          />
          <button onClick={handleButtonClick}>
            Store Value
          </button>
        </div>
    </div>
  );
}

export default App;
