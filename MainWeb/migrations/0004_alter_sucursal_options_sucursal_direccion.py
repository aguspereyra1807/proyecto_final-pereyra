# Generated by Django 4.2.3 on 2023-08-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWeb', '0003_sucursal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sucursal',
            options={'ordering': ['nombre'], 'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursales'},
        ),
        migrations.AddField(
            model_name='sucursal',
            name='direccion',
            field=models.CharField(default='', max_length=50),
        ),
    ]
