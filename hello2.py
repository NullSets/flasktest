from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
app.config["SECRET_KEY"] = "hard to guess string"
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    # StringField类表示属性为type="text"的<input>元素
    name = StringField("What is your name?", validators=[DataRequired()])
    # SubmitField类表示属性为type="submit"的<input>元素
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Look like you have changed your name!")
        session["name"] = form.name.data
        return redirect(url_for('index'))
    return render_template("index1.html", form=form, name=session.get("name"))



