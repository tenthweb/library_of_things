from django.db import models

# Create your models here.
class LibraryItem(models.Model):

    # Name is a character field with a limit
    name = models.CharField(max_length=100)
    # desctiption is a text field
    description = models.TextField()

    # available is either true or false, and true by default

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.namepython3 