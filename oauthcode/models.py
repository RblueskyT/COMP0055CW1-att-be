from django.db import models

# Create your models here.
class Ocode(models.Model):
    oauth_code = models.CharField(max_length=1000)

    def __str__(self):
        return self.oauth_code
