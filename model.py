from wtforms import Form, FloatField, validators, StringField, TextField
from math import pi
import math


def check_delta_T(form, field):
    """Form validation: failure if delta_t  > T ."""
    T = form.T.data
    delta_t = field.data
    print(type(T))
    if type(T) == float and type(delta_t) == float:
        if T < delta_t:
            raise validators.ValidationError(
                'Delta_t has to be smaller than T')


def check_delta_X(form, field):
    """Form validation: failure if delta_t  > T ."""
    L = form.L.data
    delta_x = field.data
    if type(L) == float and type(delta_x) == float:
        if L < delta_x:
            raise validators.ValidationError(
                'Delta_x has to be smaller than L')


class HeatForm(Form):
    L = FloatField(
        label='Length of the rod', default=pi,
        validators=[validators.InputRequired()])
    delta_x = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired(), check_delta_X])
    T = FloatField(
        label='Time', default=1,
        validators=[validators.InputRequired()])
    delta_t = FloatField(
        label='Time step size', default=0.01,
        validators=[validators.InputRequired(), check_delta_T])
    beta = FloatField(
        label='Beta', default=1,
        validators=[validators.InputRequired()])
    f_x = TextField(
        'Initial Condition', default="math.sin(x)",
        validators=[validators.InputRequired()])
    boundary_1 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])
    boundary_2 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])


class WaveForm(Form):
    L = FloatField(
        label='Length of the string', default=1,
        validators=[validators.InputRequired()])
    delta_x = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired(), check_delta_X])
    T = FloatField(
        label='Time', default=1,
        validators=[validators.InputRequired()])
    delta_t = FloatField(
        label='Time step size', default=0.005,
        validators=[validators.InputRequired(), check_delta_T])
    c = FloatField(
        label='c', default=1,
        validators=[validators.InputRequired()])
    f_x = TextField(
        'Initial_condition', default="math.sin(pi*x)",
        validators=[validators.InputRequired()])
    g_x = TextField(
        'Intial_velocity', default="0",
        validators=[validators.InputRequired()])
    boundary_1 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])
    boundary_2 = FloatField(
        label='Boundary condition', default=0,
        validators=[validators.InputRequired()])
