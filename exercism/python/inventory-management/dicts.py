"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create inventory dictionary from item list."""
    inventory = {}

    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def add_items(inventory, items):
    """Add or increment inventory items."""
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1

    return inventory


def decrement_items(inventory, items):
    """Decrease inventory counts safely."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory."""
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    """Return non-zero inventory items."""
    return [
        (item, count)
        for item, count in inventory.items()
        if count > 0
    ]