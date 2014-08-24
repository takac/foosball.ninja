#!/usr/bin/python
import flask
from foosball import db

blueprint = flask.Blueprint('main', __name__)


# Handler for the GET requests
@blueprint.route('/')
def home():
    return flask.render_template(
        'home.html', players=db.players(), title='FOOS')


@blueprint.route('/player/<int:player_id>/<string:name>')
@blueprint.route('/player/<int:player_id>')
def player(player_id, name=None):
    player = db.player(player_id)
    scores = db.scores(player)
    return flask.render_template(
        'player.html', player=player, scores=scores, title='FOOS')
