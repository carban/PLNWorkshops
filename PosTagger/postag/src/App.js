import React from 'react';
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      sentences: [
        ["Correr", "es", "importante", "para", "mi"],
        ["El", "hombre", "bajo", "corre", "bajo", "el", "puente", "con", "bajo", "indice", "de", "adrenalina"]
      ],
      tags: [
        ["vmn0000", "vsip3s0", "aq0cs0", "sps00", "aq0fsp"],
        ["da0ms0", "ncms000", "sps00", "vmip3s0", "sps00", "da0ms0", "ncms000", "sps00", "sps00", "ncms000", "sps00", "np0000o"]
      ]
    }
  }

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
        <br></br>
        <div>
          {
            this.state.sentences.map((sentence, i) => (
              <table key={i}>
                <div>
                  <tr>
                    {
                      sentence.map((word, j) => (
                        <td key={j} style={{ "border": "1px solid black" }}>
                          {word}
                        </td>
                      ))
                    }
                  </tr>
                  <tr>
                    {
                      sentence.map((word, j) => (
                        <td key={j} style={{ "border": "1px solid black" }}>
                          {this.state.tags[i][j]}
                        </td>
                      ))
                    }
                  </tr>
                </div>
              </table>

            ))
          }
        </div>
      </div>
    );
  }
}

export default App;
