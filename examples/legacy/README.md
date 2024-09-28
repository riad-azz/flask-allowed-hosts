# Flask Allowed Hosts - Legacy Example

This project demonstrates how to enforce allowed hosts in a Flask application using the `flask_allowed_hosts` package.

In this example, the `limit_hosts` decorator is used to restrict access to specific endpoints based on the request's IP address. Hosts that are not on the allowed list will receive a custom error message.

## Usage

1. Install the necessary package:

   ```bash
   pip install flask-allowed-hosts
   ```

2. Start the Flask application by running:

   ```bash
   python main.py
   ```

3. Access the following endpoints using a browser or API client.

## Features

- **Host Validation**: The `limit_hosts` decorator checks the request's host IP against a pre-configured list (`ALLOWED_HOSTS`).
- **Custom Denied Response**: Requests from unallowed hosts will receive a 403 error with a custom JSON message.

## Endpoints

### `/` (GET)

- Returns a simple "Hello World!" message.

### `/api/greet` (GET)

- **Host Validation**: Restricted to IP addresses in `ALLOWED_HOSTS`.
- Accepts an optional query parameter `name`. Returns a JSON response greeting the user.

### `/api/greet/local` (GET)

- **Host Override**: This endpoint overrides the `ALLOWED_HOSTS` list and allows only `localhost` and `127.0.0.1` to access it.
- Accepts an optional query parameter `name` and returns a greeting override message.

## Custom Denial Message

If a request comes from an unallowed host, the API will return a JSON response:

```json
{
  "error": "Oops! looks like you are not allowed to access this page!"
}
```
