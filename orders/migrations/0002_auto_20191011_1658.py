# Generated by Django 2.2.6 on 2019-10-11 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderDetails',
            new_name='OrderDetail',
        ),
    ]
