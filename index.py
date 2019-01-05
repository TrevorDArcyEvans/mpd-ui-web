from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "index"

@app.route("/toggle")
def toggle():
  os.system('mpc toggle &')
  return "toggle"

@app.route("/next")
def next():
  os.system('mpc next &')
  return "next"

@app.route("/prev")
def prev():
  os.system('mpc prev &')
  return "prev"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

