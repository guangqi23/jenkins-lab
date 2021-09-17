import flask, time

app = flask.Flask(__name__)


@app.route("/")
def index():
    msg = "Welcome!!! " + time.localtime
    return msg
