# Flask Allowed Hosts with Custom Error Page Example

This project demonstrates how to use the `flask_allowed_hosts` package in a Flask application to enforce allowed hosts
and redirect unauthorized requests to a custom error page.

In this example, the `limit` decorator is used to restrict access to specific endpoints based on the request's IP
address. If a request comes from an unallowed host, it is redirected to a custom error page.

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

- **Host Validation**: The `limit` decorator checks the request's host IP against a pre-configured
  list (`ALLOWED_HOSTS`).
- **Custom Denied Response**: Requests from unallowed hosts will be redirected to `/custom-error`.

## Endpoints

### `/` (GET)

- Returns a simple "Hello World!" message.

### `/custom-error` (GET)

- This is the custom error page where users are redirected if their IP is not in the allowed list. Displays an error
  message: "Oops! looks like you are not allowed to access this page!"

### `/api/greet` (GET)

- **Host Validation**: Restricted to IP addresses in `ALLOWED_HOSTS`.
- Accepts an optional query parameter `name`. Returns a JSON response greeting the user.

### `/api/greet/override` (GET)

- **Host Override**: This endpoint allows additional hosts like `localhost` and `127.0.0.1` to access it.
- Accepts an optional query parameter `name` and returns a greeting override message.

## Custom Denial Redirect

If a request comes from an unallowed host, the API will redirect the user to the `/custom-error` page.

