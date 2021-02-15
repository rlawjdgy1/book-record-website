from django.db import models

# Create your models here.
class Book(models.Model):
    #fields for the book table
    name = models.CharField(max_length=300)
    writer = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    publish_date = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)

def __str__(self):
    return self.name

def __unicode__(self):
    return self.name
