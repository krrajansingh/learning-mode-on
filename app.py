from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def First():
  return render_template('home.html')


@app.route("/SecondPage")
def Second():
  return "<p>Second Page Website</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)