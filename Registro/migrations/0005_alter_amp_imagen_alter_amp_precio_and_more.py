# Generated by Django 4.2 on 2024-09-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_amp_imagen_instrumento_imagen_pedal_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amp',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='amp/'),
        ),
        migrations.AlterField(
            model_name='amp',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='inst/'),
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pedal',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='pedal/'),
        ),
        migrations.AlterField(
            model_name='pedal',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='portapuas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='porta/'),
        ),
        migrations.AlterField(
            model_name='portapuas',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
