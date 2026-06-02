from flask import Flask, request, render_template
from datetime import datetime
from service import login_user

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html", result=None)

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        ip = request.remote_addr

        input_info = {}

        input_info["ip"] = ip
        input_info["username"] = username
        input_info["password"] = password
        input_info["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = login_user(input_info)

        return render_template("login.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)