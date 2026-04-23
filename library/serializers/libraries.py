from rest_framework import serializers

from library.models import Library


class LibraryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = [
            'id',
            'name',
        ]


class LibraryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = "__all__"
