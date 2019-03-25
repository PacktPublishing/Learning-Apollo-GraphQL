import React from 'react';
import { gql, graphql } from 'react-apollo';

const Persons = ({ data: { loading, error, allPersons }}) => {
  if (loading) {
    return <p>Querying GraphQL ...</p>
  }
  if (error) {
    return <p>{error.message}</p>
  }

  return (
    <ul>
      { allPersons.edges.map( item => 
      (<li key={item.node.id_}>{item.node.id_} ' -> ' {item.node.name}</li>)
      )}
    </ul>
  );
}

export const allPersonsListQuery = gql`
query {
  allPersons {
    edges {
      node {
        id_
        name
      }
    }
  }
}

`;

export default graphql(allPersonsListQuery)(Persons);
