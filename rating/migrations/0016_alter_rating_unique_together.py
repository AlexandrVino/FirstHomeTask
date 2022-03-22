# Generated by Django 3.2.12 on 2022-03-22 06:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0006_auto_20220321_1309'),
        ('rating', '0015_auto_20220322_1058'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('item', 'user')},
        ),
    ]
