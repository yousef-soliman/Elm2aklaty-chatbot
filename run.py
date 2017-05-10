# -*- coding: utf-8 -*-
from flask import Flask,jsonify
from flask import render_template
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL
import random
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'restaurant'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect().cursor()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getJson",methods=['GET'])
def getJson():
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
    return jsonify(json_string)

@app.route("/allrestaurants")
def allrestaurants():
    conn.execute("select * from fish")
    data = conn.fetchall()
    buttons = []
    for raw in data:
        name = raw[0]
        buttons.append({"name":name, "value":name})
    json_string = {"message":"","buttons":buttons}
    return jsonify(json_string)

@app.route("/wanttoeat")
def eat():
        msg = [u'عارف مكانك ولا هتتعبنا',u'طيب اشطة حدد مكانك',u'طب يلا عشان تعزمني ']
        randmsg=random.choice(msg)
        json_string = {"message": randmsg,"do":"locate()",
                       "buttons":[{"name":"fish","value":u'سمك'},
                                  {"name":"meat","value":u'لحمة'},
                                  {"name": "italian", "value": u'ايطالي'}
                                  ]
                        }
        return (json_string["message"])

if __name__ == '__main__':
    app.run(debug=True)
