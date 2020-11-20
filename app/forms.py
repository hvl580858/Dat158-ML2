from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, \
    SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class DataForm(FlaskForm):
    """
    The form for entering values for prediction of movie box value.
    All values that are needed for prediction will be here as we removed a lot.
    """
    name = StringField('Enter movie name')

    budget = IntegerField('Movie budget', validators=[InputRequired()])

    all_genres = SelectField('Movie in one of the following genres',
                             choices=[(305, 'Romantic Drama Comedy'), (186, 'Comedy'), (266, 'Drama'),
                                      (520, 'Horror Thriller'), (480, 'Porn')])

    runtime = FloatField('Movie runtime', validators=[DataRequired()])

    popularity = FloatField('Movie popularity', validators=[DataRequired()])

    tagline = BooleanField(label='Movie have a tagline')

    belongs_to_collection = BooleanField(label='Movie belongs to collection')

    original_language = SelectField('Select original language',
                                    choices=[(7, 'English'), (2, 'Korean'), (11, 'French'), (16, 'Italian'),
                                             (13, 'Hindi'), (27, 'Russian'), (8, 'Spanish'), (17, 'Japanese'),
                                             (18, 'Chinese')])

    production_countries = SelectField('Select production country',
                                       choices=[(275, 'USA'), (222, 'USA & UK'), (204, 'United Kingdom'),
                                                (233, 'India'), (176, 'France'), (241, 'Russia'), (151, 'Germany'),
                                                (216, 'China')])

    release_year = IntegerField('Year of release', validators=[DataRequired()])

    release_month = IntegerField('Month of release', validators=[DataRequired()])

    submit = SubmitField('Submit')
