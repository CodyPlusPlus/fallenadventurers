# Generated by Django 3.0.6 on 2020-05-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(max_length=50)),
                ('charclass', models.CharField(max_length=50)),
                ('liferange', models.CharField(max_length=50)),
                ('enscription', models.CharField(max_length=150)),
            ],
        ),
    ]
