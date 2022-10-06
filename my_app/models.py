from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_message = models.TextField(null=True, blank=True)
    second_message = models.TextField(null=True, blank=True)
    third_message = models.TextField(null=True, blank=True)
    fourth_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}"