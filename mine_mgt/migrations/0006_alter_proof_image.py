# Generated by Django 4.0.5 on 2022-07-05 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mine_mgt', '0005_remove_payment_mine_payment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
