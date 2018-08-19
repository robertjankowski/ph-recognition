import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('predict', __name__, url_prefix='/predict')


@bp.route('/', methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        blue = request.form['blue']
        red = request.form['red']
        green = request.form['green']

        error = None

        if not blue:
            error = 'Blue color is required'
        elif not red:
            error = 'Red color is required'
        elif not green:
            error = 'Green color is required'

        # TODO
        # 1. complete predicting
        # 2. return new view

    return render_template('predict.html')
