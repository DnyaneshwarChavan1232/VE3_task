# Generated by Django 4.2.13 on 2024-06-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_uploadfile_rename_age_titanic_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titanic',
            name='id',
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Age',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Cabin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Embarked',
            field=models.CharField(blank=True, choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Fare',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='PassengerId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='titanic',
            name='Survived',
            field=models.BooleanField(),
        ),
    ]