# Generated by Django 3.2.3 on 2021-06-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_brand_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='tag',
            field=models.SlugField(default='', max_length=20, unique=True),
        ),
    ]
