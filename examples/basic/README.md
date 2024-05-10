
# Flask Allowed Hosts Example

This example demonstrates how to use the `flask_allowedhosts` package to enforce allowed hosts for a Flask API endpoint.

The `limit_hosts` decorator is applied to the `/api/greet` endpoint, which ensures that requests are only allowed from specified hosts.

## Usage

- Start the Flask application using `python basic_example.py`.
- Access the `/api/greet` endpoint using a browser or API client.
- The `limit_hosts` decorator will validate the request host against the `allowed_hosts` list.
- If the host is in the allowed list, the API endpoint will return a greeting with the provided name.
- If the host is not in the allowed list, a 403 Forbidden error will be returned.

### Attributes

- `ALLOWED_HOSTS` (list): A list of allowed hosts in the format 'host:port'. Modify this list to include the allowed hosts.

### Endpoints

- `/api/greet`: The API endpoint that requires host validation. It accepts a query parameter `name` and returns a JSON response with a greeting.

### Note

- Ensure that the `flask-allowedhosts` package is installed (`pip install flask-allowedhosts`) to use the `limit_hosts` decorator.

- The `host` parameter in `app.run()` is set to `'0.0.0.0'` to make the application externally accessible. Modify it as needed.
