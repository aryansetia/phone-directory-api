# Generated by Django 4.0.5 on 2022-06-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_contact_email_alter_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
