import public as public
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    class Meta:
        db_table = "book"
