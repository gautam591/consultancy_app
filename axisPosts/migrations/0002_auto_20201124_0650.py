# Generated by Django 3.0.8 on 2020-11-23 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axisPosts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applypopularity', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-applypopularity'],
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]