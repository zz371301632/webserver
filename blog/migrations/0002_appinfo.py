# Generated by Django 3.1 on 2020-08-27 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInfo',
            fields=[
                ('ihao', models.TextField()),
                ('deviceName', models.TextField()),
                ('time', models.BigIntegerField()),
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('os', models.IntegerField()),
                ('appVersion', models.TextField()),
                ('plugin', models.TextField()),
            ],
        ),
    ]