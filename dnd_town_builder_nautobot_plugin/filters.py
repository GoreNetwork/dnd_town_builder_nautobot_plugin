from nautobot.utilities.filters import BaseFilterSet
import django_filters
from django.utils import timezone
from .models import  Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName

class BackgroundsFilterSet(django_filters.FilterSet):
    class Meta:
        model = Backgrounds
        fields = ("background", "type",)

class ServiceLocationFilterSet(django_filters.FilterSet):
    class Meta:
        model = ServiceLocation
        fields = ("service_type", "service", "service_price_low", "service_price_high",)

class ServiceNamesFilterSet(django_filters.FilterSet):
    class Meta:
        model = ServiceNames
        fields = ("name_part", "Name", "service_type",)

class CharNameFilterSet(django_filters.FilterSet):
    class Meta:
        model = CharName
        fields = ("race", "name_part", "name", "sex",)

class StoreNameFilterSet(django_filters.FilterSet):
    class Meta:
        model = StoreName
        fields = ("store_type", "name_part", "name",)

class StoreItemsFilterSet(django_filters.FilterSet):
    class Meta:
        model = StoreItems
        fields = ("store_type", "item_name", "item_price", "item_rarity",)

class TownNameFilterSet(django_filters.FilterSet):
    class Meta:
        model = TownName
        fields = ("name_part", "name",)
