# Generated by Django 4.1.3 on 2023-12-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True, help_text='Enter the description of the item', null=True),
        ),
    ]
