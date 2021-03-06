# Generated by Django 3.2.6 on 2021-08-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortenedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='original url', max_length=512)),
                ('short_path', models.CharField(db_index=True, max_length=15, unique=True, verbose_name='short url')),
                ('domain', models.CharField(max_length=50, verbose_name='domain from url')),
            ],
            options={
                'verbose_name': 'Shortened Url',
                'verbose_name_plural': 'Shortened Urls',
            },
        ),
    ]
