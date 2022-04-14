# Generated by Django 4.0.3 on 2022-04-13 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist_app', '0004_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='../media/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
