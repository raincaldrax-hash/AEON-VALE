"""Character system - Player and NPC character management."""

from typing import Dict, List, Optional
from aria.core.entity import Entity


class Character(Entity):
    """Represents a character (player or NPC) in the game."""

    def __init__(self, name: str, char_class: str = "Adventurer"):
        """Initialize a character.
        
        Args:
            name: Character name
            char_class: Character class/profession
        """
        super().__init__(name, "character")
        self.char_class = char_class
        self.level = 1
        self.experience = 0
        self.health = 100
        self.max_health = 100
        self.mana = 50
        self.max_mana = 50
        self.inventory: List[str] = []
        self.stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10,
        }

    def gain_experience(self, amount: int) -> None:
        """Gain experience points.
        
        Args:
            amount: Amount of experience to gain
        """
        self.experience += amount
        # Level up every 100 experience
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self) -> None:
        """Increase the character's level."""
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.max_mana += 5
        self.mana = self.max_mana
        # Increase stats
        for stat in self.stats:
            self.stats[stat] += 1

    def take_damage(self, amount: int) -> None:
        """Take damage.
        
        Args:
            amount: Amount of damage to take
        """
        self.health = max(0, self.health - amount)

    def heal(self, amount: int) -> None:
        """Heal the character.
        
        Args:
            amount: Amount of health to restore
        """
        self.health = min(self.max_health, self.health + amount)

    def add_to_inventory(self, item: str) -> None:
        """Add an item to inventory.
        
        Args:
            item: The item to add
        """
        self.inventory.append(item)

    def remove_from_inventory(self, item: str) -> bool:
        """Remove an item from inventory.
        
        Args:
            item: The item to remove
            
        Returns:
            True if item was removed, False otherwise
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

    def is_alive(self) -> bool:
        """Check if the character is alive.
        
        Returns:
            True if health is above 0
        """
        return self.health > 0
