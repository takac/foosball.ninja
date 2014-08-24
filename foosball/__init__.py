import flask
from foosball import foosdb

app = flask.Flask('foosball')
app.debug = True

db = foosdb.FoosDatabase('foosball.db')

from foosball.controller import blueprint

app.register_blueprint(blueprint)
