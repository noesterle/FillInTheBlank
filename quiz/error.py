from flask import render_template

# @app.errorhandler(404)
def page_not_found(error):
    print("Error",error)
    return render_template('not_found.jinja', error=error), 404