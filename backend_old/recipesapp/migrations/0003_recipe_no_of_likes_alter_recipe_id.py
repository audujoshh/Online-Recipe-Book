# Generated by Django 5.1.6 on 2025-02-16 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0002_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='no_of_likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
