from django.contrib import admin
from django.urls import include, path
from .views import to_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', to_books),
    path('', include('books.urls')),
]
