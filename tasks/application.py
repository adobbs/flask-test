from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

todos = []

@app.route("/")
def tasks():
    return render_template("tasks.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        todo = request.form.get("task")
        todos.append(todo)
        return redirect("/")