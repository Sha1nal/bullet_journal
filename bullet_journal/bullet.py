#!/home/shainal/dev/python3/bulletJournal/venv/bin/python3

import sys
sys.path.insert(0, '/home/shainal/dev/python3/bulletJournal/bullet_journal')

import click

from helpers import TaskHelper, NoteHelper

@click.group(invoke_without_command=True)
def cli():
    pass

@click.command('ta')
@click.argument('task_text', nargs=1, type=click.STRING, default='')
def add_tasks(task_text):
    """
    Takes one argument from the command line
    Adds it to the task list
    """
    TaskHelper.create_task(task_text)
    click.echo('Task Added')

@click.command('tv')
def view_tasks():
    """
    Populates list with open tasks
    """
    task_list = TaskHelper.view_tasks()
    click.echo('-----Task List-----')
    for task in task_list:
        oneline = '{}: {}'.format(task[0], task[1])
        click.echo(oneline)

@click.command('tc')
@click.argument('task_id', nargs=1, type=click.INT)
def close_tasks(task_id):
    """
    Takes in a task ID
    Closes task so that it is removed off list
    """
    TaskHelper.close_task(task_id)
    click.echo('Closed Task: ' + str(task_id))

@click.command('na')
@click.argument('arg_list', nargs=-1)
def add_notes(arg_list):
    """
    """
    note_text = ''
    tag_list = []
    new_note = NoteHelper()
    for arg in reversed(arg_list):
        if arg == arg_list[-1]:
            note_text = arg     #assign last argument as note text
        else:
            tag_list.append(arg)    #all other arguments become tags

    new_note.create_note(note_text, tag_list)

@click.command('nv')
@click.argument('tag_list', nargs=-1)
def View_notes(tag_list):
    note_list = NoteHelper.view_notes(tag_list) 
    for note in note_list:
        click.echo(note)

cli.add_command(add_tasks)
cli.add_command(view_tasks)
cli.add_command(close_tasks)
cli.add_command(add_notes)
cli.add_command(View_notes)

if __name__ == '__main__':
    cli()
