# Generated by Django 4.2.1 on 2023-06-08 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
