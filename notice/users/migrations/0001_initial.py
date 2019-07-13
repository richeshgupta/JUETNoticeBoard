# Generated by Django 2.0.7 on 2019-07-13 10:25

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
            name='NoticeBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('notice', models.TextField(default='', max_length=1000, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('url', models.URLField(blank=True, max_length=100)),
                ('docs', models.FileField(blank=True, upload_to='docs')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
