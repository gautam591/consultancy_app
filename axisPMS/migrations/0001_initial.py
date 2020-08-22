# Generated by Django 3.0.8 on 2020-08-22 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='pmsPostReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.BigIntegerField()),
                ('reaction', models.IntegerField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pmsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectTitle', models.CharField(max_length=200)),
                ('projectSlug', models.SlugField(max_length=200, unique=True)),
                ('projectBudget', models.IntegerField(default=0)),
                ('projectDeadline', models.DateTimeField(auto_now=True)),
                ('projectArea', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('category', models.IntegerField(default=0)),
                ('axisStatus', models.IntegerField(default=0)),
                ('popularity', models.BigIntegerField(default=0)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('projectAuthor', models.ForeignKey(default='AnynomousAxisUser', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['popularity'],
            },
        ),
        migrations.CreateModel(
            name='pmsComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.BigIntegerField()),
                ('parentId', models.IntegerField()),
                ('comment', models.TextField()),
                ('popularity', models.IntegerField(default=0)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('commentAuthor', models.ForeignKey(default='AnynomousAxisUser', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pmsCommentReactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentId', models.IntegerField()),
                ('reaction', models.IntegerField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
