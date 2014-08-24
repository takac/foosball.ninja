import flask

app = flask.Flask('foosball')
app.config.from_object('config.Config')

from foosball import foosdb
db = foosdb.FoosDatabase()
from foosball.controller import blueprint


app.register_blueprint(blueprint)
