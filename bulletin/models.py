from django.db import models
from django.conf import settings

from count_views.models import CountableModelMixin

# Create your models here.


class BulletinManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()

class City(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"


class Bulletin(CountableModelMixin, models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
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
        return "{} by {} in {}".format(
            self.title,
            self.author.username,
            self.city.name
        )
