from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddEntrance(FlaskForm):

    name = StringField('Name of Entrance:')
    driving_time = IntegerField("Driving time in minutes:")
    submit = SubmitField('Add Entrance')

class DeleteEntrance(FlaskForm):

    id = IntegerField('Id Number of Entrance to Remove:')
    submit = SubmitField('Remove Entrance')
