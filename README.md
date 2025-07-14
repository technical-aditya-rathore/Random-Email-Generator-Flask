# Random-Email-Generator-Flask
--------------------------------------------------------------------------------------------------------------------------------------------------------=----------------------
✅ Project Overview
Name: Random Email Generator

Tech Stack: Python (Flask) + HTML + CSS

Features:

Generates a random email each time you click a button

Clean, responsive webpage

Copyright in the footer
random_email_generator/
│
├── app.py
├── templates/
│   ├── index.html
├── static/
│   ├── style.css
└── README.md
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
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Random Email Generator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Random Email Generator</h1>
        <button id="generateBtn">Generate Email</button>
        <p id="emailOutput"></p>
    </div>

    <footer>
        &copy; 2025 Aditya Kumar Jha | All Rights Reserved.
    </footer>

    <script>
        const btn = document.getElementById('generateBtn');
        const output = document.getElementById('emailOutput');

        btn.addEventListener('click', () => {
            fetch('/generate')
            .then(response => response.json())
            .then(data => {
                output.textContent = "Generated Email: " + data.email;
            });
        });
    </script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    background: #0f2027;  /* dark background */
    color: #f5f5f5;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    justify-content: center;
    align-items: center;
    margin: 0;
}

.container {
    text-align: center;
    background: #1c1c1c;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 10px #00ffff;
}

button {
    background: #00ffff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    color: #000;
    cursor: pointer;
    border-radius: 5px;
    transition: background 0.3s ease;
}

button:hover {
    background: #00ced1;
}

footer {
    position: fixed;
    bottom: 10px;
    text-align: center;
    width: 100%;
    color: #ccc;
    font-size: 14px;
}

# Random Email Generator Website

This is a simple Flask web app that generates a random email address at the click of a button.

## How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd random_email_generator

© 2025 Aditya Kumar Jha. All Rights Reserved.  
This project, “Random Email Generator”, including all source code, design, and content, is protected under applicable copyright laws. Unauthorized reproduction, distribution, or use of any part of this project without express written permission is strictly prohibited.
```


