# Generated by Django 3.0.5 on 2020-04-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='todolist'),
        ),
    ]
