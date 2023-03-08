from django.db import models


class Stream(models.Model):
    """ Stream Model for each individual stream """

    name = models.CharField(max_length=200, unique=False, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Streams'
