# Generated by Django 4.2 on 2024-09-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_alter_amp_descripcion_alter_instrumento_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='amp',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='instrumentos/'),
        ),
        migrations.AddField(
            model_name='instrumento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='instrumentos/'),
        ),
        migrations.AddField(
            model_name='pedal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='instrumentos/'),
        ),
        migrations.AddField(
            model_name='portapuas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='instrumentos/'),
        ),
    ]
