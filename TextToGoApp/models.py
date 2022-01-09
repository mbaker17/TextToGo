from django.db import models

# Create your models here.
class OrderObject(models.Model):
    FirstName = models.CharField(max_length=256, blank=True)
    LastName = models.CharField(max_length=256, blank=True)
    Email = models.EmailField(max_length=256, blank=True)
    ConfirmNum = models.CharField(max_length=8, blank=False)
    # PickUp = models.PickUpObject()

class PickUpObject(models.Model):
    BagPulled = models.BooleanField()
    BagPickedUp = models.BooleanField()
    MissedPickUp = models.BooleanField()
    InvalidConfirmNum = models.BooleanField()
    




