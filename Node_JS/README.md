## Resources

**Read or watch**:

- [Node JS getting started](https://intranet.atlasschool.com/rltoken/9WlTQzMdmP4OTPlLkTWC7A)
- [Process API doc](https://intranet.atlasschool.com/rltoken/Zyrw_4wpEnRIZr9XcfmJgg)
- [Child process](https://intranet.atlasschool.com/rltoken/8rwdLS4ysWLsBriObByWYQ)
- [Express getting started](https://intranet.atlasschool.com/rltoken/T8esFM9ydZBeuzO-S63VTA)
- [Mocha documentation](https://intranet.atlasschool.com/rltoken/wvYeeqR0_yn096Ah9d6NGw)
- [Nodemon documentation](https://intranet.atlasschool.com/rltoken/d9OSq6Ewww7BuQ__uaxCYg)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/RPNxm64HnUsFD2SSR2IDww), **without the help of Google**:

- run javascript using NodeJS
- use NodeJS modules
- use specific Node JS module to read files
- use `process` to access command line arguments and the environment
- create a small HTTP server using Node JS
- create a small HTTP server using Express JS
- create advanced routes with Express JS
- use ES6 with Node JS with Babel-node
- use Nodemon to develop faster

# [Introduction to Node.js](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs#introduction-to-nodejs)

Node.js is a runtime environment that allows you to run JavaScript on the server side. Traditionally, JavaScript was primarily used for client-side scripting in web browsers. Node.js extends the capabilities of JavaScript to the server, enabling developers to build scalable and efficient backend services.

### Key Features of Node.js:

1. **Event-Driven Architecture**:
    - Node.js uses an event-driven, non-blocking I/O model which makes it lightweight and efficient. This is ideal for applications that need to handle a large number of simultaneous connections with high throughput.
2. **Non-Blocking I/O**:
    - The non-blocking I/O model means that Node.js can handle multiple operations concurrently without waiting for any single operation to complete. This leads to high performance and scalability.
3. **Single Programming Language**:
    - With Node.js, you can use JavaScript for both frontend and backend development, which can streamline the development process and make it easier to maintain the codebase.
4. **Package Manager (npm)**:
    - Node.js comes with npm (Node Package Manager), which is the largest ecosystem of open-source libraries. It allows developers to easily share and reuse code, speeding up the development process.
5. **Rich Ecosystem**:
    - Node.js has a vast ecosystem with numerous libraries and frameworks (like Express.js, Koa.js) that help in building a variety of applications, from simple web servers to complex APIs and microservices.

### Use Cases of Node.js:

1. **Web Servers and APIs**:
    - Node.js is commonly used to build web servers and RESTful APIs due to its asynchronous nature and ability to handle many requests simultaneously.
2. **Real-Time Applications**:
    - Applications that require real-time data processing, such as chat applications, online gaming, and live streaming, benefit from Node.js's event-driven architecture.
3. **Microservices Architecture**:
    - Node.js is well-suited for microservices architecture, where applications are broken down into smaller, independent services that communicate with each other.
4. **Server-Side Rendering**:
    - Node.js can be used for server-side rendering of web applications, which can improve performance and SEO for single-page applications (SPAs).
5. **Command-Line Tools**:
    - Node.js is also used to build command-line tools and scripts for automation and other purposes.

### Basic Example:

Here’s a simple example of a web server written in Node.js:

```jsx
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

This code creates a basic HTTP server that listens on `localhost` at port `3000` and responds with "Hello, World!" to any incoming request.

## How to use NodeJS modules

Using Node.js modules is fundamental to structuring and organizing your application code. Node.js modules allow you to encapsulate and reuse code across different parts of your application or even across different projects. Here’s a step-by-step guide on how to use Node.js modules effectively:

### 1. Built-in Modules

Node.js comes with several built-in modules that you can use without any additional installation. Examples include `http`, `fs` (file system), `path`, `os`, and many more.

**Example: Using the `http` module to create a simple server:**

```jsx
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

### 2. External Modules

You can also use modules from the npm (Node Package Manager) ecosystem. To use an npm module, you first need to install it using the `npm install` command.

**Example: Using the `express` module to create a web server:**

1. Initialize your project if you haven’t already:
    
    `npm init -y`
    
2. Install the `express` module:
`npm install express`
3. Create a simple Express server:

```jsx
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
```

### 3. Creating Custom Modules

You can create your own modules to organize your code. A module in Node.js is just a JavaScript file. You can export functionality from a module using `module.exports` or `exports` and import it using `require`.

**Example: Creating and using a custom module:**

1. Create a file named `math.js`:

```jsx
// math.js
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add,
  subtract
};
```

Use the custom module in another file, say `app.js`:

```jsx
// app.js
const math = require('./math');

console.log(math.add(5, 3));       // Output: 8
console.log(math.subtract(5, 3));  // Output: 2
```

## How to use specific Node JS module to read files

### Using the `fs` Module

First, you need to require the `fs` module in your Node.js script:

`const fs = require('fs');`

### Asynchronous File Reading

Asynchronous methods are non-blocking, meaning the rest of your code can continue executing while the file is being read.

**Example: Asynchronously reading a file:**

```jsx
const fs = require('fs');

// Asynchronously read the contents of the file
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err);
    return;
  }
  console.log('File contents:', data);
});
```

## How to access command line arguments and the environment

In Node.js, you can use the `process` object to access command line arguments and environment variables. The `process` object is a global object in Node.js and provides various properties and methods that allow you to interact with the current Node.js process.

### Accessing Command Line Arguments

Command line arguments passed to a Node.js script are available in the `process.argv` array. The first two elements in this array are:

1. The path to the Node.js executable.
2. The path to the JavaScript file being executed.

Any additional command line arguments start from the third element (index 2).

**Example: Accessing command line arguments:**

```jsx
// Accessing command line arguments
const args = process.argv;

// The first two elements are the node executable and the script path
console.log('Node.js executable:', args[0]);
console.log('Script path:', args[1]);

// Additional arguments start from index 2
const userArgs = args.slice(2);
console.log('User arguments:', userArgs);
```

**Output:**

```jsx
Node.js executable: /usr/local/bin/node
Script path: /path/to/script.js
User arguments: [ 'arg1', 'arg2', 'arg3' ]
```

## How to create advanced routes with Express JS

Creating advanced routes with Express.js involves setting up different endpoints and handling various HTTP methods (GET, POST, PUT, DELETE, etc.) for each route. Express.js is a web application framework for Node.js that makes it easy to build robust web applications and APIs.

### Creating Advanced Routes

Here’s an example of how to create and manage advanced routes in Express.js.

1. **Basic Route**:
Define a simple GET route:
    
    ```jsx
    app.get('/', (req, res) => {
      res.send('Hello, World!');
    });
    ```
    
2. **Route Parameters**:
Define a route with route parameters:
    
    ```jsx
    app.get('/users/:userId', (req, res) => {
      const userId = req.params.userId;
      res.send(`User ID: ${userId}`);
    });
    ```
    
3. **Query Parameters**:
Access query parameters in a route:
    
    ```jsx
    app.get('/search', (req, res) => {
      const query = req.query.q;
      res.send(`Search query: ${query}`);
    })
    ```
    
4. **Handling Different HTTP Methods**:
Define routes for different HTTP methods:
    
    ```jsx
    app.post('/users', (req, res) => {
      // Handle creating a new user
      res.send('User created');
    });
    
    app.put('/users/:userId', (req, res) => {
      // Handle updating user with userId
      res.send(`User ${req.params.userId} updated`);
    });
    
    app.delete('/users/:userId', (req, res) => {
      // Handle deleting user with userId
      res.send(`User ${req.params.userId} deleted`);
    });
    ```
