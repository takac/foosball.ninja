import flask

class Blueprint(flask.Blueprint):
    def register(self, app, options, first_registration=False):
        self.config = app.config
        self.db = app.db
        super(Blueprint, self).register(app, options, first_registration)

