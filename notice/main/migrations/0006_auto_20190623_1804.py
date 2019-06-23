# Generated by Django 2.0.5 on 2019-06-23 12:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190623_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tag3_a',
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag3_q',
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_a',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='notice_a',
            field=models.TextField(default='', max_length=1500, unique=True, verbose_name='Describe Answer'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='ques',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question', verbose_name='Select Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='tag1_a',
            field=models.CharField(max_length=15, verbose_name='Tag 1'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='tag2_a',
            field=models.CharField(max_length=15, verbose_name='Tag 2'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='url_a',
            field=models.URLField(blank=True, max_length=100, verbose_name='URL reference'),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_q',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='question',
            name='notice_q',
            field=models.TextField(default='', max_length=1000, unique=True, verbose_name='Description of Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tag1_q',
            field=models.CharField(max_length=15, verbose_name='Tag 1'),
        ),
        migrations.AlterField(
            model_name='question',
            name='tag2_q',
            field=models.CharField(max_length=15, verbose_name='Tag 2'),
        ),
        migrations.AlterField(
            model_name='question',
            name='url_q',
            field=models.URLField(blank=True, max_length=100, verbose_name='URL reference'),
        ),
    ]