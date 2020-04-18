#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for the models module in the django_chime package
----
'''

import unittest
from uuid import UUID
from django_chime.models import ChimeSite
from penn_chime.models import Parameters
from django.utils import timezone


class TestDjango_chime_models(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_chimesite_model_defaults(self):
        '''
        Tests the chimesite model field defaults
        '''

        chime_model = ChimeSite()

        self.assertIsInstance(chime_model.id, UUID)
        self.assertEqual(chime_model.name, '')
        self.assertEqual(chime_model.population, 3600000)
        self.assertEqual(chime_model.current_hospitalized, 69)
        self.assertEqual(chime_model.date_first_hospitalized, None)
        self.assertEqual(chime_model.doubling_time, 4.0)
        self.assertEqual(chime_model.hospitalized_days, 7)
        self.assertEqual(chime_model.hospitalized_rate, 0.025)
        self.assertEqual(chime_model.icu_days, 9)
        self.assertEqual(chime_model.icu_rate, 0.0075)
        self.assertEqual(chime_model.infectious_days, 14)
        self.assertEqual(chime_model.market_share, 0.15)
        self.assertEqual(chime_model.n_days, 100)
        self.assertEqual(chime_model.mitigation_date, timezone.localdate())
        self.assertEqual(chime_model.relative_contact_rate, 0.30)
        self.assertEqual(chime_model.ventilated_days, 10)
        self.assertEqual(chime_model.ventilated_rate, 0.005)
        self.assertIsInstance(chime_model.parameters, Parameters)
