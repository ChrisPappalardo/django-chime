# -*- coding: utf-8 -*-

'''
django_chime/core
-----------------

core functions for the django-chime app
'''

import altair as alt

from penn_chime.view.charts import (
    build_admits_chart,
    build_census_chart,
    build_sim_sir_w_date_chart,
    build_table,
)
from penn_chime.model.parameters import Parameters
from penn_chime.model.sir import Sir


class ShortID(object):
    '''
    short id property
    '''

    @property
    def short_id(self):
        return str(self.id)[-8:]


def is_number(s):
    '''
    returns True if s is a number, False otherwise
    '''

    if s is None:
        return False

    try:
        float(s)
        return True

    except ValueError:
        return False


def get_chime_model(parameters):
    '''
    instantiates and returns CHIME model using parameters
    '''

    if not isinstance(parameters, Parameters):
        t = type(parameters)
        raise TypeError(f'parameters must be a Parameters object not {t}')

    return Sir(parameters)


def build_charts(model, width='container', padding={'right': 50}):
    '''
    builds CHIME charts
    '''

    charts = list()

    for fcn, attr in (
            (build_admits_chart, 'admits_floor_df'),
            (build_census_chart, 'census_floor_df'),
            (build_sim_sir_w_date_chart, 'sim_sir_w_date_floor_df'),
    ):
        charts.append({
            'chart': fcn(
                **{
                    'alt': alt,
                    attr: getattr(model, attr),
                },
            ).properties(
                width=width,
                padding=padding,
            ).to_json(),
        })

    return charts


def build_tables(model, labels):
    '''
    builds CHIME tables
    '''

    tables = list()

    for title, desc, attr in (
            (
                'New Admissions',
                'Projected number of daily COVID-19 admissions.',
                'admits_floor_df'
            ),
            (
                'Admitted Patients (Census)',
                'Projected census of COVID-19 patients, accounting for arrivals and discharges.',  # noqa: E501
                'census_floor_df',
            ),
            (
                'Susceptible, Infected, and Recovered',
                'The number of susceptible, infected, and recovered individuals in the hospital catchment region at any given moment.',  # noqa: E501
                'sim_sir_w_date_floor_df',
            ),
    ):

        df = getattr(model, attr)

        columns = [{'field': c, 'title': c} for c in df.columns]
        data = build_table(df=df, labels=labels)

        tables.append({
            'title': title,
            'desc': desc,
            'id': attr,
            'columns': columns,
            'data': data.to_json(orient='records'),
        })

    return tables
