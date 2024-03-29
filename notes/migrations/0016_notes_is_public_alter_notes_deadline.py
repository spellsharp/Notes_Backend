# Generated by Django 4.2 on 2024-02-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0015_alter_notes_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
