# Generated by Django 3.2 on 2021-04-25 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='born_date',
            field=models.DateField(auto_now_add=True, verbose_name='born_date'),
        ),
    ]