import os

from flask import render_template, session, redirect, url_for, request

from app import app
from app.forms import DataForm
from app.predict import preprocess, predict, postprocess
from app.database import execute_sql_select, execute_sql_insert

app.config['SECRET_KEY'] = 'BoxOfficeDat158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            for fieldname, value in form.data.items():
                session[fieldname] = value

            data = preprocess(session)
            pred = predict(data)
            pred = postprocess(pred)
            title = "Not implemented"
            pred_value = "${:,.2f}".format(float(pred['pred']))
            corr_value = 0
            session['pred'] = "${:,.2f}".format(float(pred['pred']))
            print(session['pred'])
            sql = """insert into prediction (title, predicted_value, corrected_value) values (%s, %s, %s)"""
            execute_sql_insert(sql, (title, pred_value, corr_value))
            return redirect(url_for('index'))
        else:
            session['pred'] = ''
            print(form.errors)

    else:
        return render_template('index.html', form=form)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    sql = """select * from prediction"""
    old_pred_list = execute_sql_select(sql, {})
    return render_template('dashboard.html', old_pred=old_pred_list)


@app.route('/update', methods=['POST'])
def update():
    name = request.form.get('rev_name')
    cor_rev = request.form.get('cor_rev')
    pred = request.form.get('pred')
    print(name, pred, cor_rev)
    return redirect(url_for('dashboard'))
