#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from collections import namedtuple
import sqlite3
import jinja2
import os
import re

PORT_NUMBER = 8080

conn = sqlite3.connect('foosball.db')

class Player(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.scores = {}

class FoosDatabase(object):
    def __init__(self, foos_db_file):
        if os.path.isfile(foos_db_file):
            self.conn = sqlite3.connect(foos_db_file)
        else:
            raise Exception('cannot find db file "{}"'.format(foos_db_file))

    def players(self):
        cursor = conn.cursor()
        player_query = 'SELECT id, name FROM player'
        cursor.execute(player_query)
        return [ dict(name=i[1], id=i[0]) for i in cursor.fetchall() ]

    def score(self, player_one, player_two):
            cursor = conn.cursor()
            score_query = jinja2.Template('SELECT COUNT(id) FROM game WHERE '
                                          'winner = {{player_one.id}} AND opponent = {{player_two.id}}')
           
            cursor.execute(score_query.render(player_one=player_one, player_two=player_two))
            score_one = cursor.fetchone()[0]
            cursor.execute(score_query.render(player_one=player_two, player_two=player_one))
            return (score_one, cursor.fetchone()[0])

    def player(self, id):
        cursor = conn.cursor()
        player_query = 'SELECT name FROM player WHERE id = {}'.format(id)
        cursor.execute(player_query)
        return { 'name': cursor.fetchone()[0], 'id': id }
    
    def opponents(self, player):
        cursor = conn.cursor()
        opponent_query = jinja2.Template('select distinct opponent from (select winner, opponent '
                          'from game where winner = {{player.id}} union all '
                          'select opponent, winner from game where opponent = {{player.id}})')
        # return player id
        cursor.execute(opponent_query.render(player=player))
        return [ self.player(i[0]) for i in cursor.fetchall() ]

    def scores(self, player):
        scores = []
        for i in db.opponents(player):
            player_score, opponent_score = db.score(player, i)
            scores.append({'opponent':i, 'opponent_score':opponent_score, 'player_score':player_score})
        return scores

db = FoosDatabase('foosball.db')

class MyHandler(BaseHTTPRequestHandler):
        
    def render_template(self, template_name, **kwargs):
        data = jinja2.Template(open('web/templates/' + template_name, 'r').read())
        return data.render(**kwargs)

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(self.render_template('home.html', players=db.players(), title='FOOS'))

        # elif self.path.startswith('/player/'):
        elif re.match(r"/player/(\d+)/?", self.path):
            id = int(re.match(r"/player/(\d+)/?", self.path).group(1))
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            player = db.player(id)
            scores = db.scores(player)
            self.wfile.write(self.render_template('player.html', player=player, scores=scores,title='FOOS'))
            
        else:
            self.send_error(404,'File Not Found: %s' % self.path)

if __name__ == '__main__':
    try:
        server = HTTPServer(('', PORT_NUMBER), MyHandler)
        print 'Started httpserver on port ' , PORT_NUMBER
        server.serve_forever()

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
            
