from flask import Flask, request, jsonify
from flask_allowed_hosts import AllowedHosts

ALLOWED_HOSTS = ["93.184.215.14", "api.example.com"]


# Returns a json response if the request IP/hostname is not in the allowed hosts
def custom_on_denied():
    error = {"error": "Oops! looks like you are not allowed to access this page!"}
    return jsonify(error), 403


app = Flask(__name__)
app.config['ALLOWED_HOSTS'] = ALLOWED_HOSTS
app.config['ALLOWED_HOSTS_ON_DENIED'] = custom_on_denied

allowed_hosts = AllowedHosts()
allowed_hosts.init_app(app)


# This endpoint only allows incoming requests from "93.184.215.14" and "api.example.com"
@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit()
def greet_endpoint():
    name = request.args.get("name", "Friend")
    data = {"message": f"Hello There {name}!"}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
