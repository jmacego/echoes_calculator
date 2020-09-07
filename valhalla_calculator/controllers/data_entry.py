"""
PI Calculators
"""
import json
import os
from flask import (
    Blueprint, render_template, request, send_file, current_app, redirect, url_for
)
import configuration  # configuration variables, including secrets

bp = Blueprint('data_entry', __name__, url_prefix='/data_entry')

@bp.route('/', methods=('GET', 'POST'))
def create_network():
    """Do PI stuff"""
    if request.method == 'GET':
        if os.path.exists("instance/pricing_data.json"):
            with open("instance/pricing_data.json") as f:
                pricing_data = json.load(f)
        else:
            pricing_data = None
        return render_template('pricing_entry.html', pricing_data=pricing_data)
    elif request.method == 'POST':
        pricing_data = [x.strip().split("\t") for x in request.form['pricing_data'].split("\n") if x.strip()]
        with open("instance/pricing_data.json", "w") as f:
            json.dump(pricing_data, f, indent=2)
        return render_template('pricing_entry.html', pricing_data=pricing_data)
    else:
        return "Method not supported"