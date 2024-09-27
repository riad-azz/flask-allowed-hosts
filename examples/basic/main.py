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
