import logo from './logo.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <img src={logo} className="logo"/>
        <h1>Ecopact</h1>
        
      </header>
      <div className="text-box">
          <input type="text" placeholder="Enter your text" />
        </div>
    </div>
  );
}

export default App;
