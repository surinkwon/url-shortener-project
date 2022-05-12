from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    original_url = models.URLField()
    url_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.url_name