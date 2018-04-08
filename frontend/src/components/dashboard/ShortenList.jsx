import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import API_URL from '../../constants/urls';
import CreateShortenLink from './CreateShortenLink';
import Paper from 'material-ui/Paper';
import Grid from 'material-ui/Grid';
import List, { ListItem, ListItemText } from 'material-ui/List';
import Card, { CardActions, CardContent } from 'material-ui/Card';
import Button from 'material-ui/Button';
import Typography from 'material-ui/Typography';
export default class ShortenList extends Component {
   constructor(props) {
    super();
    this.state = {
      page: 1,
      items: [],
      pagination:{}
    }
    this.getData = this.getData.bind(this);
  }
  componentWillMount() {
    this.getData()
  }
  paginate(direction) {
   if (direction == "next") {
    this.setState((prevState) => { page: prevState.page + 1}, () =>this.getData(this.state.page+1))
   }
   if (direction == "back") {
      this.setState((prevState) => { page: prevState.page - 1},()=> this.getData(this.state.page))
  }
}
  getData(page=this.state.page) {
      axios.get(API_URL.getList, { params: {page}})
        .then( res => {
          const jsonData = res.data
          this.setState({
            items: jsonData.data,
            pagination: jsonData.pagination
          })
        })
  }
  render() {
      console.log(this.state)
       let ShortenListToRender =  this.state.items.map((elem => 
        <Grid items sm={3} key={elem.shortcode}>
          <Card>
            <CardContent>
                <Typography variant="headline" component="h2">
                  {elem.shortcode}
                </Typography>
                <Typography  color="textSecondary">
                  {elem.url}
                </Typography>
            </CardContent>
            <CardActions>
              <Button size="small" href={elem.url} target="_blank">Navigate</Button>
            </CardActions>
          </Card>
        </Grid>
      ))
      let nextButton = null;
      let prevButton = null;
      let pagination = this.state.pagination
      console.log(pagination.count,)
      if (pagination.count > pagination.page) {
       nextButton = <Button size="small" onClick={e => this.paginate("next")}> NEXT</Button>
      }
      if (pagination.page > 1) {
       prevButton = <Button size="small" onClick={e => this.paginate("back")}> PREV</Button>
      }
      return (
        <Grid alignContent='center' alignItems='center' container>
          <Grid items sm={4}></Grid>
          <Grid items sm={8}>
              <CreateShortenLink onChange={this.getData}/>
          </Grid>
          <Grid container>
              {ShortenListToRender}
          </Grid>
          <Grid container>
            <Grid items sm={3}>
              {prevButton}
            </Grid>
            <Grid items sm={6}>
            </Grid>
            <Grid items sm={3}>
              {nextButton}
            </Grid>
          </Grid>
        </Grid>

)
    }
}