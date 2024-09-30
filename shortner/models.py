from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
