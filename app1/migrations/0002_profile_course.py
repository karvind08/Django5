# Generated by Django 4.2.19 on 2025-03-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course',
            field=models.CharField(default='B.Tech', max_length=50),
            preserve_default=False,
        ),
    ]
