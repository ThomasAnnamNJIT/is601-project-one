import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    path = "./static/images/"
    return render_template("index.html", name="Thomas Annam", images=[path+image for image in os.listdir(path)])


if __name__ == '__main__':
    app.run()
