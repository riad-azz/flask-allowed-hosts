from flask import Flask, request, jsonify

from flask_allowed_hosts import AllowedHosts

ALLOWED_HOSTS = ["93.184.215.14", "api.example.com"]


# Returns a json response if the request IP/hostname is not in the allowed hosts
def custom_on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


app = Flask(__name__)
allowed_hosts = AllowedHosts(app, allowed_hosts=ALLOWED_HOSTS, on_denied=custom_on_denied)


# This endpoint only allows incoming requests from "93.184.215.14" and "api.example.com"
@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit()
def greet_endpoint():
    name = request.args.get("name", "Friend")
    data = {"message": f"Hello There {name}!"}
    return jsonify(data), 200


# This endpoint allows all incoming requests
@app.route("/api/public", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["0.0.0.0/0"])
def public_endpoint():
    data = {"message": f"this is a public endpoint by override"}
    return jsonify(data), 200


# This endpoint only allows incoming requests from "127.0.0.1" to "127.0.0.255"
@app.route("/api/network", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["127.0.0.0/24"])
def override_endpoint():
    data = {"message": f"this endpoint is restricted to 127.0.0.0/24"}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
