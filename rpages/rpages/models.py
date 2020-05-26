from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    days1 = models.PositiveSmallIntegerField()
    days2 = models.PositiveSmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
