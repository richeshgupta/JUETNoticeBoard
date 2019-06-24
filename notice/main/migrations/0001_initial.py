# Generated by Django 2.0.5 on 2019-06-24 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_a', models.TextField(default='', max_length=1500, unique=True, verbose_name='Describe Answer')),
                ('date_a', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/Time')),
                ('url_a', models.URLField(blank=True, max_length=100, verbose_name='URL reference')),
                ('upvotes', models.IntegerField(default=0)),
                ('tag1_a', models.CharField(max_length=15, verbose_name='Tag 1')),
                ('tag2_a', models.CharField(max_length=15, verbose_name='Tag 2')),
                ('author_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_q', models.CharField(max_length=100, unique=True, verbose_name='Title of Question')),
                ('notice_q', models.TextField(default='', max_length=1000, unique=True, verbose_name='Description of Question')),
                ('date_q', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/Time')),
                ('url_q', models.URLField(blank=True, max_length=100, verbose_name='URL reference')),
                ('tag1_q', models.CharField(max_length=15, verbose_name='Tag 1')),
                ('tag2_q', models.CharField(max_length=15, verbose_name='Tag 2')),
                ('author_q', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='report_ans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.answer')),
            ],
        ),
        migrations.CreateModel(
            name='report_ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question', verbose_name='Select Question'),
        ),
    ]
