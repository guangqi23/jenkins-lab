import flask, time

app = flask.Flask(__name__)
app = 2

@app.route("/")
def index():
    return "Welcome!!! ",time.localtime
