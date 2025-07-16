from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

def generate_random_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    domain = random.choice(domains)
    return f"{name}@{domain}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    email = generate_random_email()
    return jsonify({'email': email})

if __name__ == '__main__':
    app.run(debug=True)
