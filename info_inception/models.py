from django.db import models


# Create your models here.

class Bild(models.Model):
    user_title = models.CharField(max_length=50,null=True)
    incept_title = models.CharField(max_length=50,null=True)
    file = models.ImageField()
    pub_date = models.DateTimeField('hochgeladen am',null=True)