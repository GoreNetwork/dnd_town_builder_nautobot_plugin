from nautobot.core.api.routers import OrderedDefaultRouter
from robot_platform_data.api import views

router = OrderedDefaultRouter()
router.register("", views.RobotPlatformDataViewSet)
urlpatterns = router.urls
