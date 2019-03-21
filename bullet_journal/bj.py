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
    expiry_date = input('Due Date (YYYY-MM-DD): ')
    note_type = input('Note Type (N, E, T): ')
    url_field = input('URL: ')
    
    new_note = Notes(note_title=title, note_text=text, expiry_date=expiry_date, url=url_field, note_type=note_type)
    new_note.save()
    click.echo('Note saved successfully')

def view_notes():
    queryset = Notes.objects.all()
    for note in queryset:
        note_title = note.note_title
        note_id = note.id

        print(str(note_id) + ": " + note_title)

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
