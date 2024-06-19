**Read or watch:**

- [Mocha documentation](https://intranet.atlasschool.com/rltoken/Ef-YqJk78G4D1zSJgCOKWw)
- [Chai](https://intranet.atlasschool.com/rltoken/1wz8FKPDf1mU9MFTBudqHA)
- [Sinon](https://intranet.atlasschool.com/rltoken/3wLyO0jXteoFaJAL3dQNNQ)
- [Express](https://intranet.atlasschool.com/rltoken/aVaeRQTkFcrLDTedHwJikw)
- [Request](https://intranet.atlasschool.com/rltoken/iDq7WAYaPp-sTdlSgPev3Q)
- [How to Test NodeJS Apps using Mocha, Chai](https://www.youtube.com/watch?v=M0UtmM1Rrpo&list=PLgbtO1Bcz4C-vU0JLfDBsZGbSUdNX4mQ8&index=2)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/4ZxwXNG7ByKjbq7VcQFc7Q), **without the help of Google**:

- How to use Mocha to write a test suite
- How to use different assertion libraries (Node or Chai)
- How to present long test suites
- When and how to use spies
- When and how to use stubs
- What are hooks and when to use them
- Unit testing with Async functions
- How to write integration tests with a small node server

## How to use Mocha to write a test suite

### Step 1: Install Mocha

First, you need to install Mocha. You can do this globally or locally to your project. It’s usually a good practice to install it locally.

```bash
# Initialize your project if you haven't already
npm init -y

# Install Mocha locally
npm install --save-dev mocha
```

### Step 2: Write Your Tests

Create a test file inside the `test` directory. For example, create `test/test.js`.

Here's a simple example of how to write tests using Mocha:

```jsx
// test/test.js

const assert = require('assert');

describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      assert.strictEqual([1, 2, 3].indexOf(4), -1);
    });

    it('should return the index when the value is present', function() {
      assert.strictEqual([1, 2, 3].indexOf(2), 1);
    });
  });
});
```

### Step 3: Use Assertions

In the example above, `assert` is used for assertions. Mocha supports various assertion libraries, including Node's built-in `assert` module, Chai, Should.js, and more. Here’s how you can use Chai:

1. Install Chai:

```bash
npm install --save-dev chai
```

1. Use Chai in your tests:

```jsx
// test/test.js

const chai = require('chai');
const expect = chai.expect;

describe('Array', function() {
  describe('#indexOf()', function() {
    it('should return -1 when the value is not present', function() {
      expect([1, 2, 3].indexOf(4)).to.equal(-1);
    });

    it('should return the index when the value is present', function() {
      expect([1, 2, 3].indexOf(2)).to.equal(1);
    });
  });
});
```

## How to present long test suites

### 1. Organize Tests by Feature or Module

Divide your tests into multiple files and directories based on features or modules. This keeps each test file manageable and logically grouped.

**Directory structure example:**

```bash
/test
  /auth
    login.test.js
    signup.test.js
  /profile
    profile.test.js
  utils.test.js
```

**Example: test/auth/login.test.js**

```jsx
const chai = require('chai');
const expect = chai.expect;

describe('Login', function() {
  it('should login with valid credentials', function() {
    // Test implementation
  });

  it('should fail with invalid credentials', function() {
    // Test implementation
  });
});
```

### 2. Use Descriptive Test Names

Use clear and descriptive names for your test cases and suites. This makes it easier to understand the purpose of each test at a glance.

```jsx
describe('User Authentication', function() {
  describe('Login Functionality', function() {
    it('should return a token for valid credentials', function() {
      // Test implementation
    });

    it('should return an error for invalid credentials', function() {
      // Test implementation
    });
  });

  describe('Signup Functionality', function() {
    it('should create a new user with valid details', function() {
      // Test implementation
    });

    it('should return an error for duplicate email', function() {
      // Test implementation
    });
  });
});
```

### 3. Use Before and After Hooks

Utilize Mocha’s hooks (`before`, `after`, `beforeEach`, `afterEach`) to set up and tear down common test preconditions. This avoids redundancy and keeps test cases focused.

**Example:**

```jsx
describe('Database Tests', function() {
  before(function() {
    // Code to connect to the database
  });

  after(function() {
    // Code to disconnect from the database
  });

  beforeEach(function() {
    // Code to reset database state before each test
  });

  it('should save a record to the database', function() {
    // Test implementation
  });

  it('should retrieve a record from the database', function() {
    // Test implementation
  });
});
```

### 4. Utilize Helper Functions

Extract common logic into helper functions to avoid duplication and make tests more readable.

**Example:**

```jsx
const { loginUser, createUser } = require('./helpers');

describe('User API', function() {
  it('should create a new user', async function() {
    const user = await createUser('test@example.com', 'password123');
    expect(user).to.have.property('id');
  });

  it('should login a user', async function() {
    const token = await loginUser('test@example.com', 'password123');
    expect(token).to.be.a('string');
  });
});
```

## When and how to use spies

### When to Use Spies

1. **Function Call Verification**: When you need to verify that a function was called or not called.
2. **Argument Verification**: When you need to check the arguments with which a function was called.
3. **Call Count Verification**: When you need to verify how many times a function was called.
4. **Context Verification**: When you need to ensure that a function was called in the correct context (`this` value).
5. **Behavior Testing**: When you want to test side effects without executing the actual implementation of a function.

### How to Use Spies

### Using Sinon.js with Mocha

Sinon.js is a popular library that provides spies, stubs, and mocks for JavaScript testing.

1. **Installation**
    
    First, install Sinon as a development dependency: `npm install --save-dev sinon` 
    
2. **Basic Usage**
    
    Here's a basic example of using Sinon spies with Mocha:
    
    ```jsx
    const sinon = require('sinon');
    const chai = require('chai');
    const expect = chai.expect;
    
    describe('User', function() {
      it('should call save method', function() {
        const user = {
          save: function() {}
        };
    
        const saveSpy = sinon.spy(user, 'save');
        user.save();
    
        expect(saveSpy.calledOnce).to.be.true;
      });
    
      it('should call save method with correct arguments', function() {
        const user = {
          save: function(name) {}
        };
    
        const saveSpy = sinon.spy(user, 'save');
        user.save('Alice');
    
        expect(saveSpy.calledWith('Alice')).to.be.true;
      });
    });
    ```
    
    **Advanced Usage**
    
    Spies can be used to test more complex scenarios, such as verifying the order of calls, the context, and the call count.
    
    ```jsx
    describe('User', function() {
      it('should call save method twice', function() {
        const user = {
          save: function() {}
        };
    
        const saveSpy = sinon.spy(user, 'save');
        user.save();
        user.save();
    
        expect(saveSpy.calledTwice).to.be.true;
      });
    
      it('should call save method with correct context', function() {
        const user = {
          name: 'Alice',
          save: function() {
            return this.name;
          }
        };
    
        const saveSpy = sinon.spy(user, 'save');
        const result = user.save();
    
        expect(saveSpy.calledOn(user)).to.be.true;
        expect(result).to.equal('Alice');
      });
    
      it('should call methods in correct order', function() {
        const user = {
          save: function() {},
          notify: function() {}
        };
    
        const saveSpy = sinon.spy(user, 'save');
        const notifySpy = sinon.spy(user, 'notify');
        user.save();
        user.notify();
    
        sinon.assert.callOrder(saveSpy, notifySpy);
      });
    });
    ```
    
    **Cleaning Up**
    
    When using spies, especially in a large test suite, it's important to clean up after each test to avoid side effects. Sinon provides `sinon.restore()` for this purpose.
    
    ```jsx
    describe('User', function() {
      let saveSpy;
    
      beforeEach(function() {
        saveSpy = sinon.spy(user, 'save');
      });
    
      afterEach(function() {
        saveSpy.restore();
      });
    
      it('should call save method', function() {
        user.save();
        expect(saveSpy.calledOnce).to.be.true;
      });
    });
    ```
    
    ## When and how to use stubs
    
    ### When to Use Stubs
    
    1. **Isolating Tests**: When you need to isolate the code under test from its dependencies.
    2. **Simulating Behavior**: When you need to simulate various behaviors or return values from functions (e.g., success and error cases).
    3. **Avoiding Side Effects**: When you need to avoid the side effects of certain operations (e.g., network requests, file system operations).
    4. **Controlling Dependencies**: When you need to control and verify the behavior of a dependency that your unit of code interacts with.
    
    **Basic Usage**
    
    Here’s how to create and use stubs in your tests:
    
    ```jsx
    const sinon = require('sinon');
    const chai = require('chai');
    const expect = chai.expect;
    
    describe('User', function() {
      it('should call save method and return success', function() {
        const user = {
          save: sinon.stub().returns('success')
        };
    
        const result = user.save();
        expect(result).to.equal('success');
        expect(user.save.calledOnce).to.be.true;
      });
    
      it('should call save method and throw error', function() {
        const user = {
          save: sinon.stub().throws(new Error('Save failed'))
        };
    
        expect(() => user.save()).to.throw('Save failed');
        expect(user.save.calledOnce).to.be.true;
      });
    });
    ```
    
    ## What are hooks and when to use them
    
    In Mocha, hooks are special functions that run at specific times during the test lifecycle. They allow you to set up preconditions, perform cleanup, and manage test environments efficiently. The primary hooks provided by Mocha are `before`, `after`, `beforeEach`, and `afterEa`
    
    ### Types of Hooks and Their Usage
    
    1. **`before` Hook**
        
        Runs once before all tests in a `describe` block. Useful for setting up global preconditions or initializing data that is needed for all tests.
        
        ```jsx
        describe('User Tests', function() {
          before(function() {
            // Code to run before all tests
            console.log('Setting up before all tests');
          });
        
          it('should test something', function() {
            // Test implementation
          });
        });
        ```
        
    2. **`after` Hook**
        
        Runs once after all tests in a `describe` block. Useful for cleaning up resources or data that were initialized in the `before` hook.
        
        ```jsx
        describe('User Tests', function() {
          after(function() {
            // Code to run after all tests
            console.log('Cleaning up after all tests');
          });
        
          it('should test something', function() {
            // Test implementation
          });
        });
        ```
        
    3. **`beforeEach` Hook**
        
        Runs before each test in a `describe` block. Useful for setting up state or data needed for each individual test.
        
        ```jsx
        describe('User Tests', function() {
          beforeEach(function() {
            // Code to run before each test
            console.log('Setting up before each test');
          });
        
          it('should test something', function() {
            // Test implementation
          });
        
          it('should test something else', function() {
            // Another test implementation
          });
        });
        ```
        
    4. **`afterEach` Hook**
        
        Runs after each test in a `describe` block. Useful for resetting state or cleaning up data after each test runs.
        
        ```jsx
        describe('User Tests', function() {
          afterEach(function() {
            // Code to run after each test
            console.log('Cleaning up after each test');
          });
        
          it('should test something', function() {
            // Test implementation
          });
        
          it('should test something else', function() {
            // Another test implementation
          });
        });
        ```
        
    
    ### **When to Use Hooks**
    
    1. **Setting Up and Tearing Down Test Environments**
        
        Use `before` and `after` hooks to set up and tear down test environments or global states that are shared across tests.
        
        ```jsx
        describe('Database Tests', function() {
          before(function() {
            // Connect to the database
            console.log('Connecting to the database');
          });
        
          after(function() {
            // Disconnect from the database
            console.log('Disconnecting from the database');
          });
        
          it('should retrieve data', function() {
            // Test implementation
          });
        });
        ```
        
    2. **Preparing and Cleaning Up Test Data**
        
        Use `beforeEach` and `afterEach` hooks to prepare and clean up test data for each test case.
        
        ```jsx
        describe('User API', function() {
          beforeEach(function() {
            // Create a new user before each test
            console.log('Creating a new user');
          });
        
          afterEach(function() {
            // Delete the user after each test
            console.log('Deleting the user');
          });
        
          it('should fetch the user', function() {
            // Test implementation
          });
        
          it('should update the user', function() {
            // Another test implementation
          });
        });
        ```
        
    3. **Mocking and Stubbing Dependencies**
        
        Use hooks to set up and tear down mocks and stubs for dependencies, ensuring that tests are isolated and do not affect each other.
        
        ```jsx
        const sinon = require('sinon');
        
        describe('Notification Service', function() {
          let sendEmailStub;
        
          beforeEach(function() {
            sendEmailStub = sinon.stub(notificationService, 'sendEmail').returns(true);
          });
        
          afterEach(function() {
            sendEmailStub.restore();
          });
        
          it('should send an email', function() {
            // Test implementation
          });
        
          it('should not send an email on error', function() {
            // Another test implementation
          });
        });
        ```
        
    4. **Shared Setup Logic**
        
        Use hooks to run shared setup logic that multiple tests rely on, reducing redundancy and keeping tests DRY (Don't Repeat Yourself).
        
        ```jsx
        describe('E-commerce Application', function() {
          let product;
        
          beforeEach(function() {
            // Set up a new product before each test
            product = { name: 'Laptop', price: 999 };
          });
        
          it('should add the product to the cart', function() {
            // Test implementation
          });
        
          it('should remove the product from the cart', function() {
            // Another test implementation
          });
        });
        ```
        

## Unit testing with Async functions

Unit testing asynchronous functions can be more challenging than testing synchronous ones, but it is crucial for ensuring that your code behaves correctly in real-world scenarios. Mocha, along with assertion libraries like Chai, provides good support for testing asynchronous code.

### Strategies for Testing Async Functions

1. **Using Callbacks**
2. **Returning Promises**
3. **Using `async`/`await`**

### 1. Using Callbacks

When testing functions that use callbacks, you need to signal to Mocha that your test is complete by calling the `done` callback.

**Example:**

```jsx
const chai = require('chai');
const expect = chai.expect;

// Example async function using a callback
function fetchData(callback) {
  setTimeout(() => {
    callback(null, 'data');
  }, 1000);
}

describe('fetchData', function() {
  it('should fetch data', function(done) {
    fetchData((err, data) => {
      expect(data).to.equal('data');
      done();
    });
  });
});
```

### 2. Returning Promises

Mocha recognizes if a test returns a promise and will wait for it to resolve. This makes testing promises straightforward.

**Example:**

```jsx
const chai = require('chai');
const expect = chai.expect;

// Example async function returning a promise
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('data');
    }, 1000);
  });
}

describe('fetchData', function() {
  it('should fetch data', function() {
    return fetchData().then((data) => {
      expect(data).to.equal('data');
    });
  });

  it('should fetch data using async/await', async function() {
    const data = await fetchData();
    expect(data).to.equal('data');
  });
});
```

### 3. Using `async`/`await`

Using `async`/`await` can make your tests more readable and maintainable. Mocha fully supports `async` functions.

**Example:**

```jsx
const chai = require('chai');
const expect = chai.expect;

// Example async function
async function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('data');
    }, 1000);
  });
}

describe('fetchData', function() {
  it('should fetch data', async function() {
    const data = await fetchData();
    expect(data).to.equal('data');
  });

  it('should handle errors', async function() {
    async function fetchDataWithError() {
      return new Promise((_, reject) => {
        setTimeout(() => {
          reject(new Error('error occurred'));
        }, 1000);
      });
    }

    try {
      await fetchDataWithError();
    } catch (error) {
      expect(error.message).to.equal('error occurred');
    }
  });
});
```

## How to write integration tests with a small node server

Integration testing ensures that various components of your application work together as expected. When testing a Node.js server, integration tests often involve making HTTP requests to the server and verifying the responses.

### Setting Up a Small Node.js Server

First, let's set up a small Node.js server using Express. Then we'll write integration tests for this server.

1. **Install Dependencies**
    
    You will need Express, Mocha, Chai, and Supertest (a library for testing HTTP servers).
    `npm install express mocha chai supertest --save-dev`
    
2. **Create the Server**
    
    Create a file called `server.js`:
    
    ```jsx
    const express = require('express');
    const app = express();
    
    app.use(express.json());
    
    app.get('/hello', (req, res) => {
      res.send('Hello, world!');
    });
    
    app.post('/echo', (req, res) => {
      res.json({ message: req.body.message });
    });
    
    const port = process.env.PORT || 3000;
    app.listen(port, () => {
      console.log(`Server is running on port ${port}`);
    });
    
    module.exports = app; // Export the app for testing
    ```
    
    ### Writing Integration Tests
    
    1. **Set Up the Test Environment**
        
        Create a folder named `test` and a file called `integration.test.js` inside it.
        
    2. **Writing Tests with Mocha, Chai, and Supertest**
        
        In `integration.test.js`, write the following code:
        
        ```jsx
        const chai = require('chai');
        const chaiHttp = require('chai-http');
        const app = require('../server');
        const expect = chai.expect;
        
        chai.use(chaiHttp);
        
        describe('Integration Tests', function() {
          describe('GET /hello', function() {
            it('should return Hello, world!', function(done) {
              chai.request(app)
                .get('/hello')
                .end((err, res) => {
                  expect(res).to.have.status(200);
                  expect(res.text).to.equal('Hello, world!');
                  done();
                });
            });
          });
        
          describe('POST /echo', function() {
            it('should return the same message in the response', function(done) {
              const message = { message: 'Hello, Echo!' };
              chai.request(app)
                .post('/echo')
                .send(message)
                .end((err, res) => {
                  expect(res).to.have.status(200);
                  expect(res.body).to.have.property('message').eql('Hello, Echo!');
                  done();
                });
            });
          });
        });
        ```
