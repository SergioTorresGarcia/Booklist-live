# Generated by Django 4.0.3 on 2022-04-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklist_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publishing_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='projectimg/'),
        ),
    ]
