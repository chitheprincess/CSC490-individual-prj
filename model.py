from wtforms import Form, FloatField, validators, StringField
from math import pi


class InputForm(Form):
    L = FloatField(
        label='Length of the rod', default=1.0,
        validators=[validators.InputRequired()])

    delta_x = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])

    T = FloatField(
        label='Time', default=pi,
        validators=[validators.InputRequired()])

    delta_t = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])

    beta = FloatField(
        label='Beta', default=1,
        validators=[validators.InputRequired()])

    initial_condition = StringField(
        'Initial Condition', default="sin(x)",
        validators=[validators.InputRequired()])

    boundary_1 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])

    boundary_2 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])
