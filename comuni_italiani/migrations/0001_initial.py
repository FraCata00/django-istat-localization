# Generated by Django 4.2.7 on 2023-11-02 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Regione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creato')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Aggiornato')),
                ('data', models.JSONField(default=dict)),
                ('code', models.CharField(help_text='Codice Regione', max_length=50, unique=True, verbose_name='Codice Regione')),
                ('denomination', models.CharField(help_text='Denominazione Regione', max_length=255, verbose_name='Denominazione Regione')),
                ('geographic_partition', models.CharField(help_text='Ripartizione geografica', max_length=255, verbose_name='Ripartizione geografica')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creato da')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Aggiornato da')),
            ],
            options={
                'verbose_name': 'Regione',
                'verbose_name_plural': 'Regioni',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creato')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Aggiornato')),
                ('data', models.JSONField(default=dict)),
                ('code', models.CharField(help_text='Codice Provincia (Storico)', max_length=50, unique=True, verbose_name='Codice Provincia (Storico)')),
                ('denomination', models.CharField(help_text='Denominazione Provincia', max_length=255, verbose_name='Denominazione Provincia')),
                ('geographic_partition', models.CharField(help_text='Ripartizione geografica', max_length=255, verbose_name='Ripartizione geografica')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creato da')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', to='comuni_italiani.regione', verbose_name='Regione')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Aggiornato da')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Province',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Comune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Creato')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Aggiornato')),
                ('data', models.JSONField(default=dict)),
                ('code', models.CharField(help_text='Codice Comune formato alfanumerico', max_length=50, unique=True, verbose_name='Codice Comune formato alfanumerico')),
                ('progressive', models.IntegerField(help_text='Progressivo del Comune', verbose_name='Progressivo del Comune')),
                ('denomination', models.CharField(help_text='Denominazione Comune', max_length=255, verbose_name='Denominazione Comune')),
                ('auto_code', models.CharField(help_text='Sigla automobilistica', max_length=2, verbose_name='Sigla automobilistica')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Creato da')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='comuni_italiani.provincia', verbose_name='Provincia')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Aggiornato da')),
            ],
            options={
                'verbose_name': 'Comune',
                'verbose_name_plural': 'Comuni',
                'ordering': ['code'],
            },
        ),
    ]
