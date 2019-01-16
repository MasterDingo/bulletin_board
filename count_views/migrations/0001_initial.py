# Generated by Django 2.1.5 on 2019-01-16 20:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seen_ids', models.TextField(blank=True, default='')),
            ],
        ),
    ]