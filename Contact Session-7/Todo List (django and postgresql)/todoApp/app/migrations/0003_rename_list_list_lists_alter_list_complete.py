# Generated by Django 4.0.3 on 2022-04-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_item_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='list',
            new_name='lists',
        ),
        migrations.AlterField(
            model_name='list',
            name='complete',
            field=models.BooleanField(),
        ),
    ]