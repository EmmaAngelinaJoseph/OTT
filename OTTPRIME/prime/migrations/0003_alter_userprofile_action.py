# Generated by Django 4.2.13 on 2024-05-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0002_customer_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='action',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
