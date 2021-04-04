from wtforms import Form, FloatField, validators
from math import pi


class InputForm(Form):
    L = FloatField(
        label='Length of the rod', default=1.0,
        validators=[validators.InputRequired()])

    Delta_x = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])

    T = FloatField(
        label='Time', default=pi,
        validators=[validators.InputRequired()])

    Delta_t = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])

    Beta = FloatField(
        label='Beta', default=1,
        validators=[validators.InputRequired()])
