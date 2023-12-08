from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({"message": "Hello world"})


if __name__ == "__main__":
    app.run(debug=True)
