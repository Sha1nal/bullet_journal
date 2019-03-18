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
