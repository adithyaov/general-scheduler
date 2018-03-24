import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      no_s : 0,
      sid : 0,
      subs: [],
      no_t : 1,
      no_g : 1,
      dow: 5,
      no_p: 8,
    }
  }

  handleAddClass = () => {
    if(this.state.no_s < 100){
      this.setState({subs : this.state.subs.concat([{
        id : this.state.sid + 1 ,
        name : '',
        t: 1,
        g: 1,
        n: 1,
       }])});
      this.setState({no_s : this.state.no_s + 1,sid : this.state.sid + 1});
    }
  }

  handleChangeClassName = (s_id) => (evt) => {
    this.setState({subs : this.state.subs.map((subj) => {
      if(subj.id !== s_id) return subj;
      subj.name = evt.target.value;
      return subj;
    })});
  }
  handleChangeHour = (s_id) => (evt) => {
    this.setState({subs : this.state.subs.map((subj) => {
      if(subj.id !== s_id) return subj;
      subj.n = evt.target.value;
      return subj;
    })});
  }

  handleRemoveClass = (idx) => () => {
    this.setState({subs: this.state.subs.filter((subs) => subs.id !== idx)});
    this.setState({no_s : this.state.no_s - 1});
    // console.log("Rem" + idx)
  }
  handleChangeNo_t = (evt) => {
    this.setState({no_t :evt.target.value});
  }
  handleChangeNo_g = (evt) => {
    this.setState({no_g :evt.target.value});
  }
  handleChangedow = (evt) => {
    this.setState({dow :evt.target.value});
  }
  handleChangeNo_p = (evt) => {
    this.setState({no_p :evt.target.value});
  }


  render() {
    return (
      <div className="App">
        <h2>Time Machine</h2>
        <button onClick={() => {console.log(this.state)}}>log state</button>
        <div>
          <label>No of working days in a week:</label>
          <input id="dow" type='number' onChange={this.handleChangedow} placeholder={this.state.dow} min="1"/>
          <br/>
          <label>No of periods in a day:</label>
          <input id="no_p" type='number' onChange={this.handleChangeNo_p} placeholder={this.state.no_p} min="1"/>
          <br/>
          <label>no of T: </label>
          <input id="no_t" type='number' onChange={this.handleChangeNo_t} placeholder={this.state.no_t} min="1"/>
          <br/>
          <label>no of G: </label>
          <input id="no_g" type='number' onChange={this.handleChangeNo_g} placeholder={this.state.no_g} min="1"/>
        </div>
        <h3>correctness constraints</h3>
        <ul>
        {this.state.subs.map((subs, idx) => (
          <li key={subs.id}>
          <div className='constraintBar'>
            <input type='text' placeholder={`Subject`} onChange={this.handleChangeClassName(subs.id)} />
            Teacher: { this.createTlist(subs.id) }
            Group: { this.createGlist(subs.id) }
            Hours: <input type='number' onChange={this.handleChangeHour(subs.id)} placeholder={this.state.no_g} min="1"/>
            <button onClick={this.handleRemoveClass(subs.id)} > Remove </button>
          </div>
          </li>
          )
          )}
        </ul>
        <button onClick={this.handleAddClass} > Add a class </button>
        </div>
    );
  }
  setTeacherConstraint = (sid) => (evt) =>
  {
    this.setState({subs : this.state.subs.map((subj) => {
      if(subj.id !== sid) return subj;
      subj.t = evt.target.value;
      return subj;
    })});
    console.log(" teacher constraint set for " + evt.target.value + " on " + sid);
  }
  setGroupConstraint = (sid) => (evt) =>
  {
    this.setState({subs : this.state.subs.map((subj) => {
      if(subj.id !== sid) return subj;
      subj.g = evt.target.value;
      return subj;
    })});
    console.log("group constraint set for " + evt.target.value + " on " + sid);
  }
  createTlist(sid)
  {
    var options = []
    for(var i = 0; i < this.state.no_t; i++){
      options.push(React.createElement('option', {"value" : i + 1 , "key": i}, i+1))
    }
    
    return(<select onChange={this.setTeacherConstraint(sid)} >{options}</select>)
  }
  createGlist(sid)
  {
    var options = []
    for(var i = 0; i < this.state.no_g; i++){
      options.push(React.createElement('option', {"value" : i + 1, "key": i}, i+1))
    }
    return(<select onChange={this.setGroupConstraint(sid)}>{options}</select>)
  }
}


export default App;
