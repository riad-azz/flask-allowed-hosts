# Flask Allowed Hosts

This extension provides a way to restrict access to your Flask application based on the incoming request's hostname or
IP address or IP address range (network).

## Features

- Per-route configuration options.
- Customize denied access behavior.
- Two usage options: class-based or decorator-based.
- Restrict access by hostname, IP address or IP address range (network).

## Installation

Install the package using pip:

```cmd
pip install flask-allowed-hosts
```

## Usage

### Class-Based Usage

1. Initialize the `AllowedHosts` class.
2. Define allowed hosts (optional).
3. Define a function for denied access behavior (optional).
4. Apply access control to routes using `@allowed_hosts.limit()` decorator (optional).

#### Example:

```python
from flask import Flask, jsonify, abort
from flask_allowed_hosts import AllowedHosts

app = Flask(__name__)

ALLOWED_HOSTS = ["93.184.215.14", "api.example.com"]


def custom_on_denied():
    error = {"error": "Oops! Looks like you are not allowed to access this page!"}
    return jsonify(error), 403


allowed_hosts = AllowedHosts(app, allowed_hosts=ALLOWED_HOSTS, on_denied=custom_on_denied)


# Allows all incoming requests
@app.route("/api/public", methods=["GET"])
def public_endpoint():
    data = {"message": "This is public!"}
    return jsonify(data), 200


# Only allows incoming requests from "93.184.215.14" and "api.example.com"
@app.route("/api/private", methods=["GET"])
@allowed_hosts.limit()
def private_endpoint():
    data = {"message": "This is private!"}
    return jsonify(data), 200


# We can override the allowed_hosts list and the on_denied function for each route
@app.route("/api/private/secret", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["127.0.0.1"], on_denied=lambda: abort(404))
def secret_private_endpoint():
    data = {"message": "This is very private!"}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Decorator-Based Usage (Legacy)

**Warning**: This approach might cause unexpected behavior when combined with the class-based usage.

1. Define allowed hosts (optional).
2. Define a function for denied access behavior (optional).
3. Apply access control to routes using `@limit_hosts` decorator.

#### Example:

```python
from flask import Flask, jsonify
from flask_allowed_hosts import limit_hosts

app = Flask(__name__)

ALLOWED_HOSTS = ["93.184.215.14", "api.example.com"]


def custom_on_denied():
    error = {"error": "Custom Denied Response"}
    return jsonify(error), 403


# Allows all incoming requests
@app.route("/api/public", methods=["GET"])
def public_endpoint():
    data = {"message": "This is public!"}
    return jsonify(data), 200


# Only allows incoming requests from "93.184.215.14" and "api.example.com"
@app.route("/api/private", methods=["GET"])
@limit_hosts(allowed_hosts=ALLOWED_HOSTS, on_denied=custom_on_denied)
def private_endpoint():
    return jsonify({"message": "This is private!"}), 200
```

### More Examples

You can find more examples in
the [examples directory](https://github.com/riad-azz/flask-allowed-hosts/tree/main/examples).

## Configuration

### Initialization Parameters

- `app`: The Flask application instance (optional).
- `allowed_hosts`: List of allowed hosts (optional, defaults to `None` which allows all hosts).
- `on_denied`: Function for denied access behavior (optional).

### Flask Config and Environment Variables

#### Flask Configuration

The extension respects these configurations:

- `ALLOWED_HOSTS`: List of allowed hosts in Flask config.
- `ALLOWED_HOSTS_ON_DENIED`: Function for denied access behavior in Flask config.

**Precedence**: Values provided during initialization override Flask config values.

#### Environment Variables

You can enable debug mode by setting the `ALLOWED_HOSTS_DEBUG` environment variable to `True`:

```shell
export ALLOWED_HOSTS_DEBUG="True"
```

This will print helpful debug messages to the console.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you have any questions or feedback, please feel free
to [open an issue or a pull request](https://github.com/riad-azz/flask-allowed-hosts/issues).

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details.
