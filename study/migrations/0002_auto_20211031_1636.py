# Generated by Django 3.2.8 on 2021-10-31 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.category'),
        ),
        migrations.AlterField(
            model_name='study',
            name='liked',
            field=models.ManyToManyField(blank=True, null=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='study',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='stydy_tags', to='study.Tag'),
        ),
    ]