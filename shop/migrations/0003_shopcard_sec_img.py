# Generated by Django 3.1.3 on 2021-02-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210210_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcard',
            name='sec_img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]