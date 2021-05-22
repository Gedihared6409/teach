# Generated by Django 3.1.6 on 2021-04-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crem', '0008_customer_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='repairAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AssetName', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('reason', models.TextField(max_length=200)),
                ('urgent', models.CharField(max_length=200)),
            ],
        ),
    ]