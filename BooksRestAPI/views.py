from django import views
from django.shortcuts import redirect
from django.urls import reverse


def to_books(request):
    return redirect(reverse('books'))
