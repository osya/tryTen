from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, help_text='100 characters max')
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.name
