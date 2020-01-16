from django.db import models

class Addresses(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField()