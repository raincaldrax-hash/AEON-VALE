"""Entity system - Base classes for all game objects."""

from typing import Dict, Any, Optional
import uuid


class Entity:
    """Base class for all entities in the game world."""

    def __init__(self, name: str, entity_type: str):
        """Initialize an entity.
        
        Args:
            name: The name of the entity
            entity_type: The type of entity (e.g., 'player', 'npc', 'monster')
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.entity_type = entity_type
        self.attributes: Dict[str, Any] = {}
        self.active = True

    def add_attribute(self, name: str, value: Any) -> None:
        """Add an attribute to the entity.
        
        Args:
            name: Attribute name
            value: Attribute value
        """
        self.attributes[name] = value

    def get_attribute(self, name: str) -> Optional[Any]:
        """Get an attribute value.
        
        Args:
            name: Attribute name
            
        Returns:
            The attribute value or None if not found
        """
        return self.attributes.get(name)

    def update(self, delta_time: float) -> None:
        """Update the entity state.
        
        Args:
            delta_time: Time elapsed since last update in seconds
        """
        pass

    def __repr__(self) -> str:
        return f"Entity(id={self.id}, name={self.name}, type={self.entity_type})"
