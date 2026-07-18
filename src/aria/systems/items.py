"""Item system - Items and inventory management."""

from typing import Dict, Any, Optional
from enum import Enum


class ItemType(Enum):
    """Item type enumeration."""
    WEAPON = "weapon"
    ARMOR = "armor"
    CONSUMABLE = "consumable"
    QUEST = "quest"
    MISC = "misc"


class Item:
    """Represents an item in the game."""

    def __init__(self, name: str, item_type: ItemType, value: int = 0):
        """Initialize an item.
        
        Args:
            name: Item name
            item_type: Type of item
            value: Gold value of the item
        """
        self.name = name
        self.item_type = item_type
        self.value = value
        self.properties: Dict[str, Any] = {}
        self.unique = False
        self.quantity = 1

    def add_property(self, key: str, value: Any) -> None:
        """Add a property to the item.
        
        Args:
            key: Property name
            value: Property value
        """
        self.properties[key] = value

    def get_property(self, key: str) -> Optional[Any]:
        """Get an item property.
        
        Args:
            key: Property name
            
        Returns:
            Property value or None
        """
        return self.properties.get(key)

    def __repr__(self) -> str:
        return f"Item(name={self.name}, type={self.item_type.value}, value={self.value})"
