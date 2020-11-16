from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    """
    The form for entering values for prediction of movie box value. We need to figure out what values we
    should use and what we can leave as median values.
    (features missing in the form are set to default values in `predict.py`).
    """
    budget = IntegerField('Movie budget', validators=[DataRequired(0)])

    genre = SelectField('Movie in one of the following genres', choices=[(0, 'Other'), (1, 'Family'), (1, 'Action'), (1, 'Adventure'), (1, 'Fantasy')])

    runtime = IntegerField('Movie runtime', validators=[DataRequired(), NumberRange(0)])

    popularity = FloatField('Move popularity', validators=[DataRequired(), NumberRange(0.0, 300.0)])

    tagline = BooleanField(label='Move have a tagline')

    belongs_to_collection = BooleanField(label='Move belongs to collection')

    homepage = BooleanField(label='Move have a webpage')

    orig_language = BooleanField(label='English is original language')

    release_year = IntegerField('Year of release', validators=[DataRequired(), NumberRange(1920)])

    release_month = IntegerField('Month of release', validators=[DataRequired(), NumberRange(1, 12)])

    submit = SubmitField('Submit')


