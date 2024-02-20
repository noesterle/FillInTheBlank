import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/quiz')

@bp.route("/start", methods={'GET'})
def quiz():
    return render_template("base.jinja", title="Fill In The Blank")