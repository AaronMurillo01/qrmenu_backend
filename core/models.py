from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    number_of_table = models.IntegerField(default=1)
    
    def __str__(self):
        return "{}/{}".format(self.owner.username, self.name)


