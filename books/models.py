from django.db import models
from datetime import date


class Author(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category


class Book(models.Model):
    book_id = models.CharField(max_length=12, primary_key=True)
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField("Author", blank=True)
    published_date = models.CharField(max_length=10)
    date = models.DateField(auto_now=False, auto_now_add=False)
    categories = models.ManyToManyField("Category", blank=True)
    average_rating = models.IntegerField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.published_date.count('-') == 2:
            d = list(map(int, self.published_date.split('-')))
            self.date = date(
                d[0],
                d[1],
                d[2]
            )
        elif self.published_date.count('-') == 1:
            d = list(map(int, self.published_date.split('-')))
            self.date = date(
                d[0],
                d[1],
                1
            )
        elif self.published_date.count('-') == 0:
            self.date = date(int(self.published_date), 1, 1)

        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
