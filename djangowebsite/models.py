from django.db import models


# Create your models here.
class UserWebsite(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.first_name + " " + self.last_name
