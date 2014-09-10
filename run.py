#!/usr/bin/env python
# encoding: utf-8

import argparse
from db.clean_db import clean
import flask
import logging
import logging.handlers
from foosball.db import foosdb
from foosball.controller import controller


logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)




parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--clean-db', '-c', action='store_true',
                   dest='clean_db',
                   help='rerun database schema and load sample data')
parser.add_argument('--debug', '-d', action='store_true',
                   dest='debug',
                   help='run the app in dev mode')
args = parser.parse_args()
app = flask.Flask('foosball')
app.debug = args.debug

if args.debug:
    logger.setLevel(logging.DEBUG)
    app.config.from_object('foosball.config.DebugConfig')
else:
    logger.setLevel(logging.INFO)
    app.config.from_object('foosball.config.Config')

file_handler = logging.handlers.WatchedFileHandler(app.config['LOG_FILE'])
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

if args.clean_db:
    clean()

app.db = foosdb.FoosDatabase(app)
app.register_blueprint(controller)

app.run(host='0.0.0.0', port=8080)
