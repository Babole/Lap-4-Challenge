from ..database.db import db

class Url(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(80))
    short_url = db.Column(db.String(500))