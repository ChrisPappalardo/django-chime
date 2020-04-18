#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for the core module in the django_chime package
----
'''

import unittest
from unittest.mock import Mock
from django_chime.core import (
    is_number,
    get_chime_model,
    build_charts,
    build_tables,
)
from penn_chime.models import SimSirModel
from django_chime.models import ChimeSite


class TestDjango_chime_core(unittest.TestCase):

    def setUp(self):
        self.chime_model = get_chime_model(ChimeSite().parameters)

    def tearDown(self):
        del self.chime_model

    def test_is_number(self):
        '''
        Tests the is_number function return values
        '''

        expected_results = [
            (None, False),
            (5, True),
            (5.5, True),
            ('5', True),
            ('chime', False),
        ]

        for value, expected in expected_results:
            self.assertEqual(is_number(value), expected)

    def test_is_number_raises_exception(self):
        '''
        Tests if the is_number function throws exceptions with invalid input
        '''

        self.assertRaises(TypeError, is_number, [])
        self.assertRaises(TypeError, is_number, {})
        self.assertRaises(TypeError, is_number, ())

    def test_get_chime_model(self):
        '''
        Tests if the get_chime_model function returns a SimSirModel
        '''

        self.assertIsInstance(self.chime_model, SimSirModel)

    def test_get_chime_model_raises_exception(self):
        '''
        Tests if the get_chime_model throws a TypeError exception
        with a specific message
        '''

        mock_parameter = Mock()
        with self.assertRaises(TypeError) as context:
            get_chime_model(mock_parameter)

        self.assertEqual(
            "parameters must be a Parameters object not <class 'unittest.mock.Mock'>",
            str(context.exception)
        )

    def test_build_charts(self):
        '''
        Tests the build_charts function return values
        '''

        charts = build_charts(self.chime_model)
        self.assertIsInstance(charts, list)

        for chart in charts:
            self.assertIsInstance(chart, dict)
            self.assertIsNotNone(chart.get('chart'))

    def test_build_tables(self):
        '''
        Tests the build_tables function return values
        '''

        tables = build_tables(self.chime_model, {})
        self.assertIsInstance(tables, list)

        for table in tables:
            self.assertIsInstance(table, dict)
            self.assertIsNotNone(table.get('title'))
            self.assertIsNotNone(table.get('id'))
            self.assertIsNotNone(table.get('columns'))
            self.assertIsNotNone(table.get('data'))
