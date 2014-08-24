import sqlite3
import os
import jinja2


class FoosDatabase(object):
    def __init__(self, db_file):
        self.db_file = db_file
        if os.path.isfile(db_file):
            self.conn = sqlite3.connect(db_file)
        else:
            raise Exception('cannot find db file "{}"'.format(db_file))

    def players(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        player_query = 'SELECT id, name FROM player'
        cursor.execute(player_query)
        return [dict(name=i[1], id=i[0]) for i in cursor.fetchall()]

    def score(self, player_one, player_two):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        score_query = jinja2.Template('SELECT COUNT(id) FROM game WHERE '
                                      'winner = {{player_one.id}} AND '
                                      'opponent = {{player_two.id}}')
        cursor.execute(score_query.render(player_one=player_one,
                                          player_two=player_two))
        score_one = cursor.fetchone()[0]
        cursor.execute(score_query.render(player_one=player_two,
                                          player_two=player_one))
        return (score_one, cursor.fetchone()[0])

    def player(self, id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        player_query = 'SELECT name FROM player WHERE id = {}'.format(id)
        cursor.execute(player_query)
        return {'name': cursor.fetchone()[0], 'id': id}

    def opponents(self, player):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        opponent_query = jinja2.Template(
            'select distinct opponent from '
            '(select winner, opponent '
            'from game where winner = {{player.id}} union all '
            'select opponent, winner from game where opponent = '
            '{{player.id}})')

        # return player id
        cursor.execute(opponent_query.render(player=player))
        return [self.player(i[0]) for i in cursor.fetchall()]

    def scores(self, player):
        scores = []
        for i in self.opponents(player):
            player_score, opponent_score = self.score(player, i)
            scores.append({'opponent': i, 'opponent_score': opponent_score,
                          'player_score': player_score})
        return scores
