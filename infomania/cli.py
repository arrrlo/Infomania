

import click

from .mania import Mania
from .klinfo import Klinfo
from .dollarkuna import DollarKuna
from .tehnicki_muzej import TehnickiMuzej


@click.group()
@click.option('-m', '--email', is_flag=True, default=False)
@click.pass_context
def cli(mania, email):
    mania.obj = Mania(email=email)


@cli.command()
@click.pass_context
def all(mania):
    mania.obj.set_source(Klinfo())
    mania.obj.set_source(TehnickiMuzej())
    mania.obj.set_source(DollarKuna())
    sources = mania.obj.run()

    print('')
    for source in sources:
        print(source.name)
        print('------------------')
        print('\n\n'.join(source.events))
        print('')
        print('')


@cli.command()
@click.pass_context
def klinfo(mania):
    mania.obj.set_source(Klinfo())
    sources = mania.obj.run()

    print('')
    for source in sources:
        print('\n\n'.join(source.events))
        print('')


@cli.command()
@click.pass_context
def tehnickimuzej(mania):
    mania.obj.set_source(TehnickiMuzej())
    sources = mania.obj.run()

    print('')
    for source in sources:
        print('\n\n'.join(source.events))
        print('')


@cli.command()
@click.pass_context
def dollarkuna(mania):
    mania.obj.set_source(DollarKuna())
    sources = mania.obj.run()

    print('')
    for source in sources:
        print('\n\n'.join(source.events))
        print('')