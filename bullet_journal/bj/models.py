from django.db import models

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
