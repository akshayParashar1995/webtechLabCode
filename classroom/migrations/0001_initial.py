# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('answer_text', models.CharField(max_length=255)),
                ('isCorrect', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date_of_submission', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('course_name', models.CharField(max_length=30)),
                ('duration', models.IntegerField(max_length=4)),
                ('course_fee', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=10)),
                ('course_id', models.ForeignKey(to='classroom.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('question_text', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('dob', models.DateField()),
                ('phone_no', models.BigIntegerField(max_length=10)),
                ('st_course', models.ManyToManyField(to='classroom.Course')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('department', models.CharField(max_length=20)),
                ('phone_no', models.BigIntegerField(max_length=10)),
                ('teacher_course', models.ManyToManyField(to='classroom.Course')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('course_id', models.ForeignKey(to='classroom.Course')),
                ('teacher_id', models.ForeignKey(to='classroom.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='notes',
            name='teacher_id',
            field=models.ForeignKey(to='classroom.Teacher'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question_id',
            field=models.ForeignKey(to='classroom.Questions'),
        ),
    ]
