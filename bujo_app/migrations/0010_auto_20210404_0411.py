# Generated by Django 3.1.7 on 2021-04-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bujo_app', '0009_auto_20210404_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledetails',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
