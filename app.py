from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from setup_db import db
from config import Config
from dao.model.place import Place
from views.places import place_ns
from utils import get_data_from_json


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    registration_extensions(application)
    return application


def registration_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(place_ns)
    create_data(application, db)


def create_data(application, db):
    with application.app_context():
        db.drop_all()
        db.create_all()

        for place in get_data_from_json():
            place_data = Place(**place)
            db.session.add(place_data)
            db.session.commit()


app = create_app(Config())


@app.errorhandler(404)
def error_404(error):
    return f"Page not found. Error: {error}", 404


@app.errorhandler(500)
def error_500(error):
    return f"Internal Server Error. Error: {error}", 500


CORS(app)
cors = CORS(resources={
    r"/*": {"origins": '*'}
})

if __name__ == '__main__':
    app.run(port=8008)
