import React from 'react';
import './App.css';

// import axios from "axios";
import { Container, Table, Button } from "reactstrap";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      text: "",
      sentences: [
        // ["Correr", "es", "importante", "para", "mi"],
        // ["El", "hombre", "bajo", "corre", "bajo", "el", "puente", "con", "bajo", "indice", "de", "adrenalina"]
      ],
      tags: [
        // ["vmn0000", "vsip3s0", "aq0cs0", "sps00", "aq0fsp"],
        // ["da0ms0", "ncms000", "sps00", "vmip3s0", "sps00", "da0ms0", "ncms000", "sps00", "sps00", "ncms000", "sps00", "np0000o"]
      ]
    }
  }

  handleInput(e) {
    this.setState({ text: e.target.value });
  }

  run(e) {
    e.preventDefault();
    alert(this.state.text);
    // axios.post('/')
    //   .then(res => {
    //     // TODO
    //   })
    //   .catch(err => {
    //     console.log(err);
    //   })
  }

  render() {
    return (
      <div className="App" >
        <h1>POS-Tagging</h1>
        <textarea
          onChange={this.handleInput.bind(this)}
          style={{
            "borderWidth": "7px",
            "width": "700px",
            "height": "115px",
            "fontSize": "20px"
          }} >
        </textarea>

        <br></br>
        <Button color="danger" onClick={this.run.bind(this)}>
          Run!
        </Button>
        <br></br>
        <br></br>

        {
          this.state.sentences.length !== 0 ?
            (
              <Container>
                {
                  this.state.sentences.map((sentence, i) => (
                    <Table key={i} size="sm" bordered hover>
                      <div>
                        <tr>
                          {
                            sentence.map((word, j) => (
                              <td key={j}>
                                {word}
                              </td>
                            ))
                          }
                        </tr>
                        <tr>
                          {
                            sentence.map((word, j) => (
                              <td key={j} style={{ "color": "red" }}>
                                <b>
                                  {this.state.tags[i][j]}
                                </b>
                              </td>
                            ))
                          }
                        </tr>
                      </div>
                    </Table>

                  ))
                }
              </Container>
            ) : true
        }
      </div>
    );
  }
}

export default App;