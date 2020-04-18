# -*- coding: utf-8 -*-

'''
django_chime/forms
------------------

forms for the django-chime app
'''

from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from django.forms.fields import FloatField, TextInput

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Field,
    Layout,
    Submit,
)
from djcorecap.forms import cancel

from .core import is_number
from .models import ChimeSite


class PercentageField(FloatField):
    '''
    custom percentage field
    '''

    widget = TextInput(attrs={"class": "percentInput"})

    def to_python(self, value):
        v = super().to_python(value)

        if is_number(v):
            return v/100

        return v

    def prepare_value(self, value):
        v = super().prepare_value(value)

        if is_number(v) and not isinstance(v, str):
            return str((float(v)*100))

        return v


class ChimeSiteCreateForm(ModelForm):
    '''
    chime site create form
    '''

    hospitalized_rate = PercentageField(
        initial=0.025,
        validators=[MinValueValidator(0.00001), MaxValueValidator(1.0)],
        help_text='Hospitalization %(total infections)',
    )
    icu_rate = PercentageField(
        initial=0.0075,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='ICU %(total infections)',
    )
    market_share = PercentageField(
        initial=0.15,
        validators=[MinValueValidator(0.00001), MaxValueValidator(1.0)],
        help_text='Hospital market share %',
    )
    relative_contact_rate = PercentageField(
        initial=0.30,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='Social distancing (% reduction in social contact going forward)',
    )
    ventilated_rate = PercentageField(
        initial=0.005,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='Ventilated %(total infections)',
    )

    class Meta:
        model = ChimeSite
        fields = [
            'name',
            'population',
            'current_hospitalized',
            'date_first_hospitalized',
            'doubling_time',
            'hospitalized_rate',
            'hospitalized_days',
            'icu_rate',
            'icu_days',
            'infectious_days',
            'market_share',
            'n_days',
            'mitigation_date',
            'relative_contact_rate',
            'ventilated_rate',
            'ventilated_days',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            *[
                Field(
                    f,
                    autocomplete='off',
                ) for f in self.fields
            ],
            FormActions(
                Submit('submit', 'Confirm'),
                cancel,
            ),
        )
