from django.contrib import admin
from django.urls import include, path
from .views import BookListView, BookDetailView, postDataSet

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<book_id>/', BookDetailView.as_view()),
    path('db/', postDataSet),
]
