from app import app
from flask import render_template, session, redirect, url_for, request
import pickle

from app.forms import DataForm

app.config['SECRET_KEY'] = 'BoxOfficeDat158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = DataForm()
    #session['pred'] = 'Test'

    return render_template('index.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
