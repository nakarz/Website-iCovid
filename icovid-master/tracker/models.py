from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TrackerFilter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    chart_type = models.IntegerField(default=1)
    number_of_data = models.IntegerField(default=7)