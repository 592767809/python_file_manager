
from django.db import models

# Create your models here.


class ApiKey(models.Model):

    key_value = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.key_value
