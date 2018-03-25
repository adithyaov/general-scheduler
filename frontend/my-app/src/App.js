import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import comfortList from './comfortList.json'

class App extends Component {
  constructor(props){
    super(props);
    this.state={
      no_s : 0,
      sid : 0,
      no_c : 0,
      cid : 0,
      subs: [],
      no_t : 1,
      no_g : 1,
      dow: 5,
      no_p: 8,
      comforts: comfortList.comforts,
      comfConst: [],
    }
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
            Subject id: {subs.id} &nbsp;
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
        <h3>Comfort constraints</h3>
        Add a comfort constraint: {this.listComfort()}
        <button onClick={this.handleAddComfort()}>Add</button>
        <div>
        <ul>
          {this.state.comfConst.map((cons, idx) => (
            <li key={idx}>{this.makeConstBody(cons)}</li>
          ))}
        </ul>
        </div>
        </div>
    );
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
  handleAddComfort = () => (evt) => {
    var comfid = document.getElementById("comfList").value;
    var newcons = {id : this.state.cid, ctype: comfid};
    switch(comfid)
    {
      case "1":
        newcons['t1'] = 1;
        newcons['t2'] = 1;
        break;
      case "2":
        newcons['t'] = 0;
        newcons['p'] = 0;
        newcons['d'] = 0;
        break;
      case "3":
        newcons['g'] = 1;
        newcons['d'] = 0;
        newcons['p'] = 0;
        break;
      case "4":
        newcons['g1'] = 1;
        newcons['g2'] = 1;
        break;
      case "5":
        newcons['t1'] = 1;
        newcons['t2'] = 1;
        break;
      case "6":
        newcons['t1'] = 1;
        newcons['t2'] = 1;
        break;
      case "7":
        newcons['t'] = 1;
        newcons['nd'] = 1;
        break;
      case "8":
        newcons['g'] = 1;
        newcons['np'] = 1;
        break;
      case "9":
        newcons['t'] = 1;
        newcons['k'] = 1;
        break;
      case "10":
        newcons['s'] = 1;
        newcons['p'] = [];
        newcons['mode'] = 0;
        break;
      case "11":
        newcons['s'] = 1;
        newcons['d'] = 1;
        newcons['mode'] = 0;
        break;
      case "12":
        newcons['s'] = 1;
        newcons['mode'] = 0;
        break;
      default : return false;
    }
    this.setState({comfConst: this.state.comfConst.concat([newcons])});
    this.setState({no_c : this.state.no_c + 1,cid : this.state.cid + 1});
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
  setComfortParam = (cid, param) => (evt) =>
  {
    this.setState({comfConst : this.state.comfConst.map((comf) => {
      if(comf.id !== cid) return comf;
      comf[param] = evt.target.value;
      return comf;
    })});
    console.log("comfort param set for " + evt.target.value + " on constraint " + cid + " as " + param);
  }

  makeConstBody = (cons) => {
    switch(cons.ctype)
    {
      case "1": return (<span>Teacher: {this.createTlistComf(cons.id)}, not to be scheduled on day {this.createDlistComf(cons.id)} during period {this.createPlistComf(cons.id)} </span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "5": return (<span>Teachers not to be alloted at the same time: {this.createTlistComf(cons.id, "t1")} and {this.createTlistComf(cons.id, "t2")}</span>) 
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
      case "": return (<span></span>);
    }
  }
  createSubListComf(cid, paramName='s')
  {
    var options = []
    for(var i = 0; i < this.state.no_s; i++){
      options.push(React.createElement('option', {"value" : this.state.subs[i].id , "key": i}, "id: " + this.state.subs[i].id))
    }
    
    return(<select onChange={this.setComfortParam(cid, paramName)} >{options}</select>)
  }
  createTlistComf(cid, paramName='t')
  {
    var options = []
    for(var i = 0; i < this.state.no_t; i++){
      options.push(React.createElement('option', {"value" : i + 1 , "key": i}, i+1))
    }
    
    return(<select onChange={this.setComfortParam(cid, paramName)} >{options}</select>)
  }
  createGlistComf(cid, paramName='g')
  {
    var options = []
    for(var i = 0; i < this.state.no_g; i++){
      options.push(React.createElement('option', {"value" : i + 1, "key": i}, i+1))
    }
    return(<select onChange={this.setComfortParam(cid, paramName)}>{options}</select>)
  }
  createDlistComf(cid, paramName='d')
  {
    var options = [];
    var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
    for(var i = 0; i < this.state.dow; i++){
      options.push(React.createElement('option', {"value" : i + 1, "key": i}, ((i+1).toString()) + " (" + days[i] + ")"));
    }
    return(<select onChange={this.setComfortParam(cid, paramName)}>{options}</select>)
  }
  createPlistComf(cid, paramName='p')
  {
    var options = []
    for(var i = 0; i < this.state.no_p; i++){
      options.push(React.createElement('option', {"value" : i + 1, "key": i}, i+1))
    }
    return(<select onChange={this.setComfortParam(cid, paramName)}>{options}</select>)
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
  listComfort()
  {
    var listElem = []
    this.state.comforts.forEach((comfort) => {
      listElem.push(React.createElement('option', {value : comfort.id, key : comfort.id}, comfort.label));
    })
    return (<select id="comfList" key={this.state.cid}>{listElem}</select>)
  }
}

export default App;
