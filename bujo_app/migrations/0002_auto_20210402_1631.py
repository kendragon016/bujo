# Generated by Django 3.1.7 on 2021-04-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bujo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfileBio',
        ),
        migrations.DeleteModel(
            name='ProfileName',
        ),
    ]