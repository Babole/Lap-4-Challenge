from flask import Blueprint, request, Flask, render_template, redirect, url_for
from ..database.db import db
from ..models.url import Url
from  ..url_generator.shortenURL import id_generator

urls_routes = Blueprint("urls", __name__)

@urls_routes.route("/", methods=["GET", "POST"])
def urls():
    if request.method == "POST":
        original = request.form["original_URL"]
        shorten_URL = id_generator()
        url = Url(original_url=original, short_url=shorten_URL)

        db.session.add(url)
        db.session.commit()
        return render_template("home.html", original_URL = original, shorten_URL = shorten_URL), 201
    else:
        return render_template("home.html" ), 200

@urls_routes.route("/<shorten_URL>")
def redirect(shorten_URL):
    if request.method == 'GET':
        url_data = Url.query.filter_by(short_url = shorten_URL).first()
        original = "http://"+url_data.original_url
        return render_template("redirect.html", original_URL = original)

