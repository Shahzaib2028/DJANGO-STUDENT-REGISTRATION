# Generated by Django 2.2.2 on 2021-02-07 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='roll_no',
        ),
    ]
