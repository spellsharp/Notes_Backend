# Generated by Django 3.2.12 on 2023-12-18 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20231218_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='tags',
        ),
        migrations.AddField(
            model_name='notes',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='notes.Tags'),
        ),
    ]
