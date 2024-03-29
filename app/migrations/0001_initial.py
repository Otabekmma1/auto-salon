# Generated by Django 5.0.3 on 2024-03-28 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='brend')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brandlar',
            },
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Rangi')),
            ],
            options={
                'verbose_name': 'Rang',
                'verbose_name_plural': 'Ranglar',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='rusumi')),
                ('price', models.IntegerField(verbose_name='Narxi')),
                ('price_types', models.CharField(choices=[('$', '$')], max_length=10, verbose_name='Valyuta')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand', verbose_name='brend')),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.colour', verbose_name='rangi')),
            ],
            options={
                'verbose_name': 'Mashina',
                'verbose_name_plural': 'Mashinalar',
            },
        ),
    ]
