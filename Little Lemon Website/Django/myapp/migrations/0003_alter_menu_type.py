# Generated by Django 4.2.8 on 2023-12-23 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='myapp.menucategory'),
        ),
    ]
