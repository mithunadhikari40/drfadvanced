# Generated by Django 3.2.9 on 2021-11-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0003_alter_deck_last_reviewed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='last_reviewed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
