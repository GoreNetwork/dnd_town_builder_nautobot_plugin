from nautobot.core.api.views import ModelViewSet
from dnd_town_builder_nautobot_plugin.models import Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName
from .serializers import BackgroundsSerializer, ServiceLocationSerializer, ServiceNamesSerializer, CharNameSerializer, StoreNameSerializer, StoreItemsSerializer, TownNameSerializer
from dnd_town_builder_nautobot_plugin.filters import BackgroundsFilterSet, ServiceLocationFilterSet, ServiceNamesFilterSet, CharNameFilterSet, StoreNameFilterSet, StoreItemsFilterSet, TownNameFilterSet

class BackgroundsViewSet(ModelViewSet):
    queryset = Backgrounds.objects.all()
    filterset_class = BackgroundsFilterSet
    serializer_class = BackgroundsSerializer

class ServiceLocationViewSet(ModelViewSet):
    queryset = ServiceLocation.objects.all()
    filterset_class = ServiceLocationFilterSet
    serializer_class = ServiceLocationSerializer

class ServiceNamesViewSet(ModelViewSet):
    queryset = ServiceNames.objects.all()
    filterset_class = ServiceNamesFilterSet
    serializer_class = ServiceNamesSerializer

class CharNameViewSet(ModelViewSet):
    queryset = CharName.objects.all()
    filterset_class = CharNameFilterSet
    serializer_class = CharNameSerializer

class StoreNameViewSet(ModelViewSet):
    queryset = StoreName.objects.all()
    filterset_class = StoreNameFilterSet
    serializer_class = StoreNameSerializer

class StoreItemsViewSet(ModelViewSet):
    queryset = StoreItems.objects.all()
    filterset_class = StoreItemsFilterSet
    serializer_class = StoreItemsSerializer

class TownNameViewSet(ModelViewSet):
    queryset = TownName.objects.all()
    filterset_class = TownNameFilterSet
    serializer_class = TownNameSerializer
