from re import DEBUG
from flask import Flask, render_template, request
from flask.templating import Environment
from controllers.events import Events

app = Flask(__name__)
controller = Events()

@app.route("/")
def index():

    return render_template("index.html")

@app.route('/evaluate', methods=["POST"])
def evaluate():
    probabilities = controller.run(request.form.to_dict())
    return (probabilities)
    
if __name__ == "__main__":
    app.run()
