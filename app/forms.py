from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):
    """
    The form for entering values for prediction of movie box value. We need to figure out what values we
    should use and what we can leave as median values.
    (features missing in the form are set to default values in `predict.py`).


    choices=[(186, 'Comedy'), ('Family', 'Family'), ('Action', 'Action'),
                                      ('Adventure', 'Adventure'), ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'),
                                      (266, 'Drama'), ('Romance', 'Romance'), ('Mystery', 'Mystery'),
                                      ('Crime', 'Crime'), ('Animation', 'Animation'), ('Horror', 'Horror'),
                                      ('Documentary', 'Documentary'), ('Family Music', 'Family Music'),
                                      ('Foreign', 'Foreign'), ('Western', 'Western')])
    """
    budget = IntegerField('Movie budget', validators=[DataRequired()])

    all_genres = SelectField('Movie in one of the following genres',
                             choices=[(305, 'Something'), (186, 'Comedy'), (266, 'Drama')])

    runtime = IntegerField('Movie runtime', validators=[DataRequired()])

    popularity = FloatField('Move popularity', validators=[DataRequired()])

    tagline = BooleanField(label='Move have a tagline')

    belongs_to_collection = BooleanField(label='Move belongs to collection')

    original_language = SelectField('Select original language',
                                    choices=[(7, 'English'), (2, 'Korean'), (11, 'French'), (16, 'Italian'),
                                             (13, 'Hindi'), (27, 'Russian'), (8, 'Spanish'), (17, 'Japanese'),
                                             (18, 'Chinese')])

    production_countries = SelectField('Select production country',
                                       choices=[(275, 'USA'), (204, 'GreatBritain'),
                                                (233, 'India'), (0, 'France')])

    release_year = IntegerField('Year of release', validators=[DataRequired()])

    release_month = IntegerField('Month of release', validators=[DataRequired()])

    submit = SubmitField('Submit')
