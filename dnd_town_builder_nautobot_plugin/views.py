"""Views for dnd_town_builder_nautobot_plugin."""

from django.shortcuts import render
from nautobot.core.views import generic
from pprint import pprint
import random
from django.views.generic import View


from dnd_town_builder_nautobot_plugin.models import Backgrounds, ServiceLocation, ServiceNames, CharName, StoreName, StoreItems, TownName 

def build_name_dict(queries):
    name_dict = {}
    for each in queries.values():
        if each['name_part'] not in name_dict:
            name_dict[each['name_part']]=[]
        
        name_dict[each['name_part']].append(each['name'])
    return name_dict

def build_name(name_dict, object_type):
    name = ''
    if 'last' in name_dict:
        name_dict['second']=name_dict['last']
    name = random.choice(name_dict['first'])
    name = f"{name} {random.choice(name_dict['second'])}"
    return name

def pull_background_and_flaws():
    backgrounds_query = Backgrounds.objects.all()
    backgrounds={}
    for each in backgrounds_query.values():
        if each['type'] not in backgrounds:
            backgrounds[each['type']]=[]
        backgrounds[each['type']].append(each['background'])            
    return backgrounds

def build_npcs(char_type):
    name_data = {}
    char_data = {}
    char_name_dict = CharName.objects.all()
    races = []
    npcs ={}
    backgrounds_and_flaws=pull_background_and_flaws()
    for each in char_name_dict.values():
        race = each['race'] 
        name_part = each['name_part']
        name = each['name']
        sex = each['sex']
        if race not in races:
            races.append(race)
            name_data[race]={}
        if name_part not in name_data[race]:
            name_data[race][name_part]=[]
        if name_part=='first':
            name_data[race][name_part].append([name, sex])
        else:
            name_data[race][name_part].append(name)
    pull_background_and_flaws()
    npc_name = ''
    race = random.choice(races)
    first_name, gender = random.choice(name_data[race]['first'])
    last_name = random.choice(name_data[race]['last'])
    name = f"{first_name} {last_name}"
    char_data['name']=name
    char_data['gender']= gender
    char_data['race']=race
    char_data['flaw'] = random.choice(backgrounds_and_flaws['flaws'])
    char_data['background']=random.choice(backgrounds_and_flaws[char_type])

    return char_data

def build_stores(store_type, how_many_stores, how_many_rares):
    store_name_queries = StoreName.objects.filter(store_type=store_type)
    store_name_data = build_name_dict(store_name_queries)
    store_items = StoreItems.objects.filter(store_type=store_type)
    items = []
    rare_items = []
    stores = []
    for item in store_items.values():
        tmp_item = {
            "name": item['item_name'],
            "rarity": item['item_rarity'],
            "price": item['item_price'], }
        items.append(tmp_item)
        if item['item_rarity'] != "common":
            rare_items.append(tmp_item)
    for each in range(0, how_many_stores):
        tmp_store = {}
        tmp_store['store_type']=store_type
        tmp_store['name'] = build_name(store_name_data, None)
        tmp_store['items'] = []
        for item in items:
            if item['rarity']=='common':
                tmp_store['items'].append(item)
        for each_two in range(0, how_many_rares):
            tmp_store['items'].append(random.choice(rare_items))
        tmp_store['owner'] = build_npcs('store_worker')
        stores.append(tmp_store)
    return stores

        

def build_city(request):

    if request.method=="POST":
        return built_city(request)
    if request.method=='GET':
        return render(request, 'dnd_town_builder_nautobot_plugin/build_city.html'  )

    # return render(request, 'dnd_town_builder_nautobot_plugin/build_city.html'  )


def built_city(request):
    print ("Build city request data****\n\n\n\n\n\n")
    pprint (dir(request.POST))
    pprint (request.POST)
    combat_store_number  = int(request.POST.get('combat_store_number' ))
    magic_store_number   = int(request.POST.get('magic_store_number'  ))
    general_store_number = int(request.POST.get('general_store_number'))
    combat_store_rare_items_number  = int(request.POST.get('combat_store_rare_items_number' ))
    magic_store_rare_items_number   = int(request.POST.get('magic_store_rare_items_number'  ))
    general_store_rare_items_number = int(request.POST.get('general_store_rare_items_number'))

    spare_npc_number = int(request.POST.get('spare_npc_number'))
    city = {}
    town_name_data = TownName.objects.all()
    name_dict = build_name_dict(town_name_data)
    city['name'] = build_name(name_dict, 'city')
    city['spair_npcs']=[]
    for each in range(0,spare_npc_number):
        city['spair_npcs'].append(build_npcs('extra_chars'))
    city['stores']=[]
    combat_stores = build_stores(store_type = 'combat_store', how_many_stores = combat_store_number, how_many_rares=combat_store_rare_items_number)
    for each in combat_stores:
        city['stores'].append(each)
    general_stores = build_stores(store_type = 'general_store', how_many_stores = general_store_number, how_many_rares=general_store_rare_items_number)
    for each in general_stores:
        city['stores'].append(each)
    magic_stores = build_stores(store_type = 'magic_store', how_many_stores = magic_store_number, how_many_rares=magic_store_rare_items_number)
    for each in magic_stores:
        city['stores'].append(each)
        
    return render(request, 'dnd_town_builder_nautobot_plugin/built_city.html', {
        'town_name_data':city['name'],
        'spair_npcs': city['spair_npcs'],
        'stores': city['stores']})
