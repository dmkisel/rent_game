# Generated by Django 5.0.6 on 2024-06-23 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('price', models.IntegerField()),
                ('age_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.agegame')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.statusgame')),
            ],
        ),
        migrations.CreateModel(
            name='RentGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('cost', models.IntegerField()),
                ('game', models.ManyToManyField(to='games.game')),
            ],
        ),
    ]
