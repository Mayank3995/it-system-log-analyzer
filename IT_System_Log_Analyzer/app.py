import random
from datetime import datetime
from flask import Flask, render_template, jsonify, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"   # session key

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple admin login
        if username == "admin" and password == "admin123":
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("index.html")


# ---------------- LOG GENERATOR ----------------
def generate_random_log():
    log_types = ["INFO", "WARNING", "ERROR"]
    messages = {
        "INFO": ["User login successful", "System running normally", "Service started"],
        "WARNING": ["CPU usage high", "Memory usage increased"],
        "ERROR": ["Disk space low", "Unauthorized access detected", "Failed login attempt"]
    }

    for _ in range(random.randint(2, 5)):
        level = random.choice(log_types)
        message = random.choice(messages[level])
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("system.log", "a") as f:
            f.write(f"{time} {level} {message}\n")


# ---------------- LIVE DATA API ----------------
@app.route("/log-data")
def log_data():
    if "user" not in session:
        return jsonify({"error": "Unauthorized"})

    generate_random_log()

    info = warning = error = threats = total = 0

    with open("system.log", "r") as f:
        for line in f:
            total += 1
            if "INFO" in line:
                info += 1
            elif "WARNING" in line:
                warning += 1
            elif "ERROR" in line:
                error += 1
            if "Unauthorized" in line or "Failed" in line:
                threats += 1

    return jsonify({
        "info": info,
        "warning": warning,
        "error": error,
        "threats": threats,
        "total": total
    })


if __name__ == "__main__":
    app.run(debug=True)
