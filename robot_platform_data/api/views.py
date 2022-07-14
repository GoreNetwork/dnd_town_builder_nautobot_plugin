from nautobot.core.api.views import ModelViewSet
from robot_platform_data.models import RobotPlatformData_MetaData
from .serializers import RobotPlatformData_MetaDataSerializer

class RobotPlatformDataViewSet(ModelViewSet):
    queryset = RobotPlatformData_MetaData.objects.all()
    serializer_class = RobotPlatformData_MetaDataSerializer