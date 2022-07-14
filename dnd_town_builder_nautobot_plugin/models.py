from django.db import models
from nautobot.core.models import BaseModel
from nautobot.core.models.generics import OrganizationalModel, PrimaryModel
from datetime import datetime

#Default values for field uses, these are defined in build_db under build_models, defaults_for_fields
model_type=PrimaryModel
default_on_delete = models.RESTRICT

class Backgrounds(model_type):
    background=models.TextField()
    type=models.TextField()

class ServiceLocation(model_type):
    service_type=models.TextField()
    service=models.TextField()
    service_price_low=models.TextField()
    service_price_high=models.TextField()

class ServiceNames(model_type):
    name_part=models.TextField()
    Name=models.TextField()
    service_type=models.TextField()

class CharName(model_type):
    race=models.TextField()
    name_part=models.TextField()
    name=models.TextField()
    sex=models.TextField()

class StoreName(model_type):
    store_type=models.TextField()
    name_part=models.TextField()
    name=models.TextField()

class StoreItems(model_type):
    store_type=models.TextField()
    item_name=models.TextField()
    item_price=models.TextField()
    item_rarity=models.TextField()

class TownName(model_type):
    name_part=models.TextField()
    name=models.TextField()