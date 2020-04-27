#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tests/test_models
-----------------
unit tests for django_chime models
'''

from uuid import UUID

from penn_chime.model.parameters import Parameters

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from django_chime.models import ChimeSite

User = get_user_model()


class TestDjango_chime_models(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='testuser',
            password='testuser',
        )
        self.site_model = ChimeSite(
            user=user,
            name='testuser',
            updated=timezone.now()
        )

    def tearDown(self):
        del self.site_model

    def test_site_model_defaults(self):
        '''
        Tests the chimesite model field defaults
        '''

        self.assertIsInstance(self.site_model.id, UUID)
        self.assertEqual(self.site_model.name, 'testuser')
        self.assertEqual(self.site_model.population, 3600000)
        self.assertEqual(self.site_model.current_hospitalized, 69)
        self.assertEqual(self.site_model.date_first_hospitalized, None)
        self.assertEqual(self.site_model.doubling_time, 4.0)
        self.assertEqual(self.site_model.hospitalized_days, 7)
        self.assertEqual(self.site_model.hospitalized_rate, 0.025)
        self.assertEqual(self.site_model.icu_days, 9)
        self.assertEqual(self.site_model.icu_rate, 0.0075)
        self.assertEqual(self.site_model.infectious_days, 14)
        self.assertEqual(self.site_model.market_share, 0.15)
        self.assertEqual(self.site_model.n_days, 100)
        self.assertEqual(self.site_model.mitigation_date, timezone.localdate())
        self.assertEqual(self.site_model.relative_contact_rate, 0.30)
        self.assertEqual(self.site_model.ventilated_days, 10)
        self.assertEqual(self.site_model.ventilated_rate, 0.005)
        self.assertIsInstance(self.site_model.parameters, Parameters)
