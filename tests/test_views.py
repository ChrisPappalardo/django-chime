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

from django_chime.models import ChimeSite


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
