import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('search', __name__, url_prefix='/')

@bp.route("/search", methods={'GET'})
def quiz():
    return render_template("search.jinja", title="Artist Search")