from cs50 import SQL
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "your_secret_key_here"  # Required for sessions

db = SQL("sqlite:///login_data.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods= ["GET","POST"])
def signup():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("pass")

        if user and password:
            db.execute("INSERT INTO userdata(username, password) VALUES(?, ?);", user, password)
            return redirect("/login")

    return render_template("signin.html")

@app.route("/login", methods= ["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("pass")

        validate = db.execute("SELECT * FROM userdata WHERE username = ? and password = ?;", user, password)

        if validate:
            session["name"]= user
            return redirect("/success")

    return render_template("login.html")

@app.route("/success", methods= ["GET","POST"])
def success():

    return render_template("success.html", name = session.get("name"))
