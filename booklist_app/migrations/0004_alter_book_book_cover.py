# Generated by Django 4.0.3 on 2022-04-09 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist_app', '0003_alter_book_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
