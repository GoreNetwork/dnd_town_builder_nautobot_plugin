from django.contrib import admin
from dnd_town_builder_nautobot_plugin.models import Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName  
@admin.register(Backgrounds)
class BackgroundsAdmin(admin.ModelAdmin):
    list_display = ( "background", "type",)
     
@admin.register(ServiceLocation)
class ServiceLocationAdmin(admin.ModelAdmin):
    list_display = ( "service_type", "service", "service_price_low", "service_price_high",)
     
@admin.register(ServiceNames)
class ServiceNamesAdmin(admin.ModelAdmin):
    list_display = ( "name_part", "Name", "service_type",)
     
@admin.register(CharName)
class CharNameAdmin(admin.ModelAdmin):
    list_display = ( "race", "name_part", "name", "sex",)
     
@admin.register(StoreName)
class StoreNameAdmin(admin.ModelAdmin):
    list_display = ( "store_type", "name_part", "name",)
     
@admin.register(StoreItems)
class StoreItemsAdmin(admin.ModelAdmin):
    list_display = ( "store_type", "item_name", "item_price", "item_rarity",)
     
@admin.register(TownName)
class TownNameAdmin(admin.ModelAdmin):
    list_display = ( "name_part", "name",)
    