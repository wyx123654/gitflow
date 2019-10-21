from django.db import models
class Follow(models.Model):
     uid = models.IntegerField()
     date = models.DateTimeField()
     
