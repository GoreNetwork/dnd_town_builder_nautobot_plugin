from nautobot.core.api.serializers import ValidatedModelSerializer
from robot_platform_data.models import RobotPlatformData_MetaData

class RobotPlatformData_MetaDataSerializer(ValidatedModelSerializer):
    class Meta:
        model = RobotPlatformData_MetaData
        fields = (''date_added', 'current', 'metadata'')