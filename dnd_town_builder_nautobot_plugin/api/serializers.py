from nautobot.core.api.serializers import ValidatedModelSerializer
from rest_framework.serializers import StringRelatedField
from dnd_town_builder_nautobot_plugin.models import Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName 

class BackgroundsSerializer(ValidatedModelSerializer):
        class Meta:
            model = Backgrounds
            fields = ("pk", "background", "type")

class ServiceLocationSerializer(ValidatedModelSerializer):
        class Meta:
            model = ServiceLocation
            fields = ("pk", "service_type", "service", "service_price_low", "service_price_high")

class ServiceNamesSerializer(ValidatedModelSerializer):
        class Meta:
            model = ServiceNames
            fields = ("pk", "name_part", "Name", "service_type")

class CharNameSerializer(ValidatedModelSerializer):
        class Meta:
            model = CharName
            fields = ("pk", "race", "name_part", "name", "sex")

class StoreNameSerializer(ValidatedModelSerializer):
        class Meta:
            model = StoreName
            fields = ("pk", "store_type", "name_part", "name")

class StoreItemsSerializer(ValidatedModelSerializer):
        class Meta:
            model = StoreItems
            fields = ("pk", "store_type", "item_name", "item_price", "item_rarity")

class TownNameSerializer(ValidatedModelSerializer):
        class Meta:
            model = TownName
            fields = ("pk", "name_part", "name")
