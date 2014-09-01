import flask
import logging
import logging.handlers
from foosball.db import foosdb
from foosball.controller import controller

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

file_handler = logging.handlers.WatchedFileHandler('foosball.log')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

app = flask.Flask('foosball')
app.config.from_object('config.Config')
app.db = foosdb.FoosDatabase(app)

app.register_blueprint(controller)
