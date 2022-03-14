# Generated by Django 2.2.16 on 2022-03-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20220314_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='имя')),
                ('slug', models.SlugField(unique=True, verbose_name='адрес')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Groups, it will be shown in admin panel',
            },
        ),
    ]
