# Generated by Django 4.2.7 on 2023-11-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0005_alter_order_address_alter_order_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='stationary',
            field=models.CharField(max_length=20),
        ),
    ]