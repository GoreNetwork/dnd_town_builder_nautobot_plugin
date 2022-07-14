from nautobot.core.api.routers import OrderedDefaultRouter
from dnd_town_builder_nautobot_plugin.api import views

router = OrderedDefaultRouter()
router.register("Backgrounds", views.BackgroundsViewSet)
router.register("ServiceLocation", views.ServiceLocationViewSet)
router.register("ServiceNames", views.ServiceNamesViewSet)
router.register("CharName", views.CharNameViewSet)
router.register("StoreName", views.StoreNameViewSet)
router.register("StoreItems", views.StoreItemsViewSet)
router.register("TownName", views.TownNameViewSet)
urlpatterns = router.urls