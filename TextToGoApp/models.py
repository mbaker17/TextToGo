from django.db import models
import datetime 
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import ValidationError


# Create your models here.
class OrderObject(models.Model):
    FirstName = models.CharField(max_length=256, blank=True)
    LastName = models.CharField(max_length=256, blank=True)
    Email = models.EmailField(max_length=256, blank=True)
    ConfirmNum = models.CharField(max_length=8, blank=False)

    one = "09:10 – 09:20"
    two = "09:20 – 09:30"
    three = "09:30 – 09:40"
    four = "09:40 – 09:50"
    five = "09:50 – 10:00"

    TIMESLOT_LIST = (
        (one, '09:10 – 09:20'),
        (two, '09:20 – 09:30'),
        (three, '09:30 – 09:40'),
        (four, '09:40 – 09:50'),
        (five, '09:50 – 10:00'),
    )

    # datetime = models.DateTimeField()
    time = models.TextField(default="yeet")

    begintime = models.TimeField(default=datetime.time(00, 00), null=True)

    timeslot = models.TextField(choices=TIMESLOT_LIST, null=True, max_length=256)
    date = models.DateField(default=datetime.date.today, null=True)

    BagPulled = models.BooleanField(default=False)
    BagPickedUp = models.BooleanField(default=False)
    MissedPickUp = models.BooleanField(default=False)
    InvalidConfirmNum = models.BooleanField(default=False)

class TimeSlotObject(models.Model):
    Order = models.ForeignKey(OrderObject, on_delete = models.CASCADE, null=True)
    customers_per_slot = models.IntegerField(default=30)

class SingleInstanceMixin(object):
    """Makes sure that no more than one instance of a given model is created."""

    def clean(self):
        model = self.__class__
        if (model.objects.count() > 1 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 %s instance" % model.__name__)
        super(SingleInstanceMixin, self).clean()



