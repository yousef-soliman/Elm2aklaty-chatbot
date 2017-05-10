from flask import Flask,jsonify, url_for
from flask import render_template
import json, os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getJson",methods=['GET'])
def getJson():
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
    return jsonify(json_string)


if __name__ == '__main__':
    app.run(debug=True)