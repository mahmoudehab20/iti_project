# Generated by Django 4.2.5 on 2023-10-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
