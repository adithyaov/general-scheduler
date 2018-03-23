import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      no_s : 3,
      subs: [{id : 0}, {id : 1}, {id : 2}]
    }
  }
  handleRemoveConstraint = (idx) => {
    // this.setState({subs: this.state.subs.filter((s, sidx) => idx !== sidx)});
    console.log("Rem" + idx)
  }
  handleAddConstraint = (idx) => {
    this.setState({subs : this.state.subs.concat([{id : idx}])});
  }

  render() {
    return (
      <div className="App">
        {
        React.createElement('div', {}, [
          React.createElement('label', {}, "T: "),
          React.createElement('input', {type : "number", min : 1}),

          // React.createElement('label', {id: 'no_s', }, "S: "),
          // React.createElement('input', {type : "number", min : 1}),

          React.createElement('label', {}, "G: "),
          React.createElement('input', {type : "number", min : 1}),         
          ]
          )
        }
        <ul>
        {this.state.subs.map((subs, idx) => (
          <li key={subs.id}>
          <div className='constraintBar'>
            <input type='text' placeholder={`Constraint #${idx + 1}`} />
            <button onClick={this.handleRemoveConstraint(idx)} > Remove </button>
          </div>
          </li>
          )
          )}
        </ul>
        <button onClick={this.handleAddConstraint(this.state.no_s)} > Add constraint </button>
        </div>
    );
  }

  TSG()
  {
    return (
      <div>poiuytre</div>
      )
  }

}

export default App;
