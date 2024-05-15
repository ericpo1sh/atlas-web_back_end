# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)


## Resources

**Read or watch**:

- [REST API Authentication Mechanisms](https://intranet.atlasschool.com/rltoken/Kb7ELziV7EkpqtPTUXY2ZQ)
- [Base64 in Python](https://intranet.atlasschool.com/rltoken/ENKa96b6goJUM4nm_unPqw)
- [HTTP header Authorization](https://intranet.atlasschool.com/rltoken/liL0xdWlzf5sweZyTEc4_w)
- [Flask](https://intranet.atlasschool.com/rltoken/XTf6irC31_V8bIKKhRE5AA)
- [Base64 - concept](https://intranet.atlasschool.com/rltoken/97wy7KWBzuiVkbKOSDUzng)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/cJmYXZqDAUuOvTffnjeRng), **without the help of Google**:

### General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

## What is authentication?

In the context of a REST API, authentication refers to the process of verifying the identity of clients or users who are accessing the API endpoints. It ensures that only authorized users or systems can interact with the API and access its resources.

Authentication mechanisms typically involve clients providing some form of credentials to the server, which are then validated to confirm the client's identity. Once authenticated, the client is granted access to the requested resources.

Authentication is essential for protecting sensitive data and preventing unauthorized access to API endpoints. It helps enforce access control policies and ensures that only authenticated users or applications can perform certain actions or access specific data within the API.

### Common methods of authentication in REST APIs include:

- **HTTP Basic Authentication**: This method involves sending the username and password with every request. The credentials are encoded with Base64 and included in the `Authorization` header of the HTTP request. While easy to implement, it's not very secure as credentials are sent in plaintext unless used over HTTPS. When encoding into Base64, the Security is not the intent of the encoding step. Rather, the intent of encoding is to encode non-HTTP-compatible characters that may be in the user’s username or password into those that are HTTP-compatible.

- **HTTP Digest Authentication**: Similar to Basic Authentication, but more secure as it sends hashed credentials. However, it's still vulnerable to man-in-the-middle attacks.

- **Token-Based Authentication (JWT)**: JSON Web Tokens (JWT) are a popular method for authentication. Upon successful login, the server issues a token that is signed and sent to the client. The client includes this token in the `Authorization` header for subsequent requests. JWTs are self-contained and can contain user information and expiration time.

- **OAuth 2.0**: OAuth 2.0 is a framework for token-based authentication that allows third-party applications to obtain limited access to a web service. It's commonly used for authentication and authorization in web and mobile applications.

## What is Base64?

Base64 is a binary-to-text encoding scheme that represents binary data (such as images, files, or binary data) in an ASCII string format. It's commonly used to encode binary data for transmission over text-based protocols, such as email or HTTP, where binary data may not be reliably transmitted.

## How can you encode a string into Base64?

In Python, you can encode a string into Base64 using the `base64` module, which provides functions for encoding and decoding data in Base64 format. Here's how you can encode a string:

```python
import base64

# Original string
original_string = "Hello, World!"

# Encode the string into Base64
encoded_bytes = base64.b64encode(original_string.encode())

# Convert the bytes-like object to a string
encoded_string = encoded_bytes.decode()

print("Base64 encoded string:", encoded_string)
```
