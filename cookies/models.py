from django.db import models

# Create your models here.

class Cookie(models.Model):
    cookie_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.cookie_text
