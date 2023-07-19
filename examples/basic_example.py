from flask import Flask, request, jsonify
from flask_allowedhosts import limit_hosts

app = Flask(__name__)

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


@app.route("/api/greet", methods=["GET"])
@limit_hosts(allowed_hosts=ALLOWED_HOSTS)
def greet_endpoint():
    name = request.args.get("name", "Friend")
    greeting = {"greeting": f"Hello There {name}!"}
    return jsonify(greeting), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
