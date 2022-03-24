# Generated by Django 3.2.12 on 2022-03-24 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20220324_1702'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating', '0020_auto_20220324_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='item',
            field=models.ForeignKey(default=None, help_text='Пожалуйста, укажите товар', on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
