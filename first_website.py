from flask import Flask

app = Flask(__name__)


@app.route("/")
def First():
  return "<p>Second Page Website</p>"


@app.route("/SecondPage")
def Second():
  return "<p>Second Page Website</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)