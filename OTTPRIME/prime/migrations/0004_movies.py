# Generated by Django 4.2.13 on 2024-05-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0003_alter_userprofile_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('genres', models.CharField(blank=True, max_length=100, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('main_actor', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='movie/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='movie/videos/')),
            ],
        ),
    ]
