#!/home/shainal/dev/python3/bulletJournal/venv/bin/python3
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bullet_journal.settings")
import django
django.setup()

import click

from bj.models import Notes

def add_note():
    title = input('Title: ')
    text = input('Body: ')
    expiry_date = input('Due Date: ')
    note_type = input('Note Type (N, E, T): ')
    url_field = input('URL: ')

def view_notes():
    title_list = Notes.objects.all().values('note_title')
    for title in title_list:
        note_title = title['note_title']
        print(note_title)

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
