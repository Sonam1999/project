# Generated by Django 3.0.5 on 2020-04-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rb', '0017_auto_20200425_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='mobile',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
