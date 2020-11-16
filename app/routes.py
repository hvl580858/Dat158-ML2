from app import app
from flask import render_template, session, redirect, url_for, request
from app.predict import preprocess, predict, postprocess
from flask_sqlalchemy import SQLAlchemy
import pickle
import os

from app.forms import DataForm

app.config['SECRET_KEY'] = 'BoxOfficeDat158'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value

        data = preprocess(session)
        pred = predict(data)
        pred = postprocess(pred)

        session['pred'] = pred

        return redirect(url_for('index'))

    return render_template('index.html', form=form)


@app.route('/dashboard')
def dashboard():
    old_pred_list = []



    return render_template('dashboard.html', old_pred=old_pred_list)
