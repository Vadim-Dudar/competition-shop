# Generated by Django 3.1.3 on 2021-02-10 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shopcard_sec_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcard',
            name='sec_img',
        ),
    ]