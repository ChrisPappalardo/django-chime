#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
tests/test_forms
-----------------
unit tests for django_chime forms
'''

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model

from django_chime.models import ChimeSite
from django_chime.forms import ChimeSiteCreateForm, PercentageField

User = get_user_model()


class TestDjango_chime_forms(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='testuser',
            password='testuser',
        )
        self.site = ChimeSite(user=user)
        self.data = {
            'name': 'testname',
            'population': 3600000,
            'current_hospitalized': 69,
            'date_first_hospitalized': timezone.localdate(),
            'doubling_time': 4.0,
            'hospitalized_rate': 0.025,
            'hospitalized_days': 7,
            'icu_rate': 0.0075,
            'icu_days': 9,
            'infectious_days': 14,
            'market_share': 0.15,
            'n_days': 100,
            'mitigation_date': timezone.localdate(),
            'relative_contact_rate': 0.30,
            'ventilated_rate': 0.005,
            'ventilated_days': 10,
        }

    def tearDown(self):
        del self.site
        del self.data

    def test_chimesite_create_form_is_valid(self):
        '''
        Tests if the ChimeSiteCreateForm is a valid form
        '''

        site_form = ChimeSiteCreateForm(self.data, instance=self.site)
        self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_name_field_is_valid(self):
        '''
        Tests that the name field is not blank
        '''

        self.data['name'] = ''
        site_form = ChimeSiteCreateForm(self.data, instance=self.site)
        self.assertFalse(site_form.is_valid())

    def test_chimesite_create_form_population_field_validation(self):
        '''
        Tests if the population field validator is a minimum of 1
        '''

        for i in range(-5, 5):
            self.data['population'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 1:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_current_hospitalized_field_validation(self):
        '''
        Tests if the current_hospitalized field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['current_hospitalized'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_date_first_hospitalized_field_validation(self):
        '''
        Tests that the date_first_hospitalized field can be null
        '''

        self.data['date_first_hospitalized'] = None
        site_form = ChimeSiteCreateForm(self.data, instance=self.site)
        self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_doubling_time_field_validation(self):
        '''
        Tests if the doubling_time field validator is a minimum of 0.0
        '''

        test_params = [-0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

        for i in test_params:
            self.data['doubling_time'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0.0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_hospitalized_rate_field_validation(self):
        '''
        Tests if the hospitalized_rate field validator is a minimum of 0.001%
        and a maximum of 100%
        '''

        test_params = [0.0008, 0.0009, 0.001, 0.002, 0.003, 98, 99, 100, 101, 102]

        for i in test_params:
            self.data['hospitalized_rate'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0.001 or i > 100:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_hospitalized_days_field_validation(self):
        '''
        Tests if the hospitalized_days field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['hospitalized_days'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_icu_rate_field_validation(self):
        '''
        Tests if the icu_rate field validator is a minimum of 0.0%
        and a maximum of 100%
        '''

        test_params = [-0.2, -0.1, 0.0, 0.1, 0.2, 98, 99, 100, 101, 102]

        for i in test_params:
            self.data['icu_rate'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0 or i > 100:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_icu_days_field_validation(self):
        '''
        Tests if the icu_days field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['icu_days'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_infectious_days_field_validation(self):
        '''
        Tests if the infectious_days field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['infectious_days'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_market_share_field_validation(self):
        '''
        Tests if the icu_rate field validator is a minimum of 0.001%
        and a maximum of 100%
        '''

        test_params = [0.0008, 0.0009, 0.001, 0.002, 0.003, 98, 99, 100, 101, 102]

        for i in test_params:
            self.data['market_share'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0.001 or i > 100:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_n_days_field_validation(self):
        '''
        Tests if the n_days field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['n_days'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_mitigation_date_field_validation(self):
        '''
        Tests that the mitigation_date field can be blank
        '''

        self.data['mitigation_date'] = None
        site_form = ChimeSiteCreateForm(self.data, instance=self.site)
        self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_relative_contact_rate_field_validation(self):
        '''
        Tests if the relative_contact_rate field validator is a minimum of 0.001%
        and a maximum of 100%
        '''

        test_params = [-0.2, -0.1, 0.0, 0.1, 0.2, 98, 99, 100, 101, 102]

        for i in test_params:
            self.data['relative_contact_rate'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0 or i > 100:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_ventilated_rate_field_validation(self):
        '''
        Tests if the ventilated_rate field validator is a minimum of 0.001%
        and a maximum of 100%
        '''

        test_params = [-0.2, -0.1, 0.0, 0.1, 0.2, 98, 99, 100, 101, 102]

        for i in test_params:
            self.data['ventilated_rate'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0 or i > 100:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_chimesite_create_form_ventilated_days_field_validation(self):
        '''
        Tests if the ventilated_days field validator is a minimum of 0
        '''

        for i in range(-5, 5):
            self.data['ventilated_days'] = i
            site_form = ChimeSiteCreateForm(self.data, instance=self.site)

            if i < 0:
                self.assertFalse(site_form.is_valid())
            else:
                self.assertTrue(site_form.is_valid())

    def test_percentagefield_methods(self):
        '''
        Tests the custom PercentageField to_python and prepare_value methods
        '''

        percent_field = PercentageField()
        self.assertEqual(percent_field.to_python('100'), 1.0)
        self.assertEqual(percent_field.to_python(None), None)
        self.assertEqual(percent_field.prepare_value(1.0), '100.0')
        self.assertEqual(percent_field.prepare_value(None), None)
