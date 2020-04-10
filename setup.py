#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
setup.py
--------

setup scripts for django-chime
'''

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'click>=6.0',
    'django>=2.2',
    'djcorecap',
    'penn_chime',
]

setup_requirements = [
]

test_requirements = [
]

setup(
    author="Chris Pappalardo",
    author_email='cpappala@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description='COVID-19 Hospital Impact Model for Epidemics (CHIME) app for Django.',
    entry_points={
        'console_scripts': [
            'django_chime=django_chime.cli:entry_point',
            'penn_chime=penn_chime.cli:entry_point',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='django-chime',
    name='django-chime',
    packages=find_packages(),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ChrisPappalardo/django-chime',
    version='0.1.0',
    zip_safe=False,
)
