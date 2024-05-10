from flask import Flask, request, jsonify
from flask_allowedhosts import limit_hosts

app = Flask(__name__)

ALLOWED_HOSTS = ["123.123.123.123", "321.321.321.321"]


# Returns a json response if the request IP is not in the allowed hosts
def on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


@app.route("/", methods=["GET"])
def home_page():
    return "Hello World!"


@app.route("/api/greet", methods=["GET"])
@limit_hosts(allowed_hosts=ALLOWED_HOSTS, on_denied=on_denied)
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
