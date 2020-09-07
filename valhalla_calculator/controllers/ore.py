"""
PI Calculators
"""
import json
from flask import (
    Blueprint, render_template, request, send_file, current_app, redirect, url_for
)
import configuration  # configuration variables, including secrets

bp = Blueprint('ore', __name__, url_prefix='/ore')

@bp.route('/', methods=('GET', 'POST'))
def calculat_ore():
    """calculate ore"""
    with open("instance/pricing_data.json") as f:
            pricing_data = json.load(f)
    resources = {}
    for row in pricing_data[2:19]:
        resources[row[0]] = row[1:7]
    last_updated = pricing_data[0][0]
    if request.method == 'GET':
        return render_template('ore.html', resources=resources, last_updated=last_updated)
    elif request.method == 'POST':
        data = {}
        value = 0
        for response in request.form.to_dict().keys():
            if "resource" in response:
                id = response.replace("resource", "")
                if request.form['quantity'+id] != "":
                    if float(request.form['quantity'+id]) >= 30000:
                        value += float(resources[request.form['resource'+id]][0]) * float(request.form['quantity'+id])
                    elif 30000 > float(request.form['quantity'+id]) >= 20000:
                        value += float(resources[request.form['resource'+id]][1]) * float(request.form['quantity'+id])
                    elif 20000 > float(request.form['quantity'+id]) >= 15000:
                        value += float(resources[request.form['resource'+id]][2]) * float(request.form['quantity'+id])
                    elif 15000 > float(request.form['quantity'+id]) >= 10000:
                        value += float(resources[request.form['resource'+id]][3]) * float(request.form['quantity'+id])
                    elif 10000 > float(request.form['quantity'+id]) >= 0:
                        value += float(resources[request.form['resource'+id]][4]) * float(request.form['quantity'+id])
        return render_template('ore.html', value=value, resources=resources, last_updated=last_updated)
    else:
        return "Method not supported"