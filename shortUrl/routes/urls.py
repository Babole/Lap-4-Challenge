from flask import Blueprint, request, Flask
from ..database.db import db
from ..models.url import Url

from flask_marshmallow import Marshmallow
import json

app = Flask(__name__)
ma = Marshmallow(app)

class urlSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "original_url", "short_url")


urls_schema = urlSchema()
urls_schema = urlSchema(many=True)

urls_routes = Blueprint("urls", __name__)

@urls_routes.route("/", methods=["GET", "POST"])
def urls():
    if request.method == "POST":
        body = request.get_json()
        print(body)
        original = body["original"]
        shorter = body["shorter"]

        url = Url(original_url=original, short_url=shorter)

        db.session.add(url)
        db.session.commit()
        return "URL added"
    else:
        all_urls = Url.query.all()
        return (json.dumps(urls_schema.dump(all_urls)))
