# -*- coding: utf-8 -*-
from flask import Flask,jsonify,request
from flask import render_template
from werkzeug.utils import secure_filename
from flaskext.mysql import MySQL
import random
from os import listdir
from os.path import isfile, join


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'restaurants'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect().cursor()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getrestaurant",methods = ["POST"])
def getrestaurant():
    name = request.form['text']
    data = tuple()
    print(name)
    conn.execute("select * from fish where name = '"+name+"';")
    data = conn.fetchall()
    conn.execute("select * from cafe where name = '"+name+"';")    
    data += conn.fetchall()
    conn.execute("select * from pizza where name = '"+name+"';")    
    data += conn.fetchall()
    conn.execute("select * from local where name = '"+name+"';")    
    data += conn.fetchall()
    conn.execute("select * from meats where name = '"+name+"';")    
    data += conn.fetchall()
    conn.execute("select * from soury where name = '"+name+"';")    
    data += conn.fetchall()
    conn.execute("select * from takeway where name = '"+name+"';")    
    data += conn.fetchall()
    

    imgs = []
    for raw in data:
        name = raw[3]
        mypath = "static/restaurants/"+ name.encode("utf-8") + "/"
        for f in listdir(mypath):
            if isfile(join(mypath, f.encode("utf-8"))):
                imgs.append(join(mypath, f.encode("utf-8")))
                print(join(mypath, f.encode("utf-8")))
    
    
    buttons = [
        {"text":"تمام", "do":"good()"},
        {"text":"لا", "do":"ok()"}
        ]
    json_str = {'path':imgs,"buttons":buttons}
    
    return jsonify(json_str)


@app.route("/category")
def category():
    buttons = [
        {"text":"اسماك","name":"fish","do":"getcategory(this)"},
        {"text":"مشويات","name":"meats","do":"getcategory(this)"},
        {"text":"شعبي","name":"local","do":"getcategory(this)"},
        {"text":"بيتزا","name":"pizza","do":"getcategory(this)"},
        {"text":"سوري","name":"soury","do":"getcategory(this)"}
    ]
    json_string = {"message":"عايز تاكل ايه","buttons":buttons}
    return jsonify(json_string)


@app.route("/getcategory", methods = ["POST"])
def getcategory():
    table = request.form['text']
    conn.execute("select * from "+table)
    data = conn.fetchall()
    buttons = []
    for raw in data:
        name = raw[0]
        buttons.append({"text":name, "name":name,"do":"send(this)"},)
    json_string = {"message":"دي المطاعم","buttons":buttons}
    return jsonify(json_string)


@app.route("/getmenu")
def getmenu():
   pass



@app.route("/allrestaurants")
def allrestaurants():
    data = tuple()
    tables_name = conn.execute("show tables;")
    print(tables_name)
    conn.execute("select * from fish")
    data = conn.fetchall()
    conn.execute("select * from cafe")    
    data += conn.fetchall()
    conn.execute("select * from pizza")    
    data += conn.fetchall()
    conn.execute("select * from local")    
    data += conn.fetchall()
    conn.execute("select * from meats")    
    data += conn.fetchall()
    conn.execute("select * from soury")    
    data += conn.fetchall()
    conn.execute("select * from takeway")    
    data += conn.fetchall()


    buttons = []
    for raw in data:
        name = raw[0]
        buttons.append({"text":name, "name":name,"do":"send(this)"},)
    json_string = {"message":"دي المطاعم","buttons":buttons}
    return jsonify(json_string)


@app.route("/wanttoeat")
def wanttoeat():
        msg = [u'عارف مكانك ولا هتتعبنا',u'طيب اشطة حدد مكانك',u'طب يلا عشان تعزمني ']
        randmsg=random.choice(msg)
        json_string = {"message": randmsg,
                       "buttons":[
                           {"text":"حدد المكان","do":"locate()"},
                                  ]
                        }
        return jsonify(json_string)

@app.route("/valid")
def valid():
        json_string = {
                       "buttons":[
                           {"text":"تمام", "do":"ok()"},
                           {"text":"لا", "do":"delete_marker()"}
                        ]
                        }
        return jsonify(json_string)


if __name__ == '__main__':
    app.run(debug=True)
