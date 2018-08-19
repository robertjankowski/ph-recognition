import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('predict', __name__, url_prefix='/predict')


@bp.route('/', methods=('GET', 'POST'))
def predict():
    if request.method == 'POST':
        blue = int(request.form['blue'])
        red = int(request.form['red'])
        green = int(request.form['green'])

        error = None

        if not blue:
            error = 'Blue color is required'
        elif not red:
            error = 'Red color is required'
        elif not green:
            error = 'Green color is required'

        if blue < 0 and blue > 255:
            error = 'Range 0 to 255'
        if red < 0 and red > 255:
            error = 'Range 0 to 255'
        if green < 0 and red > 255:
            error = 'Range 0 to 255'
        
        # TODO 
        # return render_template('result.html')
        return redirect('predict/result')

        flash(error)

        
        # TODO
        # 1. complete predicting
        # 2. return new view

    return render_template('predict.html')


