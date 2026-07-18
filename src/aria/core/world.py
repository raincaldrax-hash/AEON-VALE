"""World system - Manages the game world state."""

from typing import Dict, List, Optional
from aria.core.entity import Entity


class World:
    """Represents the game world and manages all entities."""

    def __init__(self, name: str = "Default World"):
        """Initialize the world.
        
        Args:
            name: The name of the world
        """
        self.name = name
        self.entities: Dict[str, Entity] = {}
        self.time = 0.0
        self.day_cycle = 0

    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the world.
        
        Args:
            entity: The entity to add
        """
        self.entities[entity.id] = entity

    def remove_entity(self, entity_id: str) -> None:
        """Remove an entity from the world.
        
        Args:
            entity_id: The ID of the entity to remove
        """
        if entity_id in self.entities:
            del self.entities[entity_id]

    def get_entity(self, entity_id: str) -> Optional[Entity]:
        """Get an entity by ID.
        
        Args:
            entity_id: The ID of the entity
            
        Returns:
            The entity or None if not found
        """
        return self.entities.get(entity_id)

    def get_entities_by_type(self, entity_type: str) -> List[Entity]:
        """Get all entities of a specific type.
        
        Args:
            entity_type: The type of entity to retrieve
            
        Returns:
            List of entities of the specified type
        """
        return [e for e in self.entities.values() if e.entity_type == entity_type]

    def update(self, delta_time: float) -> None:
        """Update the world state.
        
        Args:
            delta_time: Time elapsed since last update in seconds
        """
        self.time += delta_time
        self.day_cycle = int(self.time // 1440)  # 1440 seconds per day

        # Update all entities
        for entity in list(self.entities.values()):
            if entity.active:
                entity.update(delta_time)

    def __repr__(self) -> str:
        return f"World(name={self.name}, entities={len(self.entities)}, time={self.time})"
