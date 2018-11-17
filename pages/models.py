from django.db import models


class AboutPage(models.Model):
    '''A simple model for a dynamic about page'''
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='pages', blank=True)

    def __str__(self):
        return self.title