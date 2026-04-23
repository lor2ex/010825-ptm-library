from rest_framework.viewsets import ModelViewSet
from library.models import Author
from library.serializers.authors import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
