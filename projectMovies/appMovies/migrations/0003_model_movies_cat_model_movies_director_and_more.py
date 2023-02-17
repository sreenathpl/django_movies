# Generated by Django 4.1.4 on 2023-01-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMovies', '0002_model_movies_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_movies',
            name='cat',
            field=models.CharField(default='dummy', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_movies',
            name='director',
            field=models.CharField(default='dummy', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='model_movies',
            name='duration',
            field=models.CharField(default='dummy', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='model_movies',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
