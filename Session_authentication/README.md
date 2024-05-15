## Background Context

In this project, you will implement a **Session Authentication**. You are not allowed to install any other module.

In the industry, you should **not** implement your own Session authentication system and use a module or framework that doing it for you (like in Python-Flask: [Flask-HTTPAuth](https://intranet.atlasschool.com/rltoken/X_Ss7um7S0h2y62_R5U5jQ)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources

**Read or watch**:

- [REST API Authentication Mechanisms - Only the session auth part](https://intranet.atlasschool.com/rltoken/vyJGpJSSrFRe0LuWasDqCQ)
- [HTTP Cookie](https://intranet.atlasschool.com/rltoken/Ry_Fo8MjzSa1KZ2nIijqOA)
- [Flask](https://intranet.atlasschool.com/rltoken/V0qd3lJG4kR_kwojoaFZng)
- [Flask Cookie](https://intranet.atlasschool.com/rltoken/sfyvsYn5YM2MDBUqyqnK-A)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/N7kCrbRr7O0pfv8oVVzynw), **without the help of Google**:

### General

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## What is authentication?

In the context of a REST API, authentication refers to the process of verifying the identity of clients or users who are accessing the API endpoints. It ensures that only authorized users or systems can interact with the API and access its resources.

Authentication mechanisms typically involve clients providing some form of credentials to the server, which are then validated to confirm the client's identity. Once authenticated, the client is granted access to the requested resources.

Authentication is essential for protecting sensitive data and preventing unauthorized access to API endpoints. It helps enforce access control policies and ensures that only authenticated users or applications can perform certain actions or access specific data within the API.

## What does session authentication mean?

Session authentication refers to a process where a user's identity is verified and maintained for the duration of their interaction with a system, typically a web application.

### Key Components of Session Authentication:

- **Authentication Credentials**: Information like username and password used for verifying the user's identity.
- **Session ID**: A unique identifier for the session, typically stored as a cookie in the user's browser.
- **Session Storage**: Server-side storage where session data is kept, such as user preferences, authentication status, and other session-specific information.
- **Cookies**: Small pieces of data stored on the client-side, often used to store the session ID.

### Benefits of Session Authentication:

- **State Management**: Allows the server to maintain user-specific data across multiple requests.
- **Security**: Properly implemented, it helps prevent unauthorized access and supports various security measures (e.g., secure cookies, HTTPS).
- **User Experience**: Provides a seamless user experience by keeping users logged in as they navigate through different parts of an application.

## What is a Cookie?

In the context of session authentication, a cookie is a small piece of data that a server sends to the user's web browser. The browser stores this data and sends it back to the server with subsequent requests. Cookies are used for various purposes, including session management, personalization, and tracking.

### Key Characteristics of Cookies:

1. **Name-Value Pairs**: Each cookie is a simple piece of text comprising a name and a value. For example: `sessionId=abc123`.
2. **Storage**: Cookies are stored on the user's device by the web browser. The storage location depends on whether the cookie is a session cookie or a persistent cookie:
    - **Session Cookies**: These are stored temporarily in the browser's memory and are deleted when the browser is closed.
    - **Persistent Cookies**: These are stored on the user's hard drive and remain there until they expire or are deleted by the user.
3. **Attributes**: Cookies can have various attributes that define their behavior:
    - **Domain and Path**: Specify which websites and paths the cookie is applicable to.
    - **Expiration Date**: Defines when the cookie will expire. If not set, the cookie will expire at the end of the session (i.e., when the browser is closed).
    - **Secure**: Indicates that the cookie should only be sent over secure (HTTPS) connections.
    - **HttpOnly**: Prevents client-side scripts from accessing the cookie, reducing the risk of cross-site scripting (XSS) attacks.

### Use of Cookies in Session Authentication:

- **Session ID Storage**: When a user logs into a web application, the server generates a unique session ID. This session ID is sent to the browser as a cookie.
- **Session Continuity**: For each subsequent request to the server, the browser sends the session cookie, allowing the server to recognize the user and maintain their session.
- **State Management**: Cookies help maintain user state, ensuring that the user does not need to re-authenticate on every request as they navigate through the web application.

![Screenshot 2024-05-15 102326](https://github.com/ericpo1sh/atlas-web_back_end/assets/126730794/6426efc6-272e-401b-a95c-40d8499c218e)

### Example of a Session Cookie:

When a user logs in, the server might respond with a header like this:

```python
Set-Cookie: sessionId=abc123; HttpOnly; Secure; Path=/; Domain=example.com
```

This instructs the browser to store a cookie named `sessionId` with the value `abc123`. The `HttpOnly` attribute ensures the cookie cannot be accessed via JavaScript, and the `Secure` attribute ensures it is only sent over HTTPS.

### Benefits of Using Cookies for Session Authentication:

- **User Experience**: Enhances user experience by allowing them to stay logged in as they navigate through different parts of the application.
- **State Persistence**: Helps in maintaining the state of the user’s interaction with the server.
- **Security**: Properly managed cookies can enhance security by restricting access and ensuring secure transmission.

## How to use Cookies in Flask (Sending/Parsing)

### 1. Setting Up Flask

First, ensure you have Flask installed. If not, install it using pip:
`pip install Flask`

### 2. Creating a Basic Flask Application

Create a simple Flask application in a file named `app.py`.

```python
from flask import Flask, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f'Hello, {username}!'
    return 'Hello, Guest!'

@app.route('/set_cookie/<username>')
def set_cookie(username):
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', username)
    return resp

@app.route('/clear_cookie')
def clear_cookie():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Running the Application

Run the Flask application: `python app.py`

## Explanation of app.py

### Setting a Cookie

In the `/set_cookie/<username>` route, we set a cookie named `username` with the value provided in the URL.

```python
@app.route('/set_cookie/<username>')
def set_cookie(username):
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', username)
    return resp
```

- `make_response()` is used to create a response object.
- `set_cookie()` method sets a cookie on the response object.
- The response then redirects to the index route.

### Reading a Cookie

In the `/` route, we read the `username` cookie.

```python
@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f'Hello, {username}!'
    return 'Hello, Guest!'
```

- `request.cookies.get('username')` retrieves the value of the `username` cookie.
- If the cookie exists, it greets the user by name; otherwise, it greets as a guest.

### Clearing a Cookie

In the `/clear_cookie` route, we clear the `username` cookie by setting its expiration date to the past.

```python
@app.route('/clear_cookie')
def clear_cookie():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    return resp
```

Setting `expires=0` effectively deletes the cookie.
