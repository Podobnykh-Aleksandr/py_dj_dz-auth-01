from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    """ Фильтрация по дате  _after & _before"""
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'updated_at', 'creator', 'status']
