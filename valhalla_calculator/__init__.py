# -*- coding: utf-8 -*-
"""Web App for some basic calculations for an EE Corp/Alliance
"""
from flask import Flask, send_from_directory, render_template
import os


def create_app(test_config=None):
    """Instantiate flask and create routes

    Implemented Routes:
        * /
    """

    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('../configuration.py', silent=False)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    if os.environ.get("FLASK_ENV", default="production") == "development":
        @app.route('/docs/<path:filename>')
        def send_docs(filename):
            return send_from_directory('../docs/_build/html', filename)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        """Basic index page with the menus for convenience"""
        return render_template('base.html')

    from valhalla_calculator.controllers import pi
    app.register_blueprint(pi.bp)

    return app