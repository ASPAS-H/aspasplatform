# Generated by Django 3.2 on 2021-05-29 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
