"""Race system - Character race definitions."""

from typing import Dict, List, Any
from enum import Enum


class RaceType(Enum):
    """Enumeration of character races."""
    HUMAN = "human"
    ELF = "elf"
    DWARF = "dwarf"
    ORC = "orc"
    HALFLING = "halfling"


class Race:
    """Represents a character race."""

    def __init__(self, name: str, race_type: RaceType):
        """Initialize a race.
        
        Args:
            name: Race name
            race_type: Type of race
        """
        self.name = name
        self.race_type = race_type
        self.attribute_bonuses: Dict[str, int] = {}
        self.abilities: List[str] = []
        self.description = ""
        self.size = "medium"
        self.speed = 30  # Movement speed

    def add_attribute_bonus(self, attribute: str, bonus: int) -> None:
        """Add an attribute bonus for this race.
        
        Args:
            attribute: Attribute name
            bonus: Bonus value
        """
        self.attribute_bonuses[attribute] = bonus

    def add_ability(self, ability: str) -> None:
        """Add a racial ability.
        
        Args:
            ability: Ability name
        """
        self.abilities.append(ability)

    def get_attribute_bonuses(self) -> Dict[str, int]:
        """Get all attribute bonuses.
        
        Returns:
            Dictionary of attribute bonuses
        """
        return self.attribute_bonuses.copy()

    def get_abilities(self) -> List[str]:
        """Get all racial abilities.
        
        Returns:
            List of abilities
        """
        return self.abilities.copy()

    def __repr__(self) -> str:
        return f"Race(name={self.name}, type={self.race_type.value})"
