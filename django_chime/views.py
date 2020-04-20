# -*- coding: utf-8 -*-

'''
django_chime/views
------------------

views for the django-chime app
'''

import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from djcorecap.views import is_logged_in

from penn_chime.constants import DOCS_URL

from .core import get_chime_model, build_charts, build_tables
from .forms import ChimeSiteCreateForm
from .models import ChimeSite


logger = logging.getLogger('django')


class BaseContextMixin(object):
    '''
    mixin to add basic data to context
    '''

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contact'] = settings.ADMINS[0][1]
        context['docs_url'] = DOCS_URL
        return context


class SuccessMixin(SuccessMessageMixin):
    '''
    mixin to enable success messages and next parameter handling
    '''

    def get_success_url(self, *args, **kwargs):

        if self.request.GET.get('next', None):
            return self.request.GET.get('next', None)

        if getattr(self, 'success_url', None) is None:
            return self.request.path

        return super().get_success_url(*args, **kwargs)


class ChimeSiteView(DetailView):
    '''
    chime site view
    '''

    model = ChimeSite

    def get_context_data(self, **kwargs):
        '''
        inject penn_chime model charts and tables
        '''

        context = super().get_context_data(**kwargs)

        parameters = self.object.parameters

        model = get_chime_model(parameters)

        charts = build_charts(model)
        tables = build_tables(model, parameters.labels)

        context['groups'] = [
            dict(list(a.items()) + list(b.items()))
            for a, b in zip(charts, tables)
        ]

        return context


@is_logged_in
class ChimeSiteListView(BaseContextMixin, ListView):
    '''
    chime site list view
    '''

    model = ChimeSite

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


@is_logged_in
class ChimeSiteCreateView(BaseContextMixin, SuccessMixin, CreateView):
    '''
    chime site create view
    '''

    model = ChimeSite
    form_class = ChimeSiteCreateForm
    success_message = 'Successfully created CHIME app.'

    def form_valid(self, form):
        '''
        inject user
        '''

        m = form.save(commit=False)

        m.user = self.request.user
        m.save()

        return super().form_valid(form)


@is_logged_in
class ChimeSiteDeleteView(SuccessMixin, DeleteView):
    '''
    chime site delete view
    '''

    model = ChimeSite
    success_message = 'Successfully deleted CHIME app.'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        # TODO: is this necessary?
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


@is_logged_in
class ChimeSiteUpdateView(BaseContextMixin, SuccessMixin, UpdateView):
    '''
    pipeline update view
    '''

    model = ChimeSite
    form_class = ChimeSiteCreateForm
    success_message = 'Successfully updated CHIME app.'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
