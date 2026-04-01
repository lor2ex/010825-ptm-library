from library.views import BookListAPIView
from django.urls import path


urlpatterns = [
    path('', BookListAPIView.as_view())
]

