# Generated by Django 3.0.8 on 2020-08-30 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('axisPosts', '0003_auto_20200831_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='postimage',
        ),
    ]