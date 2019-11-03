import os
import subprocess

from flask import Flask, request
app = Flask(__name__, static_url_path='', static_folder='')

@app.route("/")
def index():
  return app.send_static_file('index.html')

@app.route("/toggle")
def toggle():
  os.system('mpc toggle &')
  return current()

@app.route("/next")
def next():
  os.system('mpc next &')
  return current()

@app.route("/prev")
def prev():
  os.system('mpc prev &')
  return current()

@app.route("/current")
def current():
  msg = subprocess.check_output(['mpc']).split('\n')
  return msg[0] + '\r\n' + msg[1]

@app.route("/volup")
def volup():
  os.system('amixer set Speaker 5%+ &')
  return current()

@app.route("/voldown")
def voldown():
  os.system('amixer set Speaker 5%- &')
  return current()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

