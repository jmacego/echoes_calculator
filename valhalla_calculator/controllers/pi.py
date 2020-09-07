"""
PI Calculators
"""
import json
from flask import (
    Blueprint, render_template, request, send_file, current_app, redirect, url_for
)
import configuration  # configuration variables, including secrets

bp = Blueprint('pi', __name__, url_prefix='/pi')

@bp.route('/', methods=('GET', 'POST'))
def create_network():
    """Do PI stuff"""

    with open("instance/pricing_data.json") as f:
            pricing_data = json.load(f)
    resources = {}
    for row in pricing_data[19:-1]:
        resources[row[0]] = int(row[1])
    last_updated = pricing_data[0][0]
    if request.method == 'GET':
        return render_template('pi.html', resources=resources, last_updated=last_updated)
    elif request.method == 'POST':
        data = {}
        value = 0
        for response in request.form.to_dict().keys():
            print(response)
            if "resource" in response:
                id = response.replace("resource", "")
                print(request.form['quantity'+id])
                print(request.form['resource'+id])
                if request.form['quantity'+id] != "":
                    value += resources[request.form['resource'+id]] * int(request.form['quantity'+id])
        return render_template('pi.html', value=value, resources=resources, last_updated=last_updated)
    else:
        return "Method not supported"
