from django.db import models
from django.conf import settings

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Bulletin(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=1024)
    city = models.ForeignKey(
        City,
        related_name='bulletins',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name='bulletins',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} by {} in {}".format(self.title, self.author.username, self.city.name)
