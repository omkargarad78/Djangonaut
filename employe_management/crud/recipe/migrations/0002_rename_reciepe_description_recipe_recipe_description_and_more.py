# Generated by Django 5.2 on 2025-04-16 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='reciepe_description',
            new_name='recipe_description',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='receipe_ingre',
            new_name='recipe_ingre',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='receipe_name',
            new_name='recipe_name',
        ),
    ]
