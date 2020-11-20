import os

from flask import render_template, session, redirect, url_for, request

from app import app
from app.forms import DataForm
from app.predict import preprocess, predict, postprocess
from app.database import execute_sql_select, execute_sql_query

app.config['SECRET_KEY'] = 'BoxOfficeDat158'

""""
Index route:
    This is our main page that deals with displaying our form, validating the form and then predict the price.
    We added a title so it would be easier to spot the specific predictions in the database/dashboard.
    The prediction we format into a dollar/money float format to make it look better.
    We use psycopg2 to save and retrieve our data as that was something we knew how to instead of flask-SQLAlchemy.
    We used PRG web development pattern so we do our prediction and saving to database in POST and display our form and 
    result in get.
"""


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            for fieldname, value in form.data.items():
                session[fieldname] = value

            data, title = preprocess(session)
            pred = predict(data)
            pred = postprocess(pred)

            if title == "":
                title = "Not given"
            pred_value = "${:,.2f}".format(float(pred['pred']))
            corr_value = 0
            session['pred'] = "${:,.2f}".format(float(pred['pred']))
            sql = """insert into prediction (title, predicted_value, corrected_value) values (%s, %s, %s)"""
            execute_sql_query(sql, (title, pred_value, corr_value))
            return redirect(url_for('index'))
        else:
            session['pred'] = ''
            print(form.errors)

    else:
        return render_template('index.html', form=form)


""""
Dashboard route:
    Small route that display the dashboard.html with the data from the database.
    Small easy select to get the data and pass to render_template.
"""


@app.route('/dashboard', methods=['GET'])
def dashboard():
    sql = """select * from prediction"""
    old_pred_list = execute_sql_select(sql, {})
    return render_template('dashboard.html', old_pred=old_pred_list)


""""
Update route:
    We didnt manage to finish this route, but we made things ready to start updating data in the database.
    We could choose to update corrected revenue, name or anything else we would put in. 
    Part of the work to get this going was saving and displaying the data to and from the database as shown in dashboard
    and index.
"""


@app.route('/update', methods=['POST'])
def update():
    name = request.form.get('rev_name')
    cor_rev = request.form.get('cor_rev')
    pred = request.form.get('pred')
    print(name, pred, cor_rev)
    return redirect(url_for('dashboard'))
