# Generated by Django 5.1.4 on 2024-12-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderHomepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttile', models.CharField(max_length=100)),
                ('little_text', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='slider')),
            ],
            options={
                'verbose_name': 'слайдер',
                'verbose_name_plural': 'Слайдер',
            },
        ),
    ]
