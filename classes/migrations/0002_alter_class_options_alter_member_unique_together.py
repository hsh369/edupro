# Generated by Django 4.1.1 on 2022-10-21 19:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterUniqueTogether(
            name='member',
            unique_together={('class_id', 'user_id')},
        ),
    ]
