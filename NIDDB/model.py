from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MaxValueValidator


class Applicant_Data(models.Model):
    nid = models.PositiveIntegerField(unique=True,validators=[MaxValueValidator(99999999999999999)])
    status = models.CharField(max_length=255,blank=True,default="Undecided",
            choices=[
                ("Approved","Approved"),
                ("Canceled","Canceled"),
            ])
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.nid} added by {self.added_by.username} at {self.date.strftime('%d-%m-%Y')}."