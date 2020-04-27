#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

tests/test_views
----------------

unit tests for django_chime views
'''

import logging

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.utils import timezone

from django_chime.models import ChimeSite
from django_chime.views import ChimeSiteView


User = get_user_model()

logging.getLogger('django.request').setLevel(logging.ERROR)


class TestViews(TestCase):

    def setUp(self):
        '''
        create two users with one chime site each
        '''

        self.users = list()
        self.sites = list()

        for i in range(2):
            user = User.objects.create_user(
                username=f'testuser{i}',
                password=f'testuser{i}',
            )
            site = ChimeSite(user=user)
            site.save()
            self.users.append(user)
            self.sites.append(site)

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
        pass

    def test_list_view(self):
        '''
        verify that users can list sites and only see sites they own
        '''

        for i in range(2):
            self.client.login(username=f'testuser{i}', password=f'testuser{i}')
            r = self.client.get('/')
            self.assertEqual(r.status_code, 200)
            n = 0 if i == 1 else 1
            self.assertNotIn(self.sites[n], r.context['object_list'])
            self.assertIn('contact', r.context)
            self.assertIn('docs_url', r.context)

    def test_delete_view_ok(self):
        '''
        verify that users can delete sites they own
        '''

        for i in range(2):
            self.client.login(username=f'testuser{i}', password=f'testuser{i}')
            r = self.client.get(f'/delete/{self.sites[i].id}/')
            self.assertEqual(r.status_code, 200)

    def test_delete_view_bad(self):
        '''
        verify that users cant delete sites they dont own
        '''

        for i in range(2):
            self.client.login(username=f'testuser{i}', password=f'testuser{i}')
            n = 0 if i == 1 else 1
            r = self.client.get(f'/delete/{self.sites[n].id}/')
            self.assertNotEqual(r.status_code, 200)

    def test_update_view_ok(self):
        '''
        verify that users can update sites they own
        '''

        for i in range(2):
            self.client.login(username=f'testuser{i}', password=f'testuser{i}')
            r = self.client.get(f'/update/{self.sites[i].id}/')
            self.assertEqual(r.status_code, 200)

    def test_update_view_bad(self):
        '''
        verify that users cant update sites they dont own
        '''

        for i in range(2):
            self.client.login(username=f'testuser{i}', password=f'testuser{i}')
            n = 0 if i == 1 else 1
            r = self.client.get(f'/update/{self.sites[n].id}/')
            self.assertNotEqual(r.status_code, 200)

    def test_create_view_success(self):
        '''
        verify the create view gets a success message and redirects
        '''

        self.client.login(username=f'testuser0', password=f'testuser0')
        r = self.client.post('/create/', self.data)
        messages = [str(m) for m in get_messages(r.wsgi_request)]
        self.assertEqual(r.status_code, 302)
        self.assertIn('Successfully created CHIME app.', messages)

    def test_create_view_form_error(self):
        '''
        verify the create view gives gives form error with invalid input
        '''

        self.data['population'] = -1
        self.client.login(username=f'testuser0', password=f'testuser0')
        r = self.client.post('/create/', self.data)
        self.assertEqual(r.status_code, 200)
        self.assertIn('population', r.context['form'].errors.as_data())

    def test_update_view_success(self):
        '''
        verify the update view gets a success message, redirects, and updates db
        '''

        self.data['population'] = 3500000
        self.client.login(username=f'testuser0', password=f'testuser0')
        r = self.client.post(f'/update/{self.sites[0].id}/', self.data)
        messages = [str(m) for m in get_messages(r.wsgi_request)]
        site = ChimeSite.objects.get(pk=self.sites[0].id)
        self.assertEqual(r.status_code, 302)
        self.assertIn('Successfully updated CHIME app.', messages)
        self.assertEqual(site.population, 3500000)

    def test_update_view_form_error(self):
        '''
        verify the update view gives gives form error with invalid input
        '''

        self.data['population'] = -1
        self.client.login(username=f'testuser0', password=f'testuser0')
        r = self.client.post(f'/update/{self.sites[0].id}/', self.data)
        self.assertEqual(r.status_code, 200)
        self.assertIn('population', r.context['form'].errors.as_data())

    def test_delete_view_success(self):
        '''
        verify the delete view gets a success message and redirects
        '''

        self.client.login(username=f'testuser0', password=f'testuser0')
        r = self.client.delete(f'/delete/{self.sites[0].id}/')
        messages = [str(m) for m in get_messages(r.wsgi_request)]
        self.assertEqual(r.status_code, 302)
        self.assertIn('Successfully deleted CHIME app.', messages)
