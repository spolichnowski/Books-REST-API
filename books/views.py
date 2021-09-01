from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import generics
from .models import Author, Book, Category
from .serializers import BookSerializer, DetailBookSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import requests


def check_key(value, key, key2=None, *args):
    '''
    Function checks if given key exist and returns its value.
    If key doesn't exist func returns None. 
    '''
    try:
        if key2:
            return value[key][key2]
        else:
            return value[key]
    except:
        return None


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, )
    filterset_fields = ['published_date']
    ordering_fields = ['date', ]

    def get_queryset(self):
        '''
        Queryset for authors filtering
        '''
        queryset = Book.objects.all()
        if 'author' in self.request.query_params:
            authors = [
                a.replace('"', "") for a in self.request.query_params.getlist('author')
            ]
            queryset = queryset.filter(authors__name__in=authors)
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    '''
    Detail view
    '''
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'
    filter_backends = (DjangoFilterBackend, OrderingFilter, )


def postDataSet(request):
    '''
    Downloads dataset and saves it in the databes.
    If item already exists it will be updated.
    '''
    link = f'https://www.googleapis.com/books/v1/volumes?q=war'
    response = requests.get(link)
    res = response.json()
    for e in res['items']:
        defaults = {}
        book_id = e['id']
        info = e['volumeInfo']
        defaults['title'] = check_key(info, 'title')
        defaults['published_date'] = check_key(info, 'publishedDate')
        defaults['average_rating'] = check_key(info, 'averageRating')
        defaults['ratings_count'] = check_key(info, 'ratingsCount')
        defaults['thumbnail'] = check_key(info, 'imageLinks', 'thumbnail')
        new_book, _ = Book.objects.update_or_create(
            book_id=book_id,
            title=defaults['title'],
            published_date=defaults['published_date'],
            average_rating=defaults['average_rating'],
            ratings_count=defaults['ratings_count'],
            thumbnail=defaults['thumbnail'],
            defaults=defaults
        )
        new_book.save()

        try:
            for name in info['authors']:
                add_author, _ = Author.objects.get_or_create(name=name)
                new_book.authors.add(add_author)
        except:
            pass

        try:
            for category in info['categories']:
                add_category, _ = Category.objects.get_or_create(
                    category=category)
                new_book.categories.add(add_category)
        except:
            pass

        new_book.save()
    return redirect(reverse('books'))
