from flask import Flask, render_template, request, redirect, url_for, Response
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/pi-status")
def temp():
    proc = subprocess.run(['vcgencmd', 'measure_temp'],stdout = subprocess.PIPE)
    msg_temp = proc.stdout.decode("utf8")
    return msg_temp

if __name__ == "__main__":
    app.run(host='0.0.0.0')
