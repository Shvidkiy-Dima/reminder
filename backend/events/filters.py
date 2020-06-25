from django_filters import CharFilter, IsoDateTimeFilter
from django_filters.rest_framework import FilterSet
from .models import Event


class EventFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    creation_date = IsoDateTimeFilter(field_name='creation_date', lookup_expr='gt')

    class Meta:
        model = Event
        fields = ['title', 'creation_date']
