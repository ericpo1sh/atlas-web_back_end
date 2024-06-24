**Read or watch**:

- [Redis quick start](https://intranet.atlasschool.com/rltoken/7eegJpVLrLqzvxgOC9cfng)
- [Redis client interface](https://intranet.atlasschool.com/rltoken/qTNQbh4fk23sAJdjtgJY4Q)
- [Redis client for Node JS](https://intranet.atlasschool.com/rltoken/y1WPXQxH-S7Op_P2bh7dPg)
- [Kue](https://intranet.atlasschool.com/rltoken/tj3H4qD7u8yg-IhtbSyG7A) *deprecated but still use in the industry*

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/KVesHRrG4OE8kHXfVkojZw), **without the help of Google**:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to the build a basic Express app interacting with a Redis server and queue

## How to use Redis Client with Node JS

sing a Redis client with Node.js for basic operations involves a few steps, including setting up your Node.js environment, installing the Redis client library, and writing code to perform basic operations like setting, getting, and deleting values. Here's a detailed guide for your notes:

### Step 1: Set Up Node.js Environment

Ensure you have Node.js installed. If not, download and install it from [nodejs.org](https://nodejs.org/).

### Step 2: Install Redis

Make sure Redis is installed and running on your local machine or a remote server. You can download and install Redis from redis.io.

### Step 3: Install Redis Client Library

Use npm to install the Redis client library (`redis`):

```
npm install redis
```

### Step 4: Write Code for Basic Operations

Create a JavaScript file (e.g., `redis_operations.js`) and add the following code to perform basic operations like connecting to Redis, setting, getting, and deleting values.

### Using CommonJS Syntax

```jsx
// Import the redis package
const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

// Basic Redis operations
async function redisOperations() {
    try {
        // Set a key-value pair
        await client.set('myKey', 'myValue');
        console.log('Key set successfully');

        // Get the value of a key
        const value = await client.get('myKey');
        console.log('Value for myKey:', value);

        // Delete a key
        await client.del('myKey');
        console.log('Key deleted successfully');
    } catch (err) {
        console.error('Error during Redis operations:', err);
    } finally {
        // Close the connection
        client.quit();
    }
}

// Run the Redis operations
redisOperations();
```

## How to store hash values in Redis

Storing hash values in Redis allows you to organize and manipulate related key-value pairs in a structured way. In Node.js, you can use the `redis` library to perform operations on hash data structures. Here's how you can store, retrieve, and delete hash values in Redis using both CommonJS and ES6 syntax.

```jsx
// Import the redis package
const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

async function hashOperations() {
    try {
        // Set multiple fields in a hash
        await client.hSet('user:1000', 'name', 'John Doe', 'email', 'john.doe@example.com', 'age', '30');
        console.log('Hash fields set successfully');

        // Get a specific field from a hash
        const name = await client.hGet('user:1000', 'name');
        console.log('Name:', name);

        // Get all fields and values from a hash
        const user = await client.hGetAll('user:1000');
        console.log('User:', user);

        // Delete a specific field from a hash
        await client.hDel('user:1000', 'age');
        console.log('Field deleted successfully');
    } catch (err) {
        console.error('Error during hash operations:', err);
    } finally {
        // Close the connection
        client.quit();
    }
}

// Run the hash operations
hashOperations();
```

### Explanation of the Code

1. **Import the Redis library**: Use `require` (CommonJS) or `import` (ES6) to include the Redis library.
2. **Create a Redis client**: Use `redis.createClient()` to create a new Redis client instance.
3. **Handle connection events**:
    - `on('connect', ...)` logs a message when the client connects successfully.
    - `on('error', ...)` logs a message if there's an error.
4. **Connect to the Redis server**: Use `client.connect()` to establish the connection.
5. **Hash operations**:
    - `client.hSet('hashKey', 'field1', 'value1', 'field2', 'value2')` sets multiple fields in a hash.
    - `client.hGet('hashKey', 'field')` retrieves the value of a specific field.
    - `client.hGetAll('hashKey')` retrieves all fields and values from a hash.
    - `client.hDel('hashKey', 'field')` deletes a specific field from a hash.
6. **Close the connection**: Use `client.quit()` to close the connection to the Redis server.

## How to deal with async operations in Redis

```jsx
const redis = require('redis');

// Create a Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

async function asyncOperations() {
    try {
        // Set a key-value pair
        await client.set('myKey', 'myValue');
        console.log('Key set successfully');

        // Get the value of a key
        const value = await client.get('myKey');
        console.log('Value for myKey:', value);

        // Delete a key
        await client.del('myKey');
        console.log('Key deleted successfully');

        // Set multiple fields in a hash
        await client.hSet('user:1000', 'name', 'John Doe', 'email', 'john.doe@example.com', 'age', '30');
        console.log('Hash fields set successfully');

        // Get a specific field from a hash
        const name = await client.hGet('user:1000', 'name');
        console.log('Name:', name);

        // Get all fields and values from a hash
        const user = await client.hGetAll('user:1000');
        console.log('User:', user);

        // Delete a specific field from a hash
        await client.hDel('user:1000', 'age');
        console.log('Field deleted successfully');
    } catch (err) {
        console.error('Error during Redis operations:', err);
    } finally {
        // Close the connection
        client.quit();
    }
}

// Run the async operations
asyncOperations();
```

### Explanation of the Code

1. **Import the Redis library**: Use `require` (CommonJS) or `import` (ES6) to include the Redis library.
2. **Create a Redis client**: Use `redis.createClient()` to create a new Redis client instance.
3. **Handle connection events**:
    - `on('connect', ...)` logs a message when the client connects successfully.
    - `on('error', ...)` logs a message if there's an error.
4. **Connect to the Redis server**: Use `client.connect()` to establish the connection.
5. **Asynchronous operations**:
    - `client.set('myKey', 'myValue')` sets a key-value pair.
    - `client.get('myKey')` retrieves the value of a specific key.
    - `client.del('myKey')` deletes a key.
    - `client.hSet('user:1000', 'field1', 'value1', 'field2', 'value2')` sets multiple fields in a hash.
    - `client.hGet('user:1000', 'field')` retrieves the value of a specific field.
    - `client.hGetAll('user:1000')` retrieves all fields and values from a hash.
    - `client.hDel('user:1000', 'field')` deletes a specific field from a hash.
6. **Close the connection**: Use `client.quit()` to close the connection to the Redis server.

## How to use Kue as a queue system

Kue is a priority job queue backed by Redis that enables you to create, process, and monitor jobs in Node.js. Here's a step-by-step guide on how to use Kue as a queue system in your Node.js application:

### Step 1: Set Up Node.js Environment

Ensure you have Node.js installed. If not, download and install it from [nodejs.org](https://nodejs.org/).

### Step 2: Install Kue and Redis Client Library

Install Kue and the Redis client library using npm:

```
npm install kue
```

### Step 3: Create a Basic Kue Setup

Create a new JavaScript file (e.g., `queue_example.js`) and add the following code to create and process jobs using Kue.

### Example Code

```jsx
// Import the kue library
const kue = require('kue');

// Create a Kue queue
const queue = kue.createQueue();

// Create a job
const job = queue.create('email', {
    title: 'Welcome email for new user',
    to: 'user@example.com',
    template: 'welcome-email'
}).save((err) => {
    if (!err) console.log(`Job saved with ID: ${job.id}`);
});

// Process jobs in the queue
queue.process('email', (job, done) => {
    sendEmail(job.data, done);
});

// Function to simulate sending an email
function sendEmail(data, done) {
    console.log(`Sending email to ${data.to} with template ${data.template}`);
    // Simulate async email sending with setTimeout
    setTimeout(() => {
        console.log('Email sent successfully');
        done();
    }, 1000);
}

// Handle job events
queue.on('job enqueue', (id, type) => {
    console.log(`Job ${id} got queued of type ${type}`);
}).on('job complete', (id, result) => {
    console.log(`Job ${id} completed with result ${result}`);
}).on('job failed', (id, errorMessage) => {
    console.log(`Job ${id} failed with error ${errorMessage}`);
});
```

### Explanation of the Code

1. **Import the Kue library**: Use `require` to import the Kue library.
2. **Create a Kue queue**: `kue.createQueue()` initializes a new Kue queue.
3. **Create a job**: `queue.create('job_type', job_data).save(callback)` creates a new job of the specified type with the given data and saves it to the queue.
4. **Process jobs in the queue**: `queue.process('job_type', (job, done) => { ... })` processes jobs of the specified type. The `done` callback should be called when the job is completed.
5. **Simulate sending an email**: The `sendEmail` function simulates an asynchronous email sending operation using `setTimeout`.
6. **Handle job events**: Use `queue.on` to listen for various job events like enqueue, complete, and fail.

## How to build a basic Express app interacting with a Redis server

### Step 1: Create the Express Application

Create a new JavaScript file (e.g., `app.js`) and add the following code to set up the Express application and connect to the Redis server.

### Example Code

```jsx
// Import required modules
const express = require('express');
const redis = require('redis');

// Create an Express application
const app = express();

// Create a Redis client
const client = redis.createClient();

// Handle Redis connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

// Middleware to parse JSON bodies
app.use(express.json());

// Route to set a key-value pair in Redis
app.post('/set', async (req, res) => {
    const { key, value } = req.body;
    try {
        await client.set(key, value);
        res.status(200).send(`Key "${key}" set successfully`);
    } catch (err) {
        res.status(500).send(`Error setting key "${key}": ${err.message}`);
    }
});

// Route to get a value by key from Redis
app.get('/get/:key', async (req, res) => {
    const { key } = req.params;
    try {
        const value = await client.get(key);
        if (value) {
            res.status(200).send(`Value for key "${key}": ${value}`);
        } else {
            res.status(404).send(`Key "${key}" not found`);
        }
    } catch (err) {
        res.status(500).send(`Error getting key "${key}": ${err.message}`);
    }
});

// Route to delete a key from Redis
app.delete('/del/:key', async (req, res) => {
    const { key } = req.params;
    try {
        await client.del(key);
        res.status(200).send(`Key "${key}" deleted successfully`);
    } catch (err) {
        res.status(500).send(`Error deleting key "${key}": ${err.message}`);
    }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### Explanation of the Code

1. **Import required modules**: Import `express` and `redis` modules.
2. **Create an Express application**: Use `express()` to create an instance of an Express application.
3. **Create a Redis client**: Use `redis.createClient()` to create a new Redis client instance.
4. **Handle Redis connection events**: Log messages when the Redis client connects or encounters an error.
5. **Connect to the Redis server**: Use `client.connect()` to establish the connection.
6. **Middleware to parse JSON bodies**: Use `express.json()` to parse JSON request bodies.
7. **Define routes**:
    - **POST /set**: Set a key-value pair in Redis.
    - **GET /get/**: Get a value by key from Redis.
    - **DELETE /del/**: Delete a key from Redis.
8. **Start the Express server**: Listen on a specified port for incoming requests.

### Step 2: Run the Application

Save the file and run it using Node.js:

```
node app.js
```

### Step 3: Test the API

You can use tools like `curl` or Postman to test the API endpoints.

### Set a Key-Value Pair

```
curl -X POST -H "Content-Type: application/json" -d '{"key":"name","value":"John Doe"}' http://localhost:3000/set
```

### Get a Value by Key

```
curl http://localhost:3000/get/name
```

### Delete a Key

```
curl -X DELETE http://localhost:3000/del/name
```

### Summary

- **Set up the Node.js environment**: Ensure Node.js is installed and initialize a new project.
- **Install necessary packages**: Use npm to install `express` and `redis`.
- **Create the Express application**: Set up Express and connect to the Redis server.
- **Define routes**: Create routes to set, get, and delete key-value pairs in Redis.
- **Run the application**: Start the Express server and test the API endpoints.

## How to build a basic express app that interacts with redis and kue

```jsx
// Import required modules
const express = require('express');
const redis = require('redis');
const kue = require('kue');

// Create an Express application
const app = express();

// Create a Redis client
const client = redis.createClient();

// Create a Kue queue
const queue = kue.createQueue();

// Handle Redis connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

// Middleware to parse JSON bodies
app.use(express.json());

// Route to set a key-value pair in Redis
app.post('/set', async (req, res) => {
    const { key, value } = req.body;
    try {
        await client.set(key, value);
        res.status(200).send(`Key "${key}" set successfully`);
    } catch (err) {
        res.status(500).send(`Error setting key "${key}": ${err.message}`);
    }
});

// Route to get a value by key from Redis
app.get('/get/:key', async (req, res) => {
    const { key } = req.params;
    try {
        const value = await client.get(key);
        if (value) {
            res.status(200).send(`Value for key "${key}": ${value}`);
        } else {
            res.status(404).send(`Key "${key}" not found`);
        }
    } catch (err) {
        res.status(500).send(`Error getting key "${key}": ${err.message}`);
    }
});

// Route to delete a key from Redis
app.delete('/del/:key', async (req, res) => {
    const { key } = req.params;
    try {
        await client.del(key);
        res.status(200).send(`Key "${key}" deleted successfully`);
    } catch (err) {
        res.status(500).send(`Error deleting key "${key}": ${err.message}`);
    }
});

// Route to create a job
app.post('/job', (req, res) => {
    const { title, email } = req.body;
    const job = queue.create('email', {
        title: title,
        email: email
    }).save((err) => {
        if (!err) {
            res.status(200).send(`Job created with ID: ${job.id}`);
        } else {
            res.status(500).send(`Error creating job: ${err.message}`);
        }
    });
});

// Process email jobs
queue.process('email', (job, done) => {
    sendEmail(job.data, done);
});

// Function to simulate sending an email
function sendEmail(data, done) {
    console.log(`Sending email to ${data.email} with title ${data.title}`);
    // Simulate async email sending with setTimeout
    setTimeout(() => {
        console.log('Email sent successfully');
        done();
    }, 1000);
}

// Handle job events
queue.on('job enqueue', (id, type) => {
    console.log(`Job ${id} got queued of type ${type}`);
}).on('job complete', (id, result) => {
    console.log(`Job ${id} completed with result ${result}`);
}).on('job failed', (id, errorMessage) => {
    console.log(`Job ${id} failed with error ${errorMessage}`);
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
```

### Explanation of the Code

1. **Import required modules**: Import `express`, `redis`, and `kue` modules.
2. **Create an Express application**: Use `express()` to create an instance of an Express application.
3. **Create a Redis client**: Use `redis.createClient()` to create a new Redis client instance.
4. **Create a Kue queue**: Use `kue.createQueue()` to create a new Kue queue instance.
5. **Handle Redis connection events**: Log messages when the Redis client connects or encounters an error.
6. **Connect to the Redis server**: Use `client.connect()` to establish the connection.
7. **Middleware to parse JSON bodies**: Use `express.json()` to parse JSON request bodies.
8. **Define routes**:
    - **POST /set**: Set a key-value pair in Redis.
    - **GET /get/**: Get a value by key from Redis.
    - **DELETE /del/**: Delete a key from Redis.
    - **POST /job**: Create a job in the Kue queue.
9. **Process jobs in the queue**: Use `queue.process('job_type', (job, done) => { ... })` to process jobs of the specified type.
10. **Simulate sending an email**: The `sendEmail` function simulates an asynchronous email sending operation using `setTimeout`.
11. **Handle job events**: Use `queue.on` to listen for various job events like enqueue, complete, and fail.
12. **Start the Express server**: Listen on a specified port for incoming requests.
