from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class seminar (models.Model):
    university:models.CharField(max_length=10)
    date :models.DateTimeField()
    description :models.CharField(max_length=2000)
    link = models.CharField(max_length=200)
    seminarpopularity = models.IntegerField(default=0)
 

    class Meta:
        ordering = ['seminarpopularity']
    def __str__(self):
        return self.seminarpopularity