# Generated by Django 4.2.7 on 2023-11-24 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
