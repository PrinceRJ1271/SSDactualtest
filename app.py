from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Simple XSS check (OWASP C5 principle - Validate All Inputs)
def is_xss(input_str):
    xss_patterns = ["<script", "</script", "<", ">", "javascript:", "onerror", "onload"]
    return any(x in input_str.lower() for x in xss_patterns)

# Simple SQL Injection check
def is_sql_injection(input_str):
    sql_keywords = ["select", "insert", "drop", "update", "--", "' or", "\" or", "'=", "\"="]
    return any(keyword in input_str.lower() for keyword in sql_keywords)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        term = request.form.get('search')
        if is_xss(term):
            return render_template('index.html', error="Possible XSS detected. Try again.")
        if is_sql_injection(term):
            return render_template('index.html', error="Possible SQL Injection detected. Try again.")
        return render_template('result.html', result=term)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
