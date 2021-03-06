# Generated by Django 3.2.8 on 2021-10-31 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0002_auto_20211031_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='preview_content',
            field=models.TextField(blank=True, null=True, verbose_name='プレビュー'),
        ),
        migrations.AlterField(
            model_name='study',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='study',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='stydy_tags', to='study.Tag'),
        ),
    ]
