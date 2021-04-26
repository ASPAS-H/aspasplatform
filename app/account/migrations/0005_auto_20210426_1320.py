# Generated by Django 3.2 on 2021-04-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'DEAF'), (1, 'INTERPRETER'), (2, 'HOSPITAL_STAFF')], default=0),
        ),
    ]