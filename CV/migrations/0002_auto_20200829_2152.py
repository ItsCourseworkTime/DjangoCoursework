# Generated by Django 2.2.12 on 2020-08-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvsection',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]