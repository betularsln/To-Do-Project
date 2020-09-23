from django.db import models
from datetime import datetime


class  Todo(models.Model):
    islem_baslik = models.CharField(max_length=255)
    islem_aciklama = models.SlugField(max_length=255)
    created_on = models.DateTimeField(default=datetime.now ,blank=True )
    finished_on = models.DateTimeField(default=datetime.now ,blank=True )
    finished = models.BooleanField(default=False)


    def __str__(self):
        return self.islem_baslik