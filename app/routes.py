from app import app
from flask import render_template, session, redirect, url_for, request
from app.predict import preprocess, predict, postprocess
import pickle

from app.forms import DataForm

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
        pred = postprocess(pred)

        session['pred'] = pred

        return redirect(url_for('index'))

    return render_template('index.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
