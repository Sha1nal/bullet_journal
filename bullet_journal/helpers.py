import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bullet_journal.settings")

django.setup()

from bj.models import Tasks, Notes_Notes, Tags, Tag_Notes

class TaskHelper():
    """
    This class will assist with all the functionality 
    of managing Tasks
    """

    def __init__(self):
        self.task = Tasks()

    def create_task(self, text):
        """
        This function will create a task. 
        As inputs it will recieve a text
        string. Its output will be a bool
        returning True if the save has been
        successful and a new entry in the 
        databse in the Tasks table.
        """
        self.task.task_text = text 
        self.task.save()
        return True

    def view_tasks(self):
        """
        This function will retrieve all incomplete
        tasks from the database and return it.
        """
        incomplete_task_list = Tasks.objects.filter(is_complete=False)
        return incomplete_task_list

    def close_task(self, task_id):
        """
        This fucntion takes a 'Task_ID' as an input 
        and changes that specific task to complete
        in the database
        """
        task = Tasks.objects.get(pk=task_id)
        task.is_complete = True
        task.save()
        return True


class NoteHelper():
    """
    This class will assist with all the functionality 
    associated with Notes
    """

    def __init__(self):
        self.note = Notes_Notes()
 
    def create_note(self, text, tags_list):
        """
        This function takes a string of text that will
        form the body of the note and a list of single
        words that will form the tags associated with the 
        note. The output will be a succesfully created 
        note entry and each tag entry associated with the
        note.
        """
        self.note.note_text = text
        self.note.save()

        for tag in tags_list:
            """
            get all tags in db
            for each tag check
                if tag_text == tag
                    get tag_text.id
                else
                    create new tag
                    save
                create new tag_notes(note_id, tag_id)
                save
            """

    def view_note(self, tag_list):
        """
        This funciton takes in a list of one or more
        words (tags). Its out output will be a list
        of all notes associated with the words (tags). 
        """