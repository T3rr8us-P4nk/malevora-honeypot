from flask import Flask, render_template, request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
@app.route('/<directory1>')
@app.route('/<directory1>/<directory2>')
@app.route('/<directory1>/<directory2>/<directory3>')
def index(directory1=None, directory2=None, directory3=None):
    if directory1:
        data = {
            'Ip Address': request.remote_addr,
            'User-Agent': request.headers.get('User-Agent'),
            'Directory1' : directory1,
            'Directory2' : directory2,
            'Directory3' : directory3
        }
        with open('http/logs/fuzz_logs.json', 'a') as f:
            json.dump(data, f, indent=4)
            f.write("\n")
        return render_template('404.html')
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        paramater = request.args.get('item')
        data = {
            'Timestamp': str(datetime.now()),
            'Ip Address': request.remote_addr,
            'User-Agent': request.headers.get('User-Agent'),
            'Payload': paramater
        }
        with open('http/logs/injection_logs.json', 'a') as f:
            json.dump(data, f, indent=4)
            f.write("\n")
        return render_template('404.html')
    return render_template('index.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    response = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        response = "Wrong Username/Password"
        data = {
            'Timestamp': str(datetime.now()),
            'Ip Address': request.remote_addr,
            'User-Agent': request.headers.get('User-Agent'),
            'Username': username,
            'Password': password
        }
        with open('http/logs/login_logs.json', 'a') as f:
            json.dump(data, f, indent=4)
            f.write("\n")
    return render_template('admin.html', response=response)


if __name__ == "__main__":
    app.run(debug=True)