# Generated by Django 3.0.2 on 2020-02-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num1', models.IntegerField(default=0)),
                ('num2', models.IntegerField(default=0)),
                ('operate', models.TextField(blank=True)),
                ('result', models.IntegerField(default=0)),
            ],
        ),
    ]
