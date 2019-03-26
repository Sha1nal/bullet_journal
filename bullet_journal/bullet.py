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
    TaskHelper.create_task(task_text)
    click.echo('Task Added')

@click.command('tv')
def view_tasks():
    task_list = TaskHelper.view_tasks()
    for task in task_list:
        oneline = '{}: {}'.format(task[0], task[1])
        click.echo(oneline)

@click.command('tc')
@click.argument('task_id', nargs=1, type=click.INT)
def close_tasks(task_id):
    TaskHelper.close_task(task_id)
    click.echo('Closed Task: ' + str(task_id))

@click.command('note')
@click.option('--a', '--add', is_flag=True)
@click.option('--v', '--view', is_flag=True)
def notes(a, v):
    if a:
        click.echo('Notes Add')
    if v:
        click.echo('Notes View')

cli.add_command(add_tasks)
cli.add_command(view_tasks)
cli.add_command(close_tasks)
cli.add_command(notes)

if __name__ == '__main__':
    cli()
