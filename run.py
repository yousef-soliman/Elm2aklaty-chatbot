from flask import Flask
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField
from wtforms_validators import InputRequired, Length

app = Flask(__name__);

class LoginForm(FlaskForm):
    username = StringField('username', validators = [InputRequired('Username Required!')]
    password = PasswordField('password', validators = [InpurRequired('Password Required!'), Length(min=8,max=64,'Must be between 8 and 64 characters.')

@app.route("/form", methods=['GET','POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h2> Ok, In principle</h2>'
    return render_template("form.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
