from flask import Flask, request, jsonify
from flask_allowedhosts import check_host

"""
Flask Allowed Hosts Example

This example demonstrates how to use the `flask_allowedhosts` package to enforce allowed hosts for a Flask API endpoint.

The `check_host` decorator is applied to the `/api` endpoint, which ensures that requests are only allowed from specified hosts.

Usage:
- Start the Flask application using `python basic_example.py`.
- Access the `/api` endpoint using a browser or API client.
- The `check_host` decorator will validate the request host against the `allowed_hosts` list.
- If the host is in the allowed list, the API endpoint will return a greeting with the provided name.
- If the host is not in the allowed list, a 403 Forbidden error will be returned.

Attributes:
- `ALLOWED_HOSTS` (list): A list of allowed hosts in the format 'host:port'. Modify this list to include the allowed hosts.

Endpoints:
- `/api`: The API endpoint that requires host validation. It accepts a query parameter `name` and returns a JSON response with a greeting.

Note:
- Ensure that the `flask-allowedhosts` package is installed (`pip install flask-allowedhosts`) to use the `check_host` decorator.
- The `host` parameter in `app.run()` is set to `'0.0.0.0'` to make the application externally accessible. Modify it as needed.
"""

app = Flask(__name__)

ALLOWED_HOSTS = ['127.0.0.1:5000', 'localhost:5000']

@app.route("/api")
@check_host(allowed_hosts=ALLOWED_HOSTS)
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)