from rest_framework import serializers

from library.models import Borrow


class BorrowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = [
            'id',
            'member',
            'book',
            'library',
            'end_plane_date',
        ]


class BorrowRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = "__all__"


class BorrowCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = "__all__"
