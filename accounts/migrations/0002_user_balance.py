# Generated by Django 4.0.5 on 2022-07-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.CharField(default=200, max_length=250),
            preserve_default=False,
        ),
    ]