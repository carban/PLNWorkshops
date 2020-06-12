import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {
  render() {
    return (
      <div className="App" >
        <h1>POS-Tagging</h1>
        <textarea
          style={{
            "borderWidth": "5px",
            "width": "700px",
            "height": "100px",
            "fontSize": "15px"
          }} >

        </textarea>
      </div>
    );
  }
}

export default App;
