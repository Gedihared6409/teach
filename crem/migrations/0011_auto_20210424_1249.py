# Generated by Django 3.1.6 on 2021-04-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crem', '0010_customer_catego'),
    ]

    operations = [
        migrations.DeleteModel(
            name='repairAsset',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='catego',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
