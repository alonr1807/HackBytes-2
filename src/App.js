import React, { useState } from 'react';
import logo from './logo.png';
import './App.css';
import $ from 'jquery';

function App() {
  const [textBoxValue, setTextBoxValue] = useState('');
  const [responseData, setResponseData] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleTextBoxChange = (event) => {
    setTextBoxValue(event.target.value);
  };

  const handleButtonClick = () => {
    setIsLoading(true);

    $.ajax({
      url: '/product',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ value: textBoxValue }),
      // success: (response) => {
      //   setResponseData(response.value);
      // },
    })

    .done((response) => {
      setResponseData(response.value);
    })
    .always(() => {
      setIsLoading(false);
    });

    console.log('Stored value:', textBoxValue);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="logo" alt="Logo" />
        <h1>Ecopact</h1>
      </header>
      <div className="text-box">
        <input
          type="text"
          placeholder="Enter your item"
          value={textBoxValue}
          onChange={handleTextBoxChange}
        />
        <button onClick={handleButtonClick}>Store Value</button>
      </div>
        {isLoading ? <p>Loading...</p> : <p>{responseData}</p>}
    </div>
  );
}

export default App;
