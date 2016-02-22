from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextField, validators
from wtforms.validators import Required
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('EMAIL:', [validators.Email()])
    passwd = PasswordField('PASSWORD:', [validators.Required(), validators.Length(min=6, max = 35)])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    passwd = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
	passwd = form.passwd.data
        form.name.data = ''
	form.passwd.data = ''
	os.system('ls -lt')	
    return render_template('index.html', form=form, name=name)


if __name__ == '__main__':
    manager.run()
