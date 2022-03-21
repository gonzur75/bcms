# Generated by Django 4.0.2 on 2022-02-20 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('ingredients', models.CharField(max_length=255)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Flock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('birds_count', models.IntegerField(verbose_name='birds')),
                ('breed', models.CharField(max_length=64)),
                ('notes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64)),
                ('av_temp', models.SmallIntegerField()),
                ('description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CoupeDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('collected_eggs', models.IntegerField()),
                ('notes', models.CharField(max_length=255)),
                ('feed_amount_kg', models.DecimalField(decimal_places=1, max_digits=4)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.feed')),
                ('flock', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.flock')),
                ('weather', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.weather')),
            ],
        ),
    ]
