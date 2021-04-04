from wtforms import Form, FloatField, validators, StringField, TextField
from math import pi
import math


class HeatForm(Form):
    L = FloatField(
        label='Length of the rod', default=pi,
        validators=[validators.InputRequired()])
    delta_x = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='Time', default=1,
        validators=[validators.InputRequired()])
    delta_t = FloatField(
        label='Space step size', default=0.01,
        validators=[validators.InputRequired()])
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
        validators=[validators.InputRequired()])
    T = FloatField(
        label='Time', default=1,
        validators=[validators.InputRequired()])
    delta_t = FloatField(
        label='Space step size', default=0.005,
        validators=[validators.InputRequired()])
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
