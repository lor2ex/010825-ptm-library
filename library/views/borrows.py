from rest_framework.viewsets import ModelViewSet

from library.models import Borrow
from library.serializers import (
    BorrowListSerializer,
    BorrowRetrieveSerializer,
    BorrowCreateUpdateSerializer,
)


class BorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BorrowListSerializer
        elif self.action in {'create', 'update', 'partial_update'}:
            return BorrowCreateUpdateSerializer
        return BorrowRetrieveSerializer
