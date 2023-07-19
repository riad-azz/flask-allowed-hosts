# Flask Allowed Hosts

Flask Allowed Hosts is a Flask extension that provides host validation for API endpoints. It allows you to enforce that requests are only accepted from specific hosts, providing an additional layer of security for your Flask application.

## Installation

Install the package using pip:

```cmd
pip install flask-allowedhosts
```

## Getting Started

To limit access to your routes using `flask-allowedhosts` follow these simple steps:

1. Import the `limit_hosts` decorator from flask_allowedhosts.
2. Define the list of allowed hosts.
3. Apply the `@limit_hosts` decorator to the desired endpoint(s).

```python
from flask import Flask, request, jsonify
from flask_allowedhosts import limit_hosts

app = Flask(__name__)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


@app.route("/api/greet")
@limit_hosts(allowed_hosts=ALLOWED_HOSTS)
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Now only the allowed hosts set in `ALLOWED_HOSTS` can access the protected endpoint(s). Requests from other hosts will receive a 403 Forbidden error.

_The default value for `allowed_hosts` is an empty list, which means requests from all hosts are allowed._

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details.