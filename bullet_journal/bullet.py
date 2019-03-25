#!/home/shainal/dev/python3/bulletJournal/venv/bin/python3
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bullet_journal.settings")
django.setup()

import click

from bj.models import Notes
from helpers import TaskHelper, NoteHelper

@click.command()
@click.option('--a', '--add', is_flag=True)
@click.option('--v', '--view', is_flag=True)
def main(a, v):
    if a:
        add_note()
    if v:
       view_notes() 
    
if __name__ == '__main__':
    main()
