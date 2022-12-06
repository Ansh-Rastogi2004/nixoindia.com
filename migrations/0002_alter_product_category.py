# Generated by Django 4.0.6 on 2022-11-02 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LO', 'Lotus'), ('RU', 'Rubino'), ('CR', 'Crystal'), ('CRG', 'Conti Rose Gold'), ('SQ', 'Squaro'), ('CL', 'Classic'), ('RE', 'Recta'), ('CU', 'Cubix'), ('AT', 'Atlanta'), ('HO', 'Hotelier'), ('RO', 'Rose'), ('MPS', 'Multipurpose Shelves'), ('CB', 'Conti Brass'), ('EC', 'Eco'), ('AL', 'Allied'), ('ESQ', 'Eco Squaro'), ('RUC', 'Rubino Chrome'), ('LOC', 'Lotus Chrome'), ('LUC', 'Luna Chrome'), ('PL', 'Pluto'), ('NE', 'Neptune')], max_length=3),
        ),
    ]