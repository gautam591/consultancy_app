from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class seminar (models.Model):
    university:models.CharField()
    date :models.DateTimeField()
    description :models.CharField()
    link = models.CharField(max_length=200)
    seminarpopularity = models.IntegerField(default=0)
    recipt:models.ImageField(upload_to="images/",null=False, blank=False)

    class Meta:
        ordering = ['seminarpopularity']
    def __str__(self):
        return self.seminarpopularity