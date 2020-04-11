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

Check out a live demo of django-chime at
`https://chime.pappanaka.com <https://chime.pappanaka.com>`_!  Register for an
account (it's free - you just need to confirm an email address) and create your
custom CHIME app instance in minutes.


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

   git+https://github.com/ChrisPappalardo/django-chime.git@master#egg=django-chime

Configuration
~~~~~~~~~~~~~

You will need to add the :literal:`django_chime` application to the
:literal:`INSTALLED_APPS` setting of your project's :literal:`settings.py` file:

.. code-block:: python

   INSTALLED_APPS = (

       ...

       'django_chime',
   )

This will make the models, views, and templates available in your project.

You will also need to migrate your database to use the django-chime models:

.. code-block:: console

   $ python manage.py migrate

Views
~~~~~

To allow users to access the django-chime views, you will need to add a path
declaration to :literal:`urlpatterns` in your project :literal:`urls.py` like so:

.. code-block:: python

   from django_chime.views import ChimeSiteView

   ...

   urlpatterns = [

       ...

       # django-chime deployed models view (authentication optional)
       path(
           '<uuid:pk>/',
           ChimeSiteView.as_view(),
           name='site',
       ),

       # django-chime model management view (requires authentication)
       path(
           'chime/',
           include("django_chime.urls"),
       ),

       ...

Once logged in, users can navigate to :literal:`/chime/` to create and configure their
CHIME models.  Once created, the CHIME models are visible without authentication
at :literal:`/<ID of CHIME model>/`.

To use the templates that come with django-chime, you will need to add the following
blocks to your project base template :literal:`base.html`:

.. code-block:: jinja

   ...

   {% block external_css %}
   {% endblock external_css %}

   ...

   {% block headline %}
   {% endblock headline %}

   ...

   {% block section_content %}
   {% endblock section_content %}

   ...

   {% block external_javascript %}
   {% endblock external_javascript %}

   {% block project_javascript %}
   {% endblock project_javascript %}

.. note::

   You will need to add the css blocks to the :literal:`<head>` section and the
   javascript blocks to the *bottom* of the :literal:`<body>` section of your
   base template.

As an alternative, try using the base template from
`djcorecap <https://github.com/ChrisPappalardo/djcorecap>`_, as the base for
your project, it's awesome!


Credits
-------

The CHIME model and source code is Copyright © 2020, The Trustees of the University of Pennsylvania and was released for public use under the MIT License.  Please visit their `live application <https://penn-chime.phl.io/>`_ for more information.

The official UPenn CHIME project code base is being actively developed by `Code for Philly <https://github.com/CodeForPhilly>`_.  Please visit their `project on GitHub <https://github.com/CodeForPhilly/chime>`_ for more information.
