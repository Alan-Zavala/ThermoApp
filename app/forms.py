from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DecimalField, DateTimeField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired
from app.models import Element

class InWaterForm(FlaskForm):
    element1 = SelectField('Element', validators=[DataRequired()])