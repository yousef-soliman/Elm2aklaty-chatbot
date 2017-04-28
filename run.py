from flask import Flask
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField

app = Flask(__name__);

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@app.route("/index", methods=['GET','POST'])
def index():
    index = LoginForm()
    if index.validate_on_submit():
        return '<h2> Ok, In principle</h2>'
    return render_template("index.html", index=index)

if __name__ == '__main__':
    app.run(debug=True)
