from django.db import models
from utils.models import TimeStampedModel
from jsonfield import JSONField
from django.conf import settings

class EquifaxAPI(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    pan_number = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    response_data = JSONField(null=True)

