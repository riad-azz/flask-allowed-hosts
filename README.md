# Flask Allowed Hosts

Flask Allowed Hosts is a Flask extension that provides host validation for API endpoints. It allows you to enforce that
requests are only accepted from specific hosts, providing an additional layer of security for your Flask application.

## Installation

Install the package using pip:

```cmd
pip install flask-allowed-hosts
```

## Getting Started

To limit access to your routes using `flask-allowed-hosts`:

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


@app.route("/", methods=["GET"])
def home_page():
  return "Hello World!"


@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit()
def greet_endpoint():
  name = request.args.get("name", "Friend")
  greeting = {"greeting": f"Hello There {name}!"}
  return jsonify(greeting), 200


@app.route("/api/greet/override", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["127.0.0.1", "localhost"])
def greet_override_endpoint():
  name = request.args.get("name", "Friend")
  greeting = {"greeting override": f"Hello There {name}!"}
  return jsonify(greeting), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
```

Now only the allowed hosts set in `ALLOWED_HOSTS` can access the protected endpoint(s). Requests from other hosts will
receive a 403 Forbidden error.

_You can check out more examples in the examples directory_.

### Arguments

- `allowed_hosts`: [List[str], str] : Modify this list to include the allowed hosts. The default value is an empty
  list `[]`, which means requests from all hosts are allowed.

- `on_denied`: Callable: Modify this function to customize the behavior when a request is denied. The default is `None`,
  which means a 403 Forbidden error is returned.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit
a pull request.

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details.
