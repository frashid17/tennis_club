# Generated by Django 5.1.2 on 2024-10-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_rename_members_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
