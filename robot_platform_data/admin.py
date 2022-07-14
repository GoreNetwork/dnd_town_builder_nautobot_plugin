from django.contrib import admin
from robot_platform_data.models import RobotPlatformData_MetaData
from robot_platform_data.models import RobotPlatformData_CxtaTests_log
# from robot_platform_data.models import RobotPlatformData_CxtaTests_output
# from robot_platform_data.models import RobotPlatformData_CxtaTests_report

@admin.register(RobotPlatformData_MetaData)
class RobotPlatformData_MetaDataAdmin(admin.ModelAdmin):
    list_display = ("date_added", "current", "metadata")


@admin.register(RobotPlatformData_CxtaTests_log)
class RobotPlatformData_CxtaTests_logAdmin(admin.ModelAdmin):
    list_display = ("date_added", "log_content")


# @admin.register(RobotPlatformData_CxtaTests_output)
# class RobotPlatformData_CxtaTests_outputAdmin(admin.ModelAdmin):
#     list_display = ("date_added", "log_content")

# @admin.register(RobotPlatformData_CxtaTests_report)
# class RobotPlatformData_CxtaTests_reportAdmin(admin.ModelAdmin):
#     list_display = ("date_added", "log_content")