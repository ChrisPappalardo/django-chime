============
django-chime
============

.. image:: https://img.shields.io/pypi/v/django_chime.svg
        :target: https://pypi.python.org/pypi/django_chime

.. image:: https://img.shields.io/travis/ChrisPappalardo/django_chime.svg
        :target: https://travis-ci.org/ChrisPappalardo/django_chime

.. image:: https://readthedocs.org/projects/django-chime/badge/?version=latest
        :target: https://django-chime.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

COVID-19 Hospital Impact Model for Epidemics (CHIME) app for Django.

* Free software: MIT license
* Documentation: https://django-chime.readthedocs.io.


Features
--------

* Re-usable application for deploying CHIME models in a Django project
* Provides database models for assumption persistence
* Integrates with Django's user and auth infrastructure for privacy and security
* Fast and lightweight platform allows hosting many models on the same website
* Built using the latest `UPenn CHIME model <https://github.com/CodeForPhilly/chime>`_


Quickstart
----------

Installation
~~~~~~~~~~~~

Install the package from github using pip:

.. code-block:: console

   $ pip install git+https://github.com/ChrisPappalardo/django-chime.git

Or you can include it in your requirements file like so:

.. code-block:: none

   git+https://github.com/ChrisPappalardo/django-chime.git

Configuration
~~~~~~~~~~~~~

You will need to add the `django_chime` application to the `INSTALLED_APPS` setting of
your project's `settings.py` file:

.. code-block:: python

   INSTALLED_APPS = (
       ...
       'django_chime',
   )

This will make the models, views, and templates available in your project.

Views
~~~~~

To allow users to access the `django_chime` views, you will need to add a path
declaration to `urlpatterns` in your project `urls.py` like so:

.. code-block:: python

   from django_chime.views import ChimeSiteView

   ...

   path(
       "<uuid:pk>/",
       ChimeSiteView.as_view(),
       name='site',
   ),

   path(
       "chime/",
       include("django_chime.urls"),
   ),

Once logged in, users can navigate to `/chime/` to create and configure their
CHIME models.  Once created, the CHIME models are visible without authentication
at `/<ID of CHIME model>/`.

Credits
-------

The CHIME model and source code is Copyright © 2020, The Trustees of the University of Pennsylvania and was released for public use under the MIT License.  Please visit their `live application <https://penn-chime.phl.io/>`_ for more information.

The official UPenn CHIME project code base is being actively developed by `Code for Philly <https://github.com/CodeForPhilly>`_.  Please visit their `project on GitHub <https://github.com/CodeForPhilly/chime>`_ for more information.
