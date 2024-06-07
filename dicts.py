
def create_inventory(items):
    inventory={} 
    for item in items:
        if item not in inventory:
            inventory[item]=1
        else:
            inventory[item]=1
    return {}


def add_items(inventory, items):
    for item in items:
        if item not in inventory:
            inventory[item]=1
        else:
            inventory[item]+=1
    return {}


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[item]>0:
            inventory[item]-=1
    return {}


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return {}


def list_inventory(inventory):
    lista=[]
    for item, cant in inventory.items():
        if cant>0:
            lista.append((item, cant))
    return {}

