from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=255)
    mobilenumber = models.CharField(max_length=15)  # Depending on the max length needed for the phone number
    preferred_time = models.CharField(max_length=50)  # Use TimeField if you want to store a specific time of day
    procedure = models.TextField()  # If this is some detailed procedure text, use TextField

    def __str__(self):
        return self.fullname
