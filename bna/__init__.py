import os

from flask import *

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='c0de4g00d',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/childcare')
    def childcare():
        return render_template('results.html', name="Childcare/Youth Services")

    @app.route('/clothing')
    def clothing():
        return render_template('results.html', name="Clothing")

    @app.route('/education')
    def education():
        return render_template('results.html', name="Education/Training")

    @app.route('/employment')
    def employment():
        return render_template('results.html', name="Employment")

    @app.route('/finaid')
    def financial_assistance():
        return render_template('results.html', name="Financial Assistance")

    @app.route('/food')
    def food():
        return render_template('results.html', name="Food/Nutrition Assistance")

    @app.route('/handicapped')
    def handicapped():
        return redner_template('results.html', name="Handicapped/Disabled Services")

    @app.route('/housing')
    def housing():
        return render_template('results.html', name="Housing/Home Ownership")

    @app.route('/legal')
    def legal():
        return render_template('results.html', name="Legal Aid")

    @app.route('/medical')
    def medical():
        return render_template('results.html', name="Medical Care")

    @app.route('/business')
    def business():
        return render_template('results.html', name="Starting a Small Business")

    @app.route('/transportation')
    def transportation():
        return render_template('results.html', name="Transportation")

    @app.route('/miscellaneous')
    def miscellaneous():
        return render_template('results.html', name="Miscellaneous/Other Services")

    return app
