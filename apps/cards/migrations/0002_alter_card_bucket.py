# Generated by Django 3.2.9 on 2021-11-14 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='bucket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cards.buckets'),
        ),
    ]