# Generated by Django 3.1.3 on 2021-02-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcard',
            name='img',
            field=models.ImageField(upload_to='shop/static/shop/img'),
        ),
    ]
