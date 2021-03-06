from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from ..models import Blog,Comment
from wtforms.validators import DataRequired

class UpdateProfileForm(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class FlyingForm(FlaskForm):
    body = TextAreaField("Blog Description",validators=[DataRequired()])
    submit = SubmitField('Submt')

class AdventureForm(FlaskForm):
    body = TextAreaField("Blog Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class CruiseForm(FlaskForm):
    body = TextAreaField("Blog Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class GlampingForm(FlaskForm):
    body = TextAreaField("Blog Description",validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    body = TextAreaField("Comment Description",validators=[DataRequired()])
    submit = SubmitField('Submit')