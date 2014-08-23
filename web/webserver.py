#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from collections import namedtuple
import sqlite3
import pystache
import os

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
            score_query = ('SELECT COUNT(id) FROM game WHERE '
                           'winner = {player_one.id} AND opponent = {player_two.id}')

            cursor.execute(score_query.format(player1=players[0], player2=players[1]))
            score_one = cursor.fetchone()[0]
            cursor.execute(score_query.format(player1=players[1], player2=players[0]))
            return (score_one, cursor.fetchone()[0])

    def player(self, id):
        cursor = conn.cursor()
        player_query = 'SELECT name FROM player WHERE id = {}'.format(id)
        cursor.execute(player_query)
        return { 'name': cursor.fetchone()[0], 'id': id }

db = FoosDatabase('foosball.db')

class MyHandler(BaseHTTPRequestHandler):
        
    def render_template(self, template_name, *args, **kwargs):
        data = open('web/templates/' + template_name, 'r').read()
        return pystache.render(data, *args, **kwargs)

    # Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(self.render_template('home.html', players=db.players(), title='FOOS'))

        elif self.path.startswith('/player/'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            scores = { 'opponent': {'name': 'Matt'}, 'opponent_score': 1, 'player_score': 2}
            self.wfile.write(self.render_template('player.html', player=db.player(1), scores=scores,title='FOOS'))
            
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
            
