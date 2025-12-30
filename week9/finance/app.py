import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])

    cash = db.execute("SELECT cash FROM users WHERE id= :user_id",
                      user_id=session["user_id"])[0]["cash"]

    t_value = cash
    total = cash

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["value"] = stock["price"] * stock["total_shares"]
        t_value += stock["value"]
        total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=usd(cash), t_value=usd(t_value), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        if not symbol:
            return apology("provid symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("provid positive number")

        stocks = lookup(symbol)
        if stocks is None:
            return apology("Symbol not found")

        price = stocks["price"]
        t_cost = int(shares) * price
        data = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["cash"]

        if data < t_cost:
            return apology("Not enough cash")

        db.execute("UPDATE users SET cash = cash - :t_cost WHERE id = :user_id",
                   t_cost=t_cost, user_id=session["user_id"])

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"], symbol=symbol, shares=shares, price=price)

        flash(f"Bought {shares} shares of {symbol} for {usd(t_cost)}")
        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    history = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])

    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not quote:
            return apology("Invalid Symbol", 400)
        return render_template("quote.html", quote=quote)
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        conform = request.form.get("confirmation")

        if not username:
            return apology("provide username.", 400)
        if not password:
            return apology("provide password.", 400)
        if not conform:
            return apology("provide confirm password.", 400)
        if conform != password:
            return apology("Confirm password not match.", 400)

        validate = db.execute("SELECT username FROM users WHERE username = ?;", username)
        if len(validate) != 0:
            return apology("username already exist.", 400)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?);",
                   username, generate_password_hash((password)))

        data = db.execute("SELECT * FROM users WHERE username = ?;", username)

        session["user_id"] = data[0]["id"]

        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")
        if not symbol:
            return apology("provid symbol")
        elif not shares or not shares.isdigit() or int(shares) <= 0:
            return apology("provid positive number")
        else:
            share = int(shares)

        for stock in stocks:
            if stock["symbol"] == symbol:
                if stock["total_shares"] < share:
                    return apology("not eougth shares")
                else:
                    quote = lookup(symbol)
                    if quote is None:
                        return apology("Symbol not found")
                    price = quote["price"]
                    total_sale = share * price

                    db.execute("UPDATE users SET cash = cash + :total_sale WHERE id = :user_id",
                               total_sale=total_sale, user_id=session["user_id"])

                    db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :share, :price)",
                               user_id=session["user_id"], symbol=symbol, share=share, price=price)

                    flash(f"Sold {share} Share of {symbol} for {usd(total_sale)}")
                    return redirect("/")

        return apology("symbol not found")

    return render_template("sell.html", stocks=stocks)
