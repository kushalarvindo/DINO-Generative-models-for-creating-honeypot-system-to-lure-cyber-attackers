from django.db import models

# Create your models here.
class HoneyPot(models.Model):
    #Source IP,Dest. Port,Protocol,Action,Payload,Outcome
    Source_IP=models.CharField(max_length=100)
    Dest_Port=models.CharField(max_length=100)
    Protocol=models.CharField(max_length=100)
    Action=models.CharField(max_length=100)
    Payload=models.CharField(max_length=100)
    Outcome=models.CharField(max_length=100)