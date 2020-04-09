# -*- coding: utf-8 -*-

'''
cli
---

console script for django_chime.
'''


import click
import sys


@click.command()
def main(args=None):
    '''
    django_chime command line interface
    '''

    click.echo("update django_chime.cli.main")
    return 0


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main())  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
