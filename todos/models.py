from django.db import models

class Todo(models.Model):
    title_text = models.CharField(max_length=100)
    detail = models.CharField(max_length=300)

    def __str__(self):
        return self.title_text
