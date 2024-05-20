## Resources

**Read or watch:**

- [Flask documentation](https://intranet.atlasschool.com/rltoken/T03S8hNvX_1hXW66qK0Z6w)
- [Requests module](https://intranet.atlasschool.com/rltoken/nf0Y9myaDn6kIJckvB9E4w)
- [HTTP status codes](https://intranet.atlasschool.com/rltoken/a_OTic47lD-ZhoWKIGINBw)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/PTIhFapJKLUJ76WnfXonkQ), **without the help of Google**:

- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request form data
- How to return various HTTP status codes

## How do you declare API routes in a Flask App?

### Define API Routes

Use the `@app.route` decorator to define your API routes. You can specify the URL pattern and the HTTP methods the route should handle. Here’s an example with a few routes:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Define a route for GET requests
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"key": "value", "foo": "bar"}
    return jsonify(sample_data)

# Define a route for POST requests
@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify({"message": "Data received", "data": new_data}), 201

# Define a route with a variable URL
@app.route('/api/data/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = {"id": item_id, "name": f"Item {item_id}"}
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation of the Example

1. **Home Route (`/`)**: This route returns a simple welcome message.
2. **GET `/api/data`**: This route handles GET requests and returns a JSON response with some sample data.
3. **POST `/api/data`**: This route handles POST requests, receives JSON data from the client, and returns a confirmation message with the received data.
4. **GET `/api/data/<int:item_id>`**: This route includes a variable part in the URL (`<int:item_id>`). It captures the `item_id` from the URL, processes it, and returns a JSON response with the item details.

### **Handling Different HTTP Methods**

You can specify which HTTP methods a route should accept by using the `methods` parameter in the `@app.route` decorator. For example:

```python
@app.route('/api/resource', methods=['GET', 'POST'])
def handle_resource():
    if request.method == 'GET':
        return jsonify({"message": "GET request"})
    elif request.method == 'POST':
        return jsonify({"message": "POST request"})
```

### **Flask Request and Response**

- **`request`**: Use `request` to access the incoming request data. For example, `request.json` retrieves JSON data sent in a POST request.
- **`jsonify`**: Use `jsonify` to create a JSON response. Flask converts the dictionary to a JSON response automatically.

## **Setting Cookies**

To set a cookie, you need to create a response object and use its `set_cookie` method. Here's an example:

```python
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/set-cookie')
def set_cookie():
    response = make_response(jsonify({"message": "Cookie has been set"}))
    response.set_cookie('my_cookie', 'cookie_value', max_age=60*60*24)  # Cookie expires in one day
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

- The `set_cookie` route creates a response using `make_response`.
- `response.set_cookie('my_cookie', 'cookie_value', max_age=60*60*24)` sets a cookie named `my_cookie` with the value `cookie_value` that expires in one day (specified in seconds).

## **Getting Cookies**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-cookie')
def get_cookie():
    cookie_value = request.cookies.get('my_cookie')
    if cookie_value:
        return jsonify({"message": f"Cookie value: {cookie_value}"})
    else:
        return jsonify({"message": "No cookie found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

- The `get_cookie` route retrieves the cookie value using `request.cookies.get('my_cookie')`.
- It checks if the cookie exists and returns its value. If the cookie is not found, it returns a 404 status with an appropriate message.

## Retrieving request form data

In Flask, you can retrieve form data sent in an HTTP POST request using the `request` object. The `request.form` attribute provides access to the form data as a dictionary.

```python
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')

    # Process the data or return a response
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    return jsonify({"name": name, "email": email})
```

1. **`request.form`**: This is a dictionary-like object that contains the form data sent in the POST request. You can access form fields using `request.form.get('field_name')`.
2. **Error Handling**: The example checks if the `name` and `email` fields are provided. If not, it returns a JSON response with an error message and a 400 status code.
3. **Response**: The form data is returned as a JSON response for demonstration purposes.

## Returning various HTTP status codes

In Flask, you can return various HTTP status codes by including them in the response tuple or by using the `make_response` function. The simplest way to return a status code along with your response is to use a tuple, where the first element is the response data and the second element is the status code.

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/success')
def success():
    return jsonify({"message": "Success"}), 200

@app.route('/created')
def created():
    return jsonify({"message": "Resource created"}), 201

@app.route('/bad-request')
def bad_request():
    return jsonify({"error": "Bad request"}), 400

@app.route('/unauthorized')
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401

@app.route('/forbidden')
def forbidden():
    return jsonify({"error": "Forbidden"}), 403

@app.route('/not-found')
def not_found():
    return jsonify({"error": "Not found"}), 404

@app.route('/internal-server-error')
def internal_server_error():
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Common HTTP Status Codes

Here are some common HTTP status codes you might use:

- **200 OK**: The request was successful.
- **201 Created**: The request was successful and a resource was created.
- **204 No Content**: The request was successful but there is no content to return.
- **400 Bad Request**: The request could not be understood or was missing required parameters.
- **401 Unauthorized**: Authentication failed or user does not have permissions for the desired action.
- **403 Forbidden**: Authentication succeeded but authenticated user does not have access to the requested resource.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.
