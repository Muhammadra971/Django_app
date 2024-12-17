# Generated by Django 5.1.3 on 2024-12-15 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie_list', '0006_censorinfo_moviedata_censor_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='moviedata',
            name='directer_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_movie', to='Movie_list.directer'),
        ),
    ]
