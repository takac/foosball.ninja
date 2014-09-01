#!/usr/bin/python
import flask
import logging
import foosball.blueprint

logger = logging.getLogger(__name__)

controller = foosball.blueprint.Blueprint('main', __name__)

# Handler for the GET requests
@controller.route('/')
def home():
    return flask.render_template(
        'players.html', players=controller.db.players(), title='FOOS', page_name='home')


@controller.route('/player/<int:player_id>/results.json')
def player_results(player_id):
    player = controller.db.player(player_id)
    result_count = controller.db.result_count(player)
    results = {'results': controller.db.results(player, offset=0, limit=result_count, epoch=True)}
    return flask.jsonify(results)


@controller.route('/player/<int:player_id>/graph/')
def player_graph(player_id):
    return flask.render_template('cumlativegraph.html',
        player=controller.db.player(player_id), title='FOOS');


@controller.route('/player/<int:player_id>/<string:name>/')
@controller.route('/player/<int:player_id>/')
def player(player_id, name=None):
    result_page = int(flask.request.args.get('page', '1'))
    page_size = 10
    player = controller.db.player(player_id)
    if name is not None and not name == player['name'].lower():
        raise Exception("name does not match")

    scores = controller.db.scores(player)
    offset = (result_page-1) * page_size
    results = controller.db.results(player, offset=offset, limit=page_size)
    result_count = controller.db.result_count(player)
    total_pages = int(result_count/page_size)
    if result_page < 0 or (total_pages > 1 and result_page > total_pages):
        raise Exception('cant be less than 0')

    return flask.render_template(
        'player.html', player=player, scores=scores,
        results=results, result_count=result_count,
        result_page=result_page, total_pages=total_pages,
        page_size=page_size,
        title='FOOS')
