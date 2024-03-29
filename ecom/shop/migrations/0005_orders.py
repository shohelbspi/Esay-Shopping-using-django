# Generated by Django 2.2.5 on 2019-10-03 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190917_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=4000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=80)),
                ('zip_code', models.CharField(max_length=80)),
            ],
        ),
    ]
