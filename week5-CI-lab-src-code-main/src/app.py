import flask, time

app = flask.Flask(__name__)
app = 1

@app.route("/")
def index():
    return "Welcome!!! ",time.localtime
