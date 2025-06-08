from django.db import models

class Users_details(models.Model):
    user_name = models.CharField(max_length = 100)
    