# Generated by Django 4.2.7 on 2024-06-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0007_alter_book_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(blank=True, null=True, upload_to="covers/"),
        ),
        migrations.AlterField(
            model_name="book",
            name="genres",
            field=models.ManyToManyField(null=True, to="books.genre"),
        ),
    ]