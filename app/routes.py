import os

from flask import render_template, session, redirect, url_for

from app import app
from app.forms import DataForm
from app.predict import preprocess, predict, postprocess
from app.database import execute_sql

app.config['SECRET_KEY'] = 'BoxOfficeDat158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value

        data = preprocess(session)
        pred = predict(data)
        # pred = postprocess(pred)

        title = "Test2"
        pred_value = 20
        session['pred'] = pred
        sql = """insert into prediction values (%(title)s, %(prediction)s, 0)"""
        execute_sql(sql, {"title": title, "predicted_value": pred_value})
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    sql = """select * from prediction"""
    old_pred_list = execute_sql(sql, {})
    return render_template('dashboard.html', old_pred=old_pred_list)
