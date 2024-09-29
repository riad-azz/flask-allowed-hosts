from flask import Flask, request, jsonify, Blueprint

from flask_allowed_hosts import AllowedHosts

ALLOWED_HOSTS = ["93.184.215.14", "api.example.com"]

app = Flask(__name__)
allowed_hosts = AllowedHosts(app, allowed_hosts=ALLOWED_HOSTS)

bp = Blueprint("bp", __name__, url_prefix="/bp")


# This endpoint only allows incoming requests from "93.184.215.14" and "api.example.com"
@bp.route("/greet", methods=["GET"])
@allowed_hosts.limit()
def bp_greet_endpoint():
    data = {"message": f"Hello There from Blueprint!"}
    return jsonify(data), 200


app.register_blueprint(bp)


# This endpoint only allows incoming requests from "127.0.0.1" and "api.example.com"
@app.route("/api/greet", methods=["GET"])
@allowed_hosts.limit(allowed_hosts=["127.0.0.1", "api.example.com"])
def greet_endpoint():
    name = request.args.get("name", "Friend")
    data = {"message": f"Hello There {name}!"}
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
