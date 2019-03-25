export const typeDefs = `
  type Person {
    id_: ID!
    name: String
  }

  type Query {
    allPersons: [Person]
  }
`;
