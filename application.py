from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/flask/hello", methods=["POST"])
def hello():
    data = request.json
    name = data.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
