import re

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

todo_items = []
priorities = ("Low", "Medium", "High")


@app.route("/")
def index():
    return render_template(
        "index.html", todo_items=todo_items, priorities=priorities
    )


@app.route("/submit", methods=["POST"])
def submit():
    task = request.form.get("task", "").strip()
    email = request.form.get("email", "").strip()
    priority = request.form.get("priority", "")

    valid_email = re.fullmatch(r"[^@\s]+@[^@\s.]+(?:\.[^@\s.]+)+", email)

    if not task or not valid_email or priority not in priorities:
        return redirect(url_for("index"))

    todo_items.append({"task": task, "email": email, "priority": priority})
    return redirect(url_for("index"))


@app.route("/clear", methods=["POST"])
def clear():
    todo_items.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()