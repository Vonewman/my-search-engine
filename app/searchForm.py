from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SeachForm(FlaskForm):
    searchbox = StringField('Que cherchez vous?', validators=[DataRequired()])
    submit = SubmitField('Search')