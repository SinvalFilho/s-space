# Generated by Django 4.1.6 on 2023-02-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotografia',
            name='foto',
        ),
        migrations.AddField(
            model_name='fotografia',
            name='foto_space',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
        migrations.AddField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
