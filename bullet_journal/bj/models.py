from django.db import models

class Notes(models.Model):
    note_title = models.CharField(max_length=140)
    note_text = models.TextField()
    date_created = models.DateField(auto_now=True)
    expiry_date = models.DateField()
    url = models.URLField()
    note_type = models.CharField(max_length=1,choices = (
                                                    ('N', 'Note'),
                                                    ('E', 'Event'),
                                                    ('T', 'Task'),
                                                )
                                                )

    def __str__(self):
        return self.note_title


class Tasks(models.Model):
    task_text = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task_text


class Notes_Notes(models.Model):
    note_text = models.TextField()
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.note_text


class Tags(models.Model):
    tag_text = models.CharField(max_length=20)
    notes = models.ManyToManyField(Notes_Notes)

    def __str__(self):
        return self.tag_text
