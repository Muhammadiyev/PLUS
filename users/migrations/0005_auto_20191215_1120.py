# Generated by Django 2.2.7 on 2019-12-15 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Contact phone number', max_length=30),
        ),
    ]
