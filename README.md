# Flask Allowed Hosts

Flask Allowed Hosts is a Flask extension that provides validation for both hostnames and IP addresses for API endpoints.
It enforces access restrictions, allowing only requests from specified hosts or IPs, an additional layer
of security to your Flask application.

While CORS is effective in browsers for preventing unauthorized origins, it does not protect against non-browser
requests. This package addresses that limitation by permitting access only to the hostnames and IPs listed in the
allowed_hosts, effectively limiting access to your API from unknown sources.

> [!CAUTION]
> the limit only applies to routes that have been decorated with `@allowed_hosts.limit` or `@limit_hosts` in
> your application other routes will not be restricted by default.

## Installation

Install the package using pip:

```cmd
pip install flask-allowed-hosts
```

## Getting Started

To limit access to your routes using `flask-allowed-hosts`:

### Basic usage of the `limit` decorator:

Here’s how to set up host validation for a basic endpoint:

```python
from flask import Flask, request, jsonify
from flask_allowed_hosts import AllowedHosts

ALLOWED_HOSTS = ["123.123.123.123", "321.321.321.321"]


# Returns a json response if the request IP is not in the allowed hosts
def on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


app = Flask(__name__)
allowed_hosts = AllowedHosts(app, allowed_hosts=ALLOWED_HOSTS, on_denied=on_denied)


@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit()
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Overriding the `allowed_hosts` or `on_denied` parameters for a specific route:

You can override the `allowed_hosts` or `on_denied` parameters for specific routes like this:

```python
from flask import Flask, request, jsonify
from flask_allowed_hosts import AllowedHosts

ALLOWED_HOSTS = ["123.123.123.123", "321.321.321.321"]


# Returns a json response if the request IP is not in the allowed hosts
def on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


app = Flask(__name__)
allowed_hosts = AllowedHosts(app, allowed_hosts=ALLOWED_HOSTS, on_denied=on_denied)


@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["127.0.0.1", "localhost"])
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Using the legacy `limit_hosts` decorator:

If you prefer to use the legacy `limit_hosts` decorator, you can do so as follows:

```python
from flask import Flask, request, jsonify
from flask_allowed_hosts import limit_hosts

ALLOWED_HOSTS = ["123.123.123.123", "321.321.321.321"]


# Returns a json response if the request IP is not in the allowed hosts
def on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


app = Flask(__name__)


@app.route("/api/greet", methods=["GET"])
@limit_hosts(allowed_hosts=ALLOWED_HOSTS, on_denied=on_denied)
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

> [!WARNING]  
> You can use both the `@allowed_hosts.limit` and the legacy `@limit_hosts` decorator at the same time. However, the
> legacy decorator will not follow the configurations set in the `AllowedHosts` instance. It is preferred to use only
> one of them to avoid inconsistencies.



_For more examples you can check [examples](https://github.com/riad-azz/flask-allowed-hosts/tree/main/examples)_.

## Parameters

### AllowedHosts class

- `app`: Flask: The Flask app object.

- `allowed_hosts`: [List[str], str]: Modify this list to include the allowed hosts. The default value is an empty
  list `[]`, which means requests from all hosts are allowed.

- `on_denied`: Callable: Modify this function to customize the behavior when a request is denied. The default is `None`,
  which means a 403 Forbidden error is returned.

### @AllowedHosts.limit decorator

- `allowed_hosts`: [List[str], str]: Modify this list to override the allowed hosts list set in `AllowedHosts`. The
  default value is what you set in the `AllowedHosts` instance.

- `on_denied`: Callable: Modify this function to customize the behavior when a request is denied. The default value is
  what you set in the `AllowedHosts` instance.

### @limit_hosts decorator (legacy)

- `allowed_hosts`: [List[str], str]: Modify this list to include the allowed hosts. The default value is `None`, which
  means requests from all hosts are allowed.

- `on_denied`: Callable: Modify this function to customize the behavior when a request is denied. The default is `None`,
  which means a 403 Forbidden error is returned.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit
a pull request.

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details.
