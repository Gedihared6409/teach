# Generated by Django 3.1.6 on 2021-03-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crem', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='crem.Tag'),
        ),
    ]
