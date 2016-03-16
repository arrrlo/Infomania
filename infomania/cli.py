

import click

from .mania import Mania
from .klinfo import Klinfo
from .dollarkuna import DollarKuna
from .tehnicki_muzej import TehnickiMuzej


@click.group(help='Infomania is a cute little script for fetching data from various websites.')
@click.option('-f', '--from_', type=click.STRING, help='Send info to e-mail address')
@click.option('-t', '--to', type=click.STRING, help='Send info from e-mail address')
@click.option('-h', '--host', type=click.STRING, help='E-mail server host')
@click.option('-u', '--username', type=click.STRING, help='E-mail server username')
@click.option('-p', '--password', type=click.STRING, help='E-mail server password')
@click.pass_context
def cli(mania, from_, to, host, username, password):
    if to: to = to.split(',')
    mania.obj = Mania(from_=from_, to=to, host=host, username=username, password=password)


@cli.command(help='Fetch data from all websites.')
@click.pass_context
def all(mania):
    mania.obj.set_source(Klinfo())
    mania.obj.set_source(TehnickiMuzej())
    mania.obj.set_source(DollarKuna())
    sources = mania.obj.run()

    click.echo('')
    for source in sources:
        click.echo(source.name)
        click.echo('------------------')
        click.echo('\n\n'.join(source.events))
        click.echo('')
        click.echo('')


@cli.command(help='Fetch events from www.klinfo.hr website for kids.')
@click.pass_context
def klinfo(mania):
    mania.obj.set_source(Klinfo())
    sources = mania.obj.run()

    click.echo('')
    for source in sources:
        click.echo('\n\n'.join(source.events))
        click.echo('')


@cli.command(help='Fetch events from www.tehnicki-muzej.hr website.')
@click.pass_context
def tehnickimuzej(mania):
    mania.obj.set_source(TehnickiMuzej())
    sources = mania.obj.run()

    click.echo('')
    for source in sources:
        click.echo('\n\n'.join(source.events))
        click.echo('')


@cli.command(help='Fetch dollar and kuna curent from www.pbz.hr')
@click.pass_context
def dollarkuna(mania):
    mania.obj.set_source(DollarKuna())
    sources = mania.obj.run()

    click.echo('')
    for source in sources:
        click.echo('\n\n'.join(source.events))
        click.echo('')
