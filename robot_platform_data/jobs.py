"""Maintenance Jobs."""
from nautobot.extras.jobs import Job
import urllib.request
import json
# from nautobot.dcim.models import RobotPlatformData_MetaData
from robot_platform_data.models import RobotPlatformData_MetaData
from robot_platform_data.models import RobotPlatformData_CxtaTests_log
name = "Maintenance Event Jobs"


class ImportMetadataIntoDatabase(Job):
    """Job that downloads the metadata file, and imports it into the database."""
    class Meta:
        

        name = "Import metadata into database"
        description = "Job that downloads the metadata file, and imports it into the database."

    def read_json_from_url(self, url):
        file = urllib.request.urlopen(url)
        output=''
        for line in file:
            output=output+line. decode("utf-8")
        output = json.loads(output)
        return output

    def get_url(self):
        return 'https://support.oneskyapp.com/hc/en-us/article_attachments/202761627/example_1.json'

    def run(self, data=None, commit=None):
        """Executes the job"""
        url = self.get_url()
        metadata = self.read_json_from_url(url)
        entry = RobotPlatformData_MetaData(
            metadata=metadata,
            current=True,
        )
        entry.validated_save()
        self.log_success(obj=RobotPlatformData_MetaData, message=metadata)

jobs=[ImportMetadataIntoDatabase]