from django.db import models

# Create your models here.
class Brand(models.Model):
    Name = models.CharField(max_length=20)
    Orgin = models.CharField(max_length=50)

    def __str__(self):
        return self.Name