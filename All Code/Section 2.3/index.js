const { ApolloServer, gql } = require('apollo-server');

// This is a small sample collection of books.
const books = [
  {
    title: 'Learning Apollo GraphQL - Book',
    author: 'Unknown',
  },
  {
    title: 'Learning Apollo GraphQL - Video',
    author: 'Doug Ortiz',
  },
];

// Type definitions define the "shape" of our data and specify
// which ways the data can be fetched from the GraphQL server.
const typeDefs = gql`
  # Comments in GraphQL are defined with the hash (#) symbol.

  type Book {
    title: String
    author: String
  }

  # This is for marking an operation or a mutation
  type Query {
    books: [Book]
  }
`;

// Resolvers define how we will fetch the types in the schema.
const resolvers = {
  Query: {
    books: () => books,
  },
};

// Starts the Apollo Server
const server = new ApolloServer({ typeDefs, resolvers });

// `listen` method launches a web-server.  
server.listen().then(({ url }) => {
  console.log(`Apollo Server is ready at ${url}`);
});