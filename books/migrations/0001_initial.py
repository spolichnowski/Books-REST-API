# Generated by Django 3.2.6 on 2021-09-01 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('published_date', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('average_rating', models.IntegerField(blank=True, null=True)),
                ('ratings_count', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('authors', models.ManyToManyField(blank=True, to='books.Author')),
                ('categories', models.ManyToManyField(blank=True, to='books.Category')),
            ],
        ),
    ]