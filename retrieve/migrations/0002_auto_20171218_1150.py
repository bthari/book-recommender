# Generated by Django 2.0 on 2017-12-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retrieve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]