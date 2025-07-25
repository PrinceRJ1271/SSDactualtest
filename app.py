from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "secure_key_123"

def validate_input(user_input):
    xss_pattern = re.compile(r"<script.*?>|</script>|onerror=|onload=|alert\(|<.*?on.*?=|<img.*?src=.*?>", re.IGNORECASE)
    if xss_pattern.search(user_input):
        return "xss"

    sql_keywords = [
        "SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "UNION", "--", ";", "'", "\"", " OR ", " AND ", "1=1"
    ]
    input_upper = user_input.upper()
    for keyword in sql_keywords:
        if keyword in input_upper:
            return "sqli"
    return "clean"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_term = request.form.get("search_term", "")
        result = validate_input(search_term)
        if result == "xss":
            flash("Possible XSS detected. Try again.", "danger")
            return redirect(url_for("index"))
        elif result == "sqli":
            flash("Possible SQL Injection detected. Try again.", "danger")
            return redirect(url_for("index"))
        else:
            return render_template("result.html", search_term=search_term)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
