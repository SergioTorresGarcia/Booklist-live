# Generated by Django 4.0.3 on 2022-04-09 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist_app', '0002_remove_book_publishing_date_book_publishing_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, default='default/image/path/', null=True, upload_to='image/directory/'),
        ),
    ]
