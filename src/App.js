import React, { useState } from 'react';
import logo from './logo.png';
import './App.css';
import $ from 'jquery';

function App() {
  const [textBoxValue, setTextBoxValue] = useState('');
  const [responseData, setResponseData] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showSearch, setShowSearch] = useState(true);

  const handleTextBoxChange = (event) => {
    setTextBoxValue(event.target.value);
  };

  const handleButtonClick = () => {
    setShowSearch(false);
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
      {showSearch && 

      <h1 className='header'>The Eco-Friendly way to shop</h1>
      }
      {showSearch && 
      <div className="text-box" id = "cover">
        <input
          type="text"
          placeholder="Enter your item"
          value={textBoxValue}
          onChange={handleTextBoxChange}
        />
        <button onClick={handleButtonClick}><svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="currentColor" viewBox="0 0 16 16">
  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"></path>
</svg></button>
      </div>
      }
      {isLoading ? <p>Loading...</p> : <p className='data'>{responseData}</p>}
    </div>
  );
}

export default App;
