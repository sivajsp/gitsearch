from django.db import models
class city_list(models.Model):
    name = models.CharField(max_length=50)
