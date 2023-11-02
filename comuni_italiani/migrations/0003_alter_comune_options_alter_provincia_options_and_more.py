# Generated by Django 4.2.7 on 2023-11-02 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comuni_italiani', '0002_remove_comune_auto_code_provincia_auto_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comune',
            options={'ordering': ['denomination'], 'verbose_name': 'Comune', 'verbose_name_plural': 'Comuni'},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['denomination'], 'verbose_name': 'Provincia', 'verbose_name_plural': 'Province'},
        ),
        migrations.AlterModelOptions(
            name='regione',
            options={'ordering': ['denomination'], 'verbose_name': 'Regione', 'verbose_name_plural': 'Regioni'},
        ),
    ]
