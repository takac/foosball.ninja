import sqlite3
import logging
import jinja2
from flask import g

logger = logging.getLogger(__name__)

class FoosDatabase(object):
    def __init__(self, app):
        self.app = app

        @app.teardown_appcontext
        def close_connection(exception):
            db = getattr(g, '_database', None)
            if db is not None:
                logger.debug('closing db connection')
                db.close()

    def get_db(self):
        db = getattr(g, '_database', None)
        if db is None:
            logger.debug('creating db connection')
            db = g._database = sqlite3.connect(
                self.app.config['DATABASE'], detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            db.row_factory = sqlite3.Row
        return db
    

    def query_db(self, query, *args, **kwargs):
        cursor = self.get_db().cursor()
        q = jinja2.Template(query).render(*args, **kwargs)
        cursor.execute(q)
        rv = cursor.fetchall()
        cursor.close()
        return rv

    def players(self):
        player_query = 'SELECT id, name FROM player'
        return [dict(name=row['name'], id=row['id'])
                for row in self.query_db(player_query)]

    def score(self, player_one, player_two):
        score_query = ('SELECT COUNT(id) FROM game WHERE '
                       'winner = {{player_one.id}} AND '
                       'opponent = {{player_two.id}}')
        score_one = self.query_db(
            score_query, player_one=player_one, player_two=player_two)[0]
        score_two = self.query_db(
            score_query, player_one=player_two, player_two=player_one)[0]
        return (score_one[0], score_two[0])

    def player(self, id):
        cursor = self.get_db().cursor()
        player_query = 'SELECT name FROM player WHERE id = {}'.format(id)
        cursor.execute(player_query)
        return {'name': cursor.fetchone()[0], 'id': id}

    def opponents(self, player):
        opponent_query = ('select distinct opponent from '
                          '(select winner, opponent '
                          'from game where winner = {{player.id}} union all '
                          'select opponent, winner from game where opponent = '
                          '{{player.id}})')

        # return player id
        rows = self.query_db(opponent_query, player=player)
        return [self.player(i[0]) for i in rows]

    def scores(self, player):
        scores = []
        for i in self.opponents(player):
            player_score, opponent_score = self.score(player, i)
            scores.append({'opponent': i, 'opponent_score': opponent_score,
                          'player_score': player_score})
        return scores

    def result_count(self, player):
        result_count_query = ('select COUNT(*) from '
                              '(select winner '
                              'from game where winner = {{player.id}} '
                              'union all select winner from '
                              'game where opponent = {{player.id}})')

        return self.query_db(result_count_query, player=player)[0][0]

    def results(self, player, offset=0, limit=20, epoch=False):
        result_query = ('select winner, opponent, gamedate as "[timestamp]" from '
                        '(select winner, opponent, gamedate '
                        'from game where winner = {{player.id}} union all '
                        'select winner, opponent, gamedate from '
                        'game where opponent = {{player.id}}) '
                        'order by gamedate desc limit {{limit}} '
                        'offset {{offset}}')
        rows = self.query_db(
            result_query, player=player, offset=offset, limit=limit)
        translated_rows = []
        for row in rows:
            r = {}
            if row['winner'] == player['id']:
                r['opponent'] = self.player(row['opponent'])
                r['won'] = True
            else:
                r['opponent'] = self.player(row['winner'])
                r['won'] = False
            # For some reason col 2 lost its key
            r['gamedate'] = row[2] if not epoch else row[2].strftime('%s')
            translated_rows.append(r)
        return translated_rows
