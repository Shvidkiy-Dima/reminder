from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Event
from .permissions import IsAuthor
from .serializers import EventSerializer
from .filters import EventFilter


class EventView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAuthor]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter


    def get_queryset(self):
        return self.request.user.my_events.all()
