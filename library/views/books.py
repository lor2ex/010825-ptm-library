from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers import BookSerializer



class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        all_books = Book.objects.all()

        year_from = self.request.query_params.get("year_from")
        category_name = self.request.query_params.get("category_name")

        if year_from:
            all_books = all_books.filter(published_date__year__gte=year_from)

        if category_name:
            all_books = all_books.filter(category__name__iexact=category_name)

        return all_books