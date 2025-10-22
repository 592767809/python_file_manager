
from django.db import models

# Create your models here.


class ApiKey(models.Model):

    name = models.CharField(max_length=32)
    key_value = models.CharField(max_length=32)

    def __str__(self):
        return self.name + ':' + self.key_value
