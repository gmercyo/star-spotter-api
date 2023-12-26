from find_actor import find_actor_profile, find_actor_id
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({"message": "Hello world"})

@app.route("/search", methods=["GET"])
def search():
   actor_name = request.args.get('name', default='')
   actor_id = find_actor_id(actor_name)
   if actor_id is not None:
    actor_profile = find_actor_profile(actor_id)
    return jsonify(actor_profile)
   else:
    return jsonify({"error": "Actor not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
