import os
import subprocess

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return current()

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

def current():
  return subprocess.check_output(['mpc', 'current'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

