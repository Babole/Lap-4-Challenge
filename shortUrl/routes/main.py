from flask import Blueprint, request, render_template
from ..database.db import db
from ..models.url import Url

main_routes = Blueprint("main", __name__)

@main_routes.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        # this would return all
        urls = Url.query.all()
        # return render_template(...)
    else:

        original = request.form["original_url"]
        # some code to shorten url
        new_url = Url(original_url=original, short_url=body)
        db.session.add(new_url)
        db.session.commit()

        #query to get the url that was just added
        # return render_template(...)