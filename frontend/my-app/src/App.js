import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      no_s : 0,
      subs: [],
      no_t : 1,
      no_g : 1,
    }
  }

  handleAddConstraint = () => {
    if(this.state.no_s < 100){
      this.setState({subs : this.state.subs.concat([{id : this.state.no_s}])});
      this.setState({no_s : this.state.no_s + 1,})
    }
  }

  handleRemoveConstraint = (idx) => () => {
    this.setState({subs: this.state.subs.filter((s, sidx) => idx !== sidx)});
    // console.log("Rem" + idx)
  }
  handleChangeNo_t = (evt) => {
    this.setState({no_t :evt.target.value});
  }
  handleChangeNo_g = (evt) => {
    this.setState({no_g :evt.target.value});
  }

  render() {
    return (
      <div className="App">
        <div>
          <label>T: </label>
          <input type='number' onChange={this.handleChangeNo_t}/>
          <label>G: </label>
          <input type='number' onChange={this.handleChangeNo_g}/>
        </div>
        <ul>
        {this.state.subs.map((subs, idx) => (
          <li key={subs.id}>
          <div className='constraintBar'>
            <input type='text' placeholder={`Constraint #${subs.id + 1}`} />
            <button onClick={this.handleRemoveConstraint(idx)} > Remove </button>
          </div>
          </li>
          )
          )}
        </ul>
        <button onClick={this.handleAddConstraint} > Add constraint </button>
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
