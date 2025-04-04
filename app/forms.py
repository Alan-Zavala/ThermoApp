from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateTimeField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from app.models import Element

class InWaterForm(FlaskForm):
    m_water = FloatField('Mass of water', validators=[InputRequired()])
    t_water = FloatField('Temperature of water', validators=[InputRequired()])
    c_subject = FloatField('Specific Heat of object', validators=[InputRequired()])
    m_subject = FloatField('Mass of object', validators=[InputRequired()])
    t_subject = FloatField('Temperature of object', validators=[InputRequired()])
    submit = SubmitField("Calculate Final Temperature")