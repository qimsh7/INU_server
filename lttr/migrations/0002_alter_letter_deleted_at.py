# Generated by Django 4.1.7 on 2023-03-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lttr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]