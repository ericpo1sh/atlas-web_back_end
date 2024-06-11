## Resources

**Read or watch**:

- [NoSQL Databases Explained](https://intranet.atlasschool.com/rltoken/0HR2bZ3XFJzkttuEVF5Rug)
- [What is NoSQL ?](https://intranet.atlasschool.com/rltoken/JGxz6PJsAN9cjBBT_WVCAg)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://intranet.atlasschool.com/rltoken/PkdXgnfXUfJIk5iqf9Wp4A)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://intranet.atlasschool.com/rltoken/y6ncfHy0Hn7uqaIyitWQRg)
- [Aggregation](https://intranet.atlasschool.com/rltoken/sIORcQADQT2Wf2opdMu30Q)
- [Introduction to MongoDB and Python](https://intranet.atlasschool.com/rltoken/BLt93wwWTkVQWVlSDerI1g)
- [mongo Shell Methods](https://intranet.atlasschool.com/rltoken/q-RfEFpmN-fGiX-SvmQjHA)
- [The mongo Shell](https://intranet.atlasschool.com/rltoken/fmrWM3wzfC2d2-WHqzzPBQ)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/2Kw4G-iwbeaF3gBMQiUZJg), **without the help of Google**:

### General

- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## What does NoSQL mean?

Some say the term “NoSQL” stands for “**non SQL**” while others say it stands for “not only SQL”. Either way, most agree that NoSQL databases are databases that store data in a format other than relational tables.

## What is the difference between SQL and NoSQL?

SQL databases are relational, and NoSQL databases are non-relational.
SQL databases use structured query language (SQL) and have a predefined
schema. NoSQL databases have dynamic schemas for unstructured data. SQL
databases are vertically scalable, while NoSQL databases are 
horizontally scalable. SQL databases are table based, while NoSQL databases can be document-oriented, key-value pairs, or graph structures

## What is ACID?

**ACID is an acronym that stands for *atomicity, consistency, isolation, and durability.***

ACID transactions guarantee that a database will be in a consistent state after running a group of operations.

Together, these ACID properties ensure that a set of database operations (grouped together in a transaction) leave the database in a valid state even in the event of unexpected errors.

## What is a document storage?

A document storage system is a *system that controls the storage, sharing and organization of electronic files or captured* data from paper-based documents.

## What are NoSQL types?

1. **Document-Oriented Databases**:
    - **Description**: Store data as documents, typically in JSON or BSON formats. Each document can have a different structure, which provides flexibility in storing varying types of data.
    - **Examples**: MongoDB, CouchDB
2. **Key-Value Stores**:
    - **Description**: Store data as key-value pairs where the key is a unique identifier and the value is the data associated with the key. This type is highly efficient for simple lookups and provides fast read and write operations.
    - **Examples**: Redis, DynamoDB, Riak
3. **Column-Family Stores**:
    - **Description**: Store data in columns rather than rows, allowing for efficient storage and retrieval of large datasets. This type is particularly effective for data warehousing and big data analytics.
    - **Examples**: Cassandra, HBase
4. **Graph Databases**:
    - **Description**: Designed to store and navigate relationships between data points. They use graph structures with nodes, edges, and properties to represent and store data.
    - **Examples**: Neo4j, ArangoDB, OrientDB
5. **Wide-Column Stores**:
    - **Description**: Similar to column-family stores, but often used interchangeably. They store data in tables, rows, and dynamic columns, allowing for high performance in read and write operations across distributed systems.
    - **Examples**: Google Bigtable, Apache Accumulo

## What are benefits of a NoSQL database?

- NoSQL databases have **flexible data models, scale horizontally, have incredibly fast queries, and are easy for developers to work with**.
- They **allow the data to be stored in ways that are easier to understand or closer to the way the data is used by applications.**
- **NoSQL databases are suitable for structured, semi-structured, and unstructured data.**

## How to query information from a NoSQL database?

Querying information from a NoSQL database varies depending on the type of NoSQL database you're working with. Here are some general guidelines and examples for querying different types of NoSQL databases:

### Document-Oriented Databases (e.g., MongoDB)

Document-oriented databases use query languages similar to JSON to retrieve data.

- **Example**: MongoDB
    
    ```jsx
    // Find all documents in the 'users' collection where the age is greater than 25
    db.users.find({ age: { $gt: 25 } })
    
    // Find a document by its unique ID
    db.users.findOne({ _id: ObjectId("60d5f884afbb4b3b1d8b4e3f") })
    
    // Find all documents with a specific name and sort by age
    db.users.find({ name: "John Doe" }).sort({ age: 1 })
    ```
    

### Key-Value Stores (e.g., Redis)

Key-value stores are typically accessed using their specific command-line interfaces or APIs.

- **Example**: Redis
    
    ```
    // Set a value
    SET user:1000 '{"name": "John Doe", "age": 30}'
    
    // Get a value
    GET user:1000
    
    // Increment a value
    INCR counter
    ```
    

### Column-Family Stores (e.g., Cassandra)

Column-family stores use query languages like CQL (Cassandra Query Language), which is similar to SQL.

- **Example**: Cassandra
    
    ```sql
    // Select all columns from a table where age is greater than 25
    SELECT * FROM users WHERE age > 25;
    
    // Select a specific user by ID
    SELECT * FROM users WHERE user_id = '1234';
    
    // Insert a new record
    INSERT INTO users (user_id, name, age) VALUES ('1234', 'John Doe', 30);
    ```
    

### Graph Databases (e.g., Neo4j)

Graph databases use languages like Cypher to traverse and query graph data structures.

- **Example**: Neo4j
    
    ```
    // Find all nodes with a specific label and property
    MATCH (n:Person {name: "John Doe"}) RETURN n;
    
    // Find relationships between nodes
    MATCH (n:Person)-[r:KNOWS]->(m:Person) RETURN n, r, m;
    
    // Create a new node and relationship
    CREATE (n:Person {name: "John Doe", age: 30})-[:KNOWS]->(m:Person {name: "Jane Smith"});
    ```
    

### General Tips for Querying NoSQL Databases

- **Understand the Data Model**: Each NoSQL database has a unique data model (documents, key-value pairs, columns, or graph nodes/edges). Understanding how data is stored and accessed is crucial.
- **Use Appropriate Query Language or API**: Each NoSQL database typically has its own query language or API. Familiarize yourself with the syntax and capabilities.
- **Leverage Indexing**: Many NoSQL databases support indexing to speed up queries. Make use of indexes where appropriate.
- **Monitor and Optimize**: Monitor query performance and optimize as needed, which might include indexing, data partitioning, or query adjustments.

## How to insert/update/delete information from a NoSQL database?

Inserting, updating, and deleting information from a NoSQL database depends on the type of NoSQL database you're using. Here are some examples for various types:

### Document-Oriented Databases (e.g., MongoDB)

**Insert:**

```jsx
// Insert a single document
db.users.insertOne({ name: "John Doe", age: 30, email: "john.doe@example.com" })

// Insert multiple documents
db.users.insertMany([
  { name: "Jane Smith", age: 25, email: "jane.smith@example.com" },
  { name: "Mike Johnson", age: 35, email: "mike.johnson@example.com" }
])
```

**Update:**

```jsx
// Update a single document
db.users.updateOne(
  { name: "John Doe" },
  { $set: { age: 31 } }
)

// Update multiple documents
db.users.updateMany(
  { age: { $gt: 30 } },
  { $set: { status: "senior" } }
)
```

**Delete:**

```jsx
// Delete a single document
db.users.deleteOne({ name: "John Doe" })

// Delete multiple documents
db.users.deleteMany({ age: { $lt: 25 } })
```

### Key-Value Stores (e.g., Redis)

**Insert (Set a Value):**

```
SET user:1000 '{"name": "John Doe", "age": 30, "email": "john.doe@example.com"}'
```

**Update (Overwrite a Value):**

```
SET user:1000 '{"name": "John Doe", "age": 31, "email": "john.doe@example.com"}'
```

**Delete:**

```
DEL user:1000
```

### General Tips for Working with NoSQL Databases

1. **Understand the API**: Each NoSQL database typically provides a specific API or query language for data operations. Ensure you understand the syntax and semantics.
2. **Use Transactions if Available**: Some NoSQL databases support transactions, which allow for multiple operations to be executed atomically. Use transactions to ensure data consistency.
3. **Indexing**: Properly index your data to optimize performance for update and delete operations.
4. **Data Model**: Understand the data model and schema design best practices for your specific NoSQL database type to ensure efficient and scalable operations.
5. **Backup and Recovery**: Ensure you have a backup and recovery strategy in place, especially when performing bulk updates or deletes.

## How to use MongoDB?

https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/

### Start MongoDB.

You can start the [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) process by issuing the
following command:

```
sudo systemctl start mongod
```

If you receive an error similar to the following when starting [`mongod`:](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod)

`Failed to start mongod.service: Unit mongod.service not found.`

Run the following command first:

```
sudo systemctl daemon-reload
```

Then run the start command above again.

### Verify that MongoDB has started successfully.

```
sudo systemctl status mongod
```

You can optionally ensure that MongoDB will start following a
system reboot by issuing the following command:

```
sudo systemctl enable mongod
```

### Stop MongoDB.

As needed, you can stop the [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) process by issuing the
following command:

```
sudo systemctl stop mongod
```

### Restart MongoDB.

You can restart the [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) process by issuing the following
command:

```
sudo systemctl restart mongod
```

You can follow the state of the process for errors or important messages
by watching the output in the `/var/log/mongodb/mongod.log` file.

### Begin using MongoDB.

Start a [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh) session on the same host machine as the [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod). You can run [`mongosh](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)` without any command-line options to connect to a [`mongod`](https://www.mongodb.com/docs/manual/reference/program/mongod/#mongodb-binary-bin.mongod) that is running on your localhost with default port 27017.

`mongosh`
