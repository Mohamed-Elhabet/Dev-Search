# Generated by Django 3.2.13 on 2022-04-29 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created']},
        ),
    ]