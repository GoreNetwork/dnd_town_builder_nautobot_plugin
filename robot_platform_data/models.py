"""Model definition for robot_platform_data."""

from django.db import models

from nautobot.core.models import BaseModel

from datetime import datetime

now = datetime.now()

class RobotPlatformData_MetaData(BaseModel):
    date_added = models.DateTimeField(auto_now=True, verbose_name="Date Data Added To DB",editable=False,)
    current = models.BooleanField(verbose_name="This Is The Current Data", default=True)
    metadata = models.JSONField(verbose_name="The Data Cisco Provides About Compatibility")

    # def __json__(self):
    #     return metadata

    class Meta:
        ordering = ("-date_added", "pk")
        verbose_name = "Metadata"
        

class RobotPlatformData_CxtaTests_log(BaseModel):
    date_added = models.DateTimeField(auto_now=True, verbose_name="Date Test Added To DB",editable=False,)
    log_content = models.TextField(verbose_name="Content Of log.html")

    # def __str__(self):
    #     return log_content

    class Meta:
        ordering = ("-date_added", "pk")
        verbose_name = "CXTA_log"
        verbose_name_plural = "CXTA_logs"
 

# class RobotPlatformData_CxtaTests_output(BaseModel):
#     date_added = models.DateTimeField(auto_now=True, verbose_name="Date Test Added To DB",editable=False,)
#     log_content = models.JSONField(verbose_name="Content Of output.xml")

#     # def __json__(self):
#     #     return log_content

#     class Meta:
#         ordering = ("-date_added", "pk")
#         verbose_name = "CXTA_output"
#         verbose_name_plural = "CXTA_outputs"

# class RobotPlatformData_CxtaTests_report(BaseModel):
#     date_added = models.DateTimeField(auto_now=True, verbose_name="Date Test Added To DB",editable=False,)
#     log_content = models.TextField(verbose_name="Content Of report.html")  

#     # def __str__(self):
#     #     return log_content

#     class Meta:
#         ordering = ("-date_added", "pk")
#         verbose_name = "CXTA_report"
#         verbose_name_plural = "CXTA_reports"        

# # Create your models here. Models should inherit from BaseModel.