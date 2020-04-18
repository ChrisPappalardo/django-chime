# -*- coding: utf-8 -*-

'''
django_chime/urls
-----------------

urls for the django-chime app
'''

from django.urls import path

from .views import (
    ChimeSiteListView,
    ChimeSiteCreateView,
    ChimeSiteDeleteView,
    ChimeSiteUpdateView,
)


app_name = 'django_chime'


urlpatterns = [

    path(
        '',
        ChimeSiteListView.as_view(),
        name='list',
    ),

    path(
        'create/',
        ChimeSiteCreateView.as_view(),
        name='create',
    ),

    path(
        'delete/<uuid:pk>/',
        ChimeSiteDeleteView.as_view(),
        name='delete',
    ),

    path(
        'update/<uuid:pk>/',
        ChimeSiteUpdateView.as_view(),
        name='update',
    ),
]
