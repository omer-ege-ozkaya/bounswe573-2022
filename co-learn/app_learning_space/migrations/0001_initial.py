# Generated by Django 4.0.4 on 2022-05-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('colearners', models.ManyToManyField(to='app_profile.profile')),
            ],
        ),
    ]
