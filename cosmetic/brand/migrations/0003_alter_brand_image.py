# Generated by Django 4.0.2 on 2022-02-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_brand_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/brand/%y/%m/%d'),
        ),
    ]
