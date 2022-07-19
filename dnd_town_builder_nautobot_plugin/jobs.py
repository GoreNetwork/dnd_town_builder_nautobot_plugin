"""Maintenance Jobs."""
import os
# from nautobot.extras.jobs import Job

# name = "Maintenance Event Jobs"

# class CheckDeviceMaintenanceEvents(Job):
#     """Job that validates if a given date has an associated maintenance event."""
#     class Meta:
#         """Meta class for CheckDeviceMaintenanceEvents"""

#         name = "Check Device Maintenance Events"
#         description = "Verify if a maintenance event is associated to a device for a given date."
#         read_only = True

#     def run(self, data=None, commit=None):
#         """Executes the job"""
#         print ("bob")
#         pass

# run = [CheckDeviceMaintenanceEvents]


# import time
import yaml
from nautobot.extras.jobs import IntegerVar, Job
from yaml.loader import SafeLoader
from dnd_town_builder_nautobot_plugin.models import Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName 



name = "Import data into Database"
class ImportdataIntoDatabase(Job):
    # interval = IntegerVar(default=4, description="The time in seconds to sleep.")

    class Meta:
        name = "Populate the Database from the yml files."
        description = ("Populate the Database from the yml files.")

    def import_yml_file(self, yml_file):
        with open(yml_file) as f:
            data = yaml.load(f, Loader=SafeLoader)
        return data

    def build_race_names(self):
        print('bob')
        self.log_info(os.getcwdb())
        races = ['dwarf',
                'elf',
                'human',
                ]
        for race in races:
            file_name = f"/opt/nautobot/plugin/dnd_town_builder_nautobot_plugin/names/{race}.yml"
            file_data = self.import_yml_file(file_name)
            for gender in file_data['first']:
                print (gender)
                for name in file_data['first'][gender]:
                    name_part='first'
                    table_update, created = CharName.objects.get_or_create(
                        race=race,
                        name_part=name_part,
                        name = name,
                        sex = gender
                    )
                    if created:
                        self.log_success( f"Added: {name}, {race}, {name_part}")
                    else:
                        self.log_info( f"Already Exists: {name}, {race}, {name_part}")
            if "adgitive" in file_data['last']:
                tmp_last = []
                for noun in file_data['last']['noun']:
                    for adgitive in file_data['last']['adgitive']:
                        tmp_last.append(f"{adgitive}{noun}")
                file_data['last']=tmp_last
            for name in file_data['last']:
                name_part="last"
                table_update, created = CharName.objects.get_or_create(
                    race=race,
                    name_part=name_part,
                    name = name,
                    sex = "None"
                )
                if created:
                    self.log_success( f"Name Added: {name}, {race}, {name_part}")
                else:
                    self.log_info( f"Name Already Exists: {name}, {race}, {name_part}")

    def build_items_for_sale(self):
        store_types = ['combat_store',
                'general_store',
                'magic_store',
                ]
        for store_type_name in store_types:
            file_name = f"/opt/nautobot/plugin/dnd_town_builder_nautobot_plugin/store_items/{store_type_name}.yml"
            store_type = self.import_yml_file(file_name)
            for name_part in store_type['names']:
                for name in store_type['names'][name_part]:
                    table_update, created = StoreName.objects.get_or_create(
                        store_type=store_type_name,
                        name_part = name_part,
                        name=name)
                    if created:
                        self.log_success( f"Store Name Added: {name}, {store_type_name}, {name_part}")
                    else:
                        self.log_info( f"Store Name Already Exists: {name}, {store_type_name}, {name_part}")
            for rarity_type in store_type:
                if 'names'==rarity_type:
                    continue
                for item_name in store_type[rarity_type]:
                    table_update, created = StoreItems.objects.get_or_create(
                        store_type=store_type_name,
                        item_price = store_type[rarity_type][item_name],
                        item_name=item_name,
                        item_rarity=rarity_type
                        )
                    if created:
                        self.log_success( f"Item Added: {item_name}")
                    else:
                        self.log_info( f"Item Already Exists: {item_name}")
    def build_town_names(self):
        file_name = f"/opt/nautobot/plugin/dnd_town_builder_nautobot_plugin/town_data/town_name_data.yml"
        town_name_data = self.import_yml_file(file_name)
        for name_part in town_name_data['names']:
            for name in town_name_data['names'][name_part]:
                table_update, created = TownName.objects.get_or_create(
                name_part = name_part,
                name = name,
                )
                if created:
                        self.log_success( f"TownName Item Added: {name}")
                else:
                    self.log_info( f"TownName Item Exists: {name}")

    def build_backgrounds(self):
        file_name = f"/opt/nautobot/plugin/dnd_town_builder_nautobot_plugin/backgrounds/backgrounds.yml"
        background_data = self.import_yml_file(file_name)
        for background_type in background_data:
            for background in background_data[background_type]:
                table_update, created = Backgrounds.objects.get_or_create(
                    background = background,
                    type = background_type,
                    )
                if created:
                        self.log_success( f"Background Item Added: {background}")
                else:
                    self.log_info( f"Background Item Exists: {background}")

    def build_general_locations(self):
        locations =['bakery',
                    'temple' ,             
                    'inn',
                    'wizard_services',]
        for location in locations:
            file_name = f"/opt/nautobot/plugin/dnd_town_builder_nautobot_plugin/general_locations/{location}.yml"
            location_data = self.import_yml_file(file_name)
            for name_part in location_data['names']:
                for name in location_data['names'][name_part]:
                    table_update, created = ServiceNames.objects.get_or_create(
                        Name=name,
                        name_part=name_part,
                        service_type = location,
                    )
                    if created:
                        self.log_success( f"ServiceName Added: {name}")
                    else:
                        self.log_info( f"ServiceName Exists: {name}")
            for service in location_data['services']:
                table_update, created = ServiceLocation.objects.get_or_create(
                        service_type=location,
                        service=service,
                        service_price_low=location_data['services'][service][0],
                        service_price_high=location_data['services'][service][1],
                    ) 
                if created:
                    self.log_success( f"Service Added: {name}")
                else:
                    self.log_info( f"Service Exists: {name}")



    def run(self, data, commit):
        self.build_race_names()
        self.build_items_for_sale()
        self.build_town_names()
        self.build_backgrounds()
        self.build_general_locations()


        # self.log_debug(message=f"Running for {interval} seconds.")
        # for step in range(1, interval + 1):
        #     time.sleep(1)
        #     self.log_info(message=f"Step {step}")
        # self.log_success(obj=None)
        # return f"Ran for {interval} seconds"


jobs = ( ImportdataIntoDatabase,)