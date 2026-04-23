from rest_framework.viewsets import ModelViewSet

from library.models import Library
from library.serializers import LibraryListSerializer, LibraryRetrieveSerializer


class LibraryViewSet(ModelViewSet):
    queryset = Library.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return LibraryListSerializer
        return LibraryRetrieveSerializer
