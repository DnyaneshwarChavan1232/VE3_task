# Generated by Django 4.2.13 on 2024-06-09 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.IntegerField()),
                ('survived', models.IntegerField()),
                ('pclass', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.FloatField()),
                ('sibsp', models.IntegerField()),
                ('parch', models.IntegerField()),
                ('ticket', models.CharField(max_length=100)),
                ('fare', models.FloatField()),
                ('cabin', models.CharField(max_length=100)),
                ('embarked', models.CharField(max_length=100)),
            ],
        ),
    ]