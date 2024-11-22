# Generated by Django 4.1.2 on 2024-08-09 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, unique=True)),
                ('joined_date', models.DateField(null=True)),
                ('slug', models.SlugField(default='')),
                ('bio', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
