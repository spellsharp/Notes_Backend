# Generated by Django 3.2.12 on 2024-02-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_auto_20240215_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
