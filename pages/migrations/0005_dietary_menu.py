# Generated by Django 3.1 on 2020-08-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200828_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dietary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dietary_tags', models.ManyToManyField(to='pages.Dietary')),
            ],
        ),
    ]