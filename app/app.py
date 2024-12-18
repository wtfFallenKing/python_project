import flask
import flask_cors
from db.routes import main_route, card_route, deck_route
from db.app import create_db, init_data_db


app = flask.Flask(__name__)


create_db()
init_data_db()


@app.route("/")
@flask_cors.cross_origin()
def index():
  return main_route()


@app.route("/card/<card_name>")
@flask_cors.cross_origin()
def card(card_name):
  return card_route(card_name=card_name)

@app.route("/deck")
@flask_cors.cross_origin()
def deck():
  return deck_route()