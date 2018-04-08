import React, {Component } from 'react'
import PropTypes from 'prop-types'
import TextField from 'material-ui/TextField';
import Grid from 'material-ui/Grid';
import Button from 'material-ui/Button';
import axios from 'axios';
import API_URL from '../../constants/urls';
class CreateShortenLink extends Component {
  constructor(props) {
    super(props);
    this.state = {
     url: '',
     shortcode: ''
    }
    this.handleForm = this.handleForm.bind(this);
  }
  handleForm(e) {
  axios.post(API_URL.getList, this.state)
    .then(res => {
      this.setState({url:'', shortcode:''},this.props.onChange)
    })
  }
  render() {
    return (

        <Grid container>
            <Grid items sm={4}>
               <TextField 
                 fullWidth
                 label="url"
                 id="url"
                 name="url"
                 value={this.state.url}
                 onChange={e => this.setState({url: e.target.value})}
                 margin="normal"
               />
            </Grid>
            <Grid items sm={4}>
               <TextField 
                 fullWidth
                 label="Short Code"
                 id="shortcode"
                 name="shortcode"
                 value={this.state.shortcode}
                 onChange={e => this.setState({shortcode: e.target.value})}
                 margin="normal"
               />
            </Grid>
            <Grid items sm={4}>
              <Button size="small" onClick={this.handleForm}>Submit</Button>
            </Grid>
        </Grid>)
}
}

export default CreateShortenLink
