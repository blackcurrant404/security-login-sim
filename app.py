from flask import Flask, request, render_template
from datetime import datetime
from service import login_user, register_user
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

        input_info = {
            "ip": ip,
            "username": username,
            "password": password,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
        result = login_user(input_info)

        return render_template("login.html", result=result)

@app.route("/signup", methods=["GET", "POST"])
def singup():

    if request.method == "GET":
        # result None because there isn't one    before any attempt
        return render_template("signup.html", result=None) 
        

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        input_info = {
            "username": username,
            "password": password
        }

        result = register_user(input_info)

        return render_template("signup.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)