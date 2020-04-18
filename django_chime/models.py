# -*- coding: utf-8 -*-

'''
django_chime/models
-------------------

models for the django-chime app
'''

import datetime as dt
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import (
    BigIntegerField,
    CASCADE,
    CharField,
    DateField,
    DateTimeField,
    FileField,
    FloatField,
    ForeignKey,
    IntegerField,
    Model,
    UUIDField,
)
from django.utils import timezone

from penn_chime.constants import EPSILON
from penn_chime.parameters import Parameters, Disposition

from .core import ShortID


User = get_user_model()


class ChimeSite(ShortID, Model):
    '''
    chime site model
    '''

    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(null=True, default=None)

    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=255)

    population = BigIntegerField(
        default=3600000,
        validators=[MinValueValidator(1)],
        help_text='Regional population',
    )
    current_hospitalized = BigIntegerField(
        default=69,
        validators=[MinValueValidator(0)],
        help_text='Currently hospitalized COVID-19 patients',
    )
    date_first_hospitalized = DateField(
        null=True,
        blank=True,
        help_text='Date of first hospitalized COVID-19 case, if known',
    )
    doubling_time = FloatField(
        default=4.0,
        validators=[MinValueValidator(0.0)],
        help_text='Doubling time in days (up to today)',
    )
    hospitalized_days = IntegerField(
        default=7,
        validators=[MinValueValidator(0)],
        help_text='Average hospital length of stay (in days)',
    )
    hospitalized_rate = FloatField(
        default=0.025,
        validators=[MinValueValidator(0.00001), MaxValueValidator(1.0)],
        help_text='Hospitalization %(total infections)',
    )
    icu_days = IntegerField(
        default=9,
        validators=[MinValueValidator(0)],
        help_text='Average days in ICU',
    )
    icu_rate = FloatField(
        default=0.0075,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='ICU %(total infections)',
    )
    infectious_days = IntegerField(
        default=14,
        validators=[MinValueValidator(0)],
        help_text='Infectious days',
    )
    market_share = FloatField(
        default=0.15,
        validators=[MinValueValidator(0.00001), MaxValueValidator(1.0)],
        help_text='Hospital market share %',
    )
    n_days = IntegerField(
        default=100,
        validators=[MinValueValidator(0)],
        help_text='Number of days to project',
    )
    mitigation_date = DateField(
        blank=True,
        default=timezone.localdate,
        help_text='Date social distancing measures went into effect',
    )
    relative_contact_rate = FloatField(
        default=0.30,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='Social distancing (% reduction in social contact going forward)',
    )
    ventilated_days = IntegerField(
        default=10,
        validators=[MinValueValidator(0)],
        help_text='Average days on ventilator',
    )
    ventilated_rate = FloatField(
        default=0.005,
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
        help_text='Ventilated %(total infections)',
    )

    def __str__(self):
        return f'{self.name} {self.short_id} {self.created:%Y-%m-%d}'

    @property
    def parameters(self):
        '''
        return penn_chime Parameters object populated with instance values
        '''

        doubling_time = self.doubling_time

        if self.date_first_hospitalized:
            doubling_time = None

        mitigation_date = self.mitigation_date
        relative_contact_rate = max(self.relative_contact_rate, EPSILON)

        if relative_contact_rate == EPSILON:
            mitigation_date = None

        return Parameters(
            current_date=timezone.localdate(),
            population=self.population,
            current_hospitalized=self.current_hospitalized,
            date_first_hospitalized=self.date_first_hospitalized,
            doubling_time=doubling_time,
            hospitalized=Disposition(
                days=self.hospitalized_days,
                rate=self.hospitalized_rate,
            ),
            icu=Disposition(
                days=self.icu_days,
                rate=self.icu_rate,
            ),
            infectious_days=self.infectious_days,
            market_share=self.market_share,
            n_days=self.n_days,
            mitigation_date=mitigation_date,
            relative_contact_rate=relative_contact_rate,
            ventilated=Disposition(
                days=self.ventilated_days,
                rate=self.ventilated_rate,
            ),
            recovered=0,  # not implemented
        )
