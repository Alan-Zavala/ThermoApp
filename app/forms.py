from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateTimeField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from app.models import Element

class InWaterForm(FlaskForm):
    m_water = FloatField('Mass of water', validators=[InputRequired()])
    t_water = FloatField('Temperature of water', validators=[InputRequired()])
    c_object = FloatField('Specific Heat of object', validators=[InputRequired()])
    m_object = FloatField('Mass of object', validators=[InputRequired()])
    t_object = FloatField('Temperature of object', validators=[InputRequired()])
    submit = SubmitField("Calculate Final Temperature")

class InContactForm(FlaskForm):
    m_1 = FloatField('Mass 1', validators=[InputRequired()])
    t_1 = FloatField('Temperature 1', validators=[InputRequired()])
    c_1 = FloatField('Specific Heat 1', validators=[InputRequired()])
    m_2 = FloatField('Mass 2', validators=[InputRequired()])
    t_2 = FloatField('Temperature 2', validators=[InputRequired()])
    c_2 = FloatField('Specific Heat 2', validators=[InputRequired()])
    submit = SubmitField("Calculate Final Temperature")

class InMarsForm(FlaskForm):
    m_water = FloatField('Mass of water', validators=[InputRequired()])
    t_water = FloatField('Temperature of water', validators=[InputRequired()])
    c_object = FloatField('Specific Heat of object', validators=[InputRequired()])
    m_object = FloatField('Mass of object', validators=[InputRequired()])
    t_object = FloatField('Temperature of object', validators=[InputRequired()])
    submit = SubmitField("Calculate Final Temperature")
