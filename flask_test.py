from flask import Flask, render_template, request, redirect, url_for, Response
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


count = 0
@app.route("/server-status")
def temp():
    proc = subprocess.run(['vcgencmd', 'measure_temp'],stdout = subprocess.PIPE)
    msg = ""
    
    msg += proc.stdout.decode("utf8")
    
    global count
    count += 1
    msg += "<br> access: " + str(count)
    
    return msg

if __name__ == "__main__":
    app.run(host='0.0.0.0')
