from django.contrib import admin
from .models import OrderObject, TimeSlotObject

# Register your models here.
admin.site.register(OrderObject)
admin.site.register(TimeSlotObject)