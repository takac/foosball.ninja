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
    result_page = int(flask.request.args.get('page', '1'))
    page_size = 10
    player = db.player(player_id)
    if name is not None and not name == player['name'].lower():
        raise Exception("name does not match")

    scores = db.scores(player)
    offset = (result_page-1) * page_size
    results = db.results(player, offset=offset, limit=page_size)
    result_count = db.result_count(player)
    total_pages = int(result_count/page_size)
    if result_page < 0 or (total_pages > 1 and result_page > total_pages):
        raise Exception('cant be less than 0')

    return flask.render_template(
        'player.html', player=player, scores=scores,
        results=results, result_count=result_count,
        result_page=result_page, total_pages=total_pages,
        page_size=page_size,
        title='FOOS')
