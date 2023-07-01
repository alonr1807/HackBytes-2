import React, { useState, useEffect} from 'react';
import logo from './logo.png';
import './App.css';
import $ from 'jquery'

function App() {
  const [textBoxValue, setTextBoxValue] = useState('');
  const [data, setData] = useState([{}])


  




  const handleTextBoxChange = (event) => {

    setTextBoxValue(event.target.value);
  };
  // send to bard api to find materials
  const handleButtonClick = () => {

    $.ajax({
      url: 'http://127.0.0.1:5000/test',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ 'value': textBoxValue })
    })

    console.log('Stored value:', textBoxValue);
  };

  useEffect(() => {
    fetch("/members").then (
      res => res.json()
  ).then(
    data => {
      setData(data)
      console.log(data)
    }
  )

  }, [])

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
