#!/home/shainal/dev/python3/bulletJournal/venv/bin/python3
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bullet_journal.settings")
django.setup()

import click

from bj.models import Notes_Notes, Tasks, Tags
from helpers import TaskHelper, NoteHelper

@click.group(invoke_without_command=True)
def cli():
    pass

@click.command('task')
@click.option('--a', '--add', is_flag=True)
@click.option('--v', '--view', is_flag=True)
@click.option('--c', '--close', is_flag=True)
def tasks(a, v, c):
    if a:
        click.echo('Task Add') 
    if v:
        click.echo('Task View')
    if c:
        click.echo('Task Close')

@click.command('note')
@click.option('--a', '--add', is_flag=True)
@click.option('--v', '--view', is_flag=True)
def notes(a, v):
    if a:
        click.echo('Notes Add')
    if v:
        click.echo('Notes View')

cli.add_command(tasks)
cli.add_command(notes)

if __name__ == '__main__':
    cli()
