#import libraries
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def is_xss(input_str):
    return "<" in input_str or "script" in input_str.lower()

def is_sql_injection(input_str):
    sql_keywords = ["select", "insert", "drop", "update", "--", "' OR", '" OR']
    return any(keyword in input_str.lower() for keyword in sql_keywords)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        term = request.form.get('search')
        if is_xss(term) or is_sql_injection(term):
            return render_template('index.html', error="Invalid input!")
        return render_template('result.html', result=term)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
