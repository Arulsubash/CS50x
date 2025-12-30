from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db= SQL("sqlite:///database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
      return render_template("error.html", error= "Name not entered")
    if not sport:
      return render_template("error.html", error= "Sport not entered")
    db.execute("INSERT INTO registration(Name, Sport) VALUES(?, ?);", name, sport)
    return render_template("success.html")

@app.route("/database")
def database():
   data = db.execute("SELECT * FROM registration;")
   return render_template("database.html", database=data)
