from find_actor import find_actor_by_image, find_actor_profile, find_actor_id
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow cross-origin request from all domains
CORS(app, resources={r"/*": {"origins": ["https://app.star-spotter.com"]}})


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({"message": "Hello world"})


@app.route("/search", methods=["GET"])
def search():
    actor_name = request.args.get("name", default="")
    actor_id = find_actor_id(actor_name)
    if actor_id is not None:
        actor_profile = find_actor_profile(actor_id)
        return jsonify(actor_profile)
    else:
        return jsonify({"error": "Actor not found"}), 404


@app.route("/rekognise", methods=["POST"])
def rekognise():
    if "image" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["image"]

    if file and file.filename != "":
        actor_name = find_actor_by_image(file)
        if actor_name is not None:
            return jsonify({"name": actor_name})
        else:
            return jsonify({"error": "Actor not found"}), 404
    else:
        # If the user does not select a file, the browser submits an empty file without a filename.
        return jsonify({"error": "No selected file"}), 400


if __name__ == "__main__":
    app.run(debug=True)
