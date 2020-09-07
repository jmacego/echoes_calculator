"""
PI Calculators
"""
from flask import (
    Blueprint, render_template, request, send_file, current_app, redirect, url_for
)
import configuration  # configuration variables, including secrets

bp = Blueprint('pi', __name__, url_prefix='/pi')

resources = {'Fiber Composite': 50,
             'Lustering Alloy': 60,
             'Toxic Metals': 160,
             'Precious Alloy': 90,
             'Glossy Compound': 50,
             'Heavy Metals': 60,
             'Noble Metals': 60,
             'Opulent Compound': 60,
             'Base Metals': 50,
             'Sheen Compound': 60,
             'Reactive Metals': 200,
             'Condensed Alloy': 50,
             'Motley Compound': 70,
             'Gleaming Alloy': 50}
@bp.route('/', methods=('GET', 'POST'))
def create_network():
    """Do PI stuff"""
    if request.method == 'GET':
        return render_template('pi.html', resources=resources)
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
        return render_template('pi.html', value=value, resources=resources)
    else:
        return "Method not supported"
