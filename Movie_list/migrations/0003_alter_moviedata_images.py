# Generated by Django 5.1.3 on 2024-12-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_list', '0002_alter_moviedata_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='images',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]