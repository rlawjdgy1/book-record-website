# Generated by Django 3.1.6 on 2021-02-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='averageRating',
            field=models.FloatField(default=0),
        ),
    ]
