require('dotenv').config();

const fs = require('fs');
const path = require('path');
const express = require('express');
const cors = require('cors');
const { ApolloServer } = require('@apollo/server');
const { expressMiddleware } = require('@as-integrations/express5');
const pool = require('./db');

const typeDefs = fs.readFileSync(
  path.join(__dirname, 'schema.graphql'),
  'utf8'
);

const resolvers = {
  Query: {
    dishes: async () => {
      const [rows] = await pool.execute(
        'SELECT id, name, price, available FROM dishes ORDER BY id'
      );

      return rows.map(row => ({
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      }));
    },

    dish: async (_, { id }) => {
      const [rows] = await pool.execute(
        'SELECT id, name, price, available FROM dishes WHERE id = ?',
        [id]
      );

      if (rows.length === 0) {
        return null;
      }

      const row = rows[0];

      return {
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      };
    }
  },

  Mutation: {
    addDish: async (_, { input }) => {
      const { name, price, available = true } = input;

      const [result] = await pool.execute(
        'INSERT INTO dishes (name, price, available) VALUES (?, ?, ?)',
        [name, price, available]
      );

      const [rows] = await pool.execute(
        'SELECT id, name, price, available FROM dishes WHERE id = ?',
        [result.insertId]
      );

      const row = rows[0];

      return {
        ...row,
        id: String(row.id),
        price: Number(row.price),
        available: Boolean(row.available)
      };
    }
  }
};

async function startServer() {
  const app = express();
  const server = new ApolloServer({ typeDefs, resolvers });

  await server.start();

  app.use(express.static(path.join(__dirname, 'public')));

  app.use(
    '/graphql',
    cors(),
    express.json(),
    expressMiddleware(server)
  );

  const port = Number(process.env.PORT) || 4000;

  app.listen(port, () => {
    console.log(`CampusEats is running at http://localhost:${port}`);
    console.log(`GraphQL endpoint: http://localhost:${port}/graphql`);
  });
}

startServer().catch(error => {
  console.error('Failed to start the server:', error.message);
  process.exit(1);
});
