from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    percentage = models.IntegerField()
    count_pool = models.IntegerField()
    count_aquapark = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)