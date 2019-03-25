import React, { Component } from 'react';
import { ApolloClient, ApolloProvider, createNetworkInterface } from 'react-apollo';
import './App.css';
import Persons from './Persons';

const networkInterface = createNetworkInterface({
  uri: 'http://localhost:5000/graphql',
  fetchOptions: {
    mode: 'no-cors',
  },
});

const client = new ApolloClient({
  networkInterface,
});

class App extends Component {
  render() {
    return (
      <ApolloProvider client={client}>
        <div className="App">
          <div className="App-header">
            <h1>List of Persons</h1>
            <h3>ID and Name</h3>
          </div>
          <Persons />
        </div>
      </ApolloProvider>
    );
  }
}

export default App;
