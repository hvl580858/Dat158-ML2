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

    rcount = IntegerField('Number of readmissions past 180 days', validators=[DataRequired()])
    gender = IntegerField('Gender. 0=Male, 1=Female', validators=[NumberRange(min=0, max=1)])

    bmi = FloatField('Average BMI during encounter')
    sodium = FloatField('Average sodium level during encounter')

    asthma = BooleanField(label='Asthma')
    irondef = BooleanField(label='Iron deficiency')
    depress = BooleanField(label='Depression')
    malnutrition = BooleanField(label='Malnutrition')

    submit = SubmitField('Submit')
