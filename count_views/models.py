from django.db import models

import uuid

# Create your models here.


class CountableModelMixin(models.Model):
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class Visitor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seen_ids = models.TextField(blank=True, default='[]')
