# Generated by Django 3.2.4 on 2021-07-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0008_alter_transection_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transection',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode/'),
        ),
    ]
