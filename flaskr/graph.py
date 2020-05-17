import json
import pandas as pd

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flask_json import as_json
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('graph', __name__)

@bp.route('/')
@login_required
def index():
    return redirect(url_for('graph.charts'))
    
@bp.route('/charts')
def charts():
    df = pd.read_csv('C:/Users/arun.alex/Personal/Python/testcase_visualizer/flaskr/datas.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data, indent=2)
    data = {'chart_data': chart_data}
    return render_template('graphs/coverage.html', data=data)

@bp.route('/data.json')
@as_json
def datas():
    df = pd.read_csv('C:/Users/arun.alex/Personal/Python/testcase_visualizer/flaskr/datas.csv')
    chart_data = df.to_dict(orient='records')
    # chart_data = json.dumps(chart_data, indent=2)
    # data = {'chart_data': chart_data}
    return chart_data
