from django.conf import settings
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='agent', on_delete=models.CASCADE,
        primary_key=True)
    name = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55)
    is_company = models.BooleanField(default=False)
    is_independent = models.BooleanField(default=False)
    about = models.TextField()
    phonenumber = PhoneNumberField(blank=True)
    line_id = models.CharField(max_length=25, unique=True, blank=True)
    #logo = models.ImageField(upload_to=, default='agents/logos/default.png')
    #document = models.FileField(upload_to=,)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


