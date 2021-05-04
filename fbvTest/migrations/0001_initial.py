# Generated by Django 3.1.7 on 2021-04-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('email', models.EmailField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
