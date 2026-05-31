from flask import Flask, request, jsonify
from datetime import datetime
from verification import verify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ip = request.remote_addr

        input_info = {}

        input_info["ip"] = ip
        input_info["username"] = username
        input_info["password"] = password
        input_info["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        verify(input_info)
    else:
        return jsonify({"message": "send post request"})

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run()