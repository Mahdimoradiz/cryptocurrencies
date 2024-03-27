from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name