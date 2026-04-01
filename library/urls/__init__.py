from django.urls import path, include


urlpatterns = [
    path('categories/', include('library.urls.categories')),
    path('books/', include('library.urls.books')),
]
