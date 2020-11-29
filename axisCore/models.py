from django.db import models
from autoslug import AutoSlugField
from django.utils import timezone

# Create your models here.
class seminar (models.Model):
    university = models.CharField(max_length=10,default="NULL")
    date = models.DateTimeField()
    description = models.CharField(max_length=2000,default='NULL')
    link = models.CharField(max_length=200,default="NULL")
    seminarpopularity = models.IntegerField(default=0)
 

    class Meta:
        ordering = ['seminarpopularity']
    def __str__(self):
        return self.university