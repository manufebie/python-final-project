from django.conf import settings
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

def user_directory_path(instance, file):
    # file will be saved to user seperated folders
    if instance.logo:
        return 'logos/agent_{}/{}'.format(instance.user.id, file)
    elif instance.document:
        return 'documents/agent_{}/{}'.format(instance.user.id, file)

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
    logo = models.ImageField(upload_to=user_directory_path, default='logos/default.jpeg')
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class VerificicationDocument(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    document = models.FileField(upload_to=user_directory_path)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


