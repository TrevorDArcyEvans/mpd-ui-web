from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "index"

@app.route("/toggle")
def toggle():
  return "toggle"

@app.route("/next")
def next():
  return "next"

@app.route("/prev")
def prev():
  return "prev"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

