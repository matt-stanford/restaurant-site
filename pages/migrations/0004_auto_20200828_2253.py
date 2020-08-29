# Generated by Django 3.1 on 2020-08-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200828_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='mjfstanford@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='Matt', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='Stanford', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='phone',
            field=models.CharField(default='07985349292', max_length=20),
            preserve_default=False,
        ),
    ]