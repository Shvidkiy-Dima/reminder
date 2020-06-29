from rest_framework.serializers import ModelSerializer, SerializerMethodField, PrimaryKeyRelatedField
from .models import Event


class EventSerializer(ModelSerializer):
    is_gone = SerializerMethodField()
    author = PrimaryKeyRelatedField(read_only=True)

    def get_is_gone(self, obj):
        return obj.is_gone()

    class Meta:
        model = Event
        fields = ('id', 'creation_date', 'date',
                 'title', 'body', 'author', 'is_gone')
