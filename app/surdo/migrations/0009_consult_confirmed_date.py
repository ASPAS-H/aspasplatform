# Generated by Django 3.2 on 2021-06-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surdo', '0008_consult_interpreter'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='confirmed_date',
            field=models.DateField(null=True),
        ),
    ]
