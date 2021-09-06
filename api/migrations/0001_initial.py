# Generated by Django 3.1.7 on 2021-09-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
                ('average_rating', models.IntegerField()),
                ('rating_count', models.IntegerField()),
                ('thumbnail', models.CharField(max_length=200)),
            ],
        ),
    ]
