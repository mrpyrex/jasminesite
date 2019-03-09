from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    theme           = models.CharField(max_length=200)
    image           = models.ImageField(upload_to='cakes/')
    date            = models.DateField(default=timezone.now)
    description     = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.theme
