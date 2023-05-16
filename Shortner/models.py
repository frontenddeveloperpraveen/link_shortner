from django.db import models

class URL(models.Model):
    sno = models.BigAutoField(primary_key=True)
    olink = models.CharField(max_length=500)
    short = models.CharField(max_length=200)
    