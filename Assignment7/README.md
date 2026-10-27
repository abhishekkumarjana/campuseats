# CampusEats GraphQL Menu Service

## Project Description

This project implements the CampusEats Menu Service using GraphQL.
It allows users to view dishes and add new dishes through a simple
HTML, CSS, and JavaScript frontend.

## Technologies Used

- Node.js
- Apollo Server
- GraphQL
- MySQL
- mysql2
- Express.js
- HTML, CSS, and JavaScript

## Features

- List all dishes using a GraphQL query.
- Retrieve a dish by its ID.
- Add a new dish using a GraphQL mutation.
- Store dish information in a MySQL database.
- Display dishes through a web interface.

## Project Structure

- schema.graphql: GraphQL type definitions, queries, and mutations.
- server.js: Apollo Server, Express application, and resolvers.
- db.js: MySQL database connection.
- schema.sql: Database table and sample records.
- public/index.html: Frontend webpage.
- README.md: Project documentation.

## Database Setup

Create the database and project user before running the application.

Execute the SQL in schema.sql using the campususer account:

mysql -u campususer -p campuseats < schema.sql

Configure the database connection using a local .env file.
Do not upload .env to GitHub.

## How to Run

1. Install Node.js and npm.
2. Install dependencies:

   npm install

3. Configure the database credentials in .env.
4. Create the database table and sample records using schema.sql.
5. Start the server:

   node server.js

6. Open http://localhost:4000 in your browser.

The GraphQL endpoint is available at:
http://localhost:4000/graphql

## Answers to Assignment Questions

### 1. Which CampusEats service did you pick?

We selected the CampusEats Menu Service.
It manages dishes and their prices and availability.

### 2. Name one field a client can skip and one it cannot. Why do we use !?

A client can skip the available field in a query if it does not need
that information. It can also omit the available input when adding
a dish because the input field is optional.

The name field in AddDishInput cannot be omitted because it is
defined as String!. The exclamation mark indicates that the value
must not be null.

### 3. Map the query to SQL. Which part becomes WHERE, and which resolver runs INSERT?

In the dish(id: ID!) query, the id argument is passed to the resolver.
The resolver uses the SQL condition WHERE id = ? to retrieve the
matching dish.

The addDish mutation is handled by the addDish resolver.
It executes an SQL INSERT statement to save the new dish in MySQL.

## Team Members

[ASHISH KUMAR SINGH] [20252651014]
[ABHISHEK KUMAR JANA][20252651002]
[BIKASH PRADHAN][20252651015]
[TUSHAR BHARDWAJ][20252651058]
.

## Demonstration

GitHub Repository: Add your repository link here.

Google Drive Demonstration Video: Add your video link here.

Before Screenshot: Add your screenshot reference here.

After Screenshot: Add your screenshot reference here.
