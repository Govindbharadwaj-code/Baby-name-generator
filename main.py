from flask import Flask, render_template_string, jsonify
import random

app = Flask(__name__)

names = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 'Reyansh', 'Ayaan', 'Krishna', 'Ishaan', 'Anaya', 'Siya', 'Pari', 'Avni', 'Myra', 'Aadhya', 'Anika', 'Prisha', 'Riya', 'Saanvi']

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Baby Name Reveal</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 80px; }
        #name { font-size: 2em; margin: 20px; color: #2d6a4f; }
        button { padding: 10px 30px; font-size: 1.2em; background: #40916c; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #1b4332; }
    </style>
</head>
<body>
    <h1>Baby Name Reveal</h1>
    <div id="name">Click below to reveal a name!</div>
    <button onclick="revealName()">Reveal Name</button>
    <script>
        function revealName() {
            fetch('/random-name').then(r => r.json()).then(data => {
                document.getElementById('name').innerText = data.name;
            });
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/random-name')
def random_name():
    return jsonify({'name': random.choice(names)})

if __name__ == '__main__':
    app.run(debug=True)
