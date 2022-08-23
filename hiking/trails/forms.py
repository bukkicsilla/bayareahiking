from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddTrail(FlaskForm):

    name = StringField('Name of Trail:')
    entrance_id = IntegerField("Id of Entrance: ")
    submit = SubmitField('Add Trail')
