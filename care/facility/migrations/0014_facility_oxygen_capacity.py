# Generated by Django 2.2.11 on 2020-03-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0013_auto_20200322_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='oxygen_capacity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]