# Generated by Django 5.1.6 on 2025-02-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_uploads/'),
        ),
    ]
