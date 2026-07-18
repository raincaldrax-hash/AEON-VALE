"""Dragon Gods system - Evolution path for dragon kin races."""

from typing import Dict, List, Optional, Set
from enum import Enum
from aria.core.entity import Entity


class DragonType(Enum):
    """Types of dragons and their elemental affinities."""
    FIRE = "fire"
    FROST = "frost"
    STORM = "storm"
    NATURE = "nature"
    VOID = "void"
    CELESTIAL = "celestial"
    SHADOW = "shadow"


class DragonGod(Entity):
    """Represents a Dragon God - the ultimate evolution of dragon kin.
    
    Dragon Gods are the highest rank achievable by dragon kin races.
    Similar to demigods, a maximum of 2 can exist per dragon kin race.
    Positions can be usurped by defeating a dragon god.
    """
    
    def __init__(self, name: str, dragon_type: DragonType, original_race: str, original_class: str):
        """Initialize a Dragon God.
        
        Args:
            name: Name of the dragon god
            dragon_type: Type/element of the dragon
            original_race: Dragon kin race (e.g., 'Drakeling', 'Dragonborn')
            original_class: Original class before ascension
        """
        super().__init__(name, "dragon_god")
        self.dragon_type = dragon_type
        self.original_race = original_race
        self.original_class = original_class
        self.title = f"Dragon God of {dragon_type.value.capitalize()}"
        
        # Dragon God capabilities
        self.power_level = 800  # Very high, between demigods and primordial demons
        self.immortal = True
        self.can_be_defeated = True
        self.can_usurp_rank = True
        
        # Dragon-specific attributes
        self.hoard: Dict[str, int] = {}  # Name -> quantity of treasures/artifacts
        self.draconic_magic: List[str] = []  # Draconic spells and abilities
        self.territory: Optional[str] = None  # Territory controlled
        self.aeons_lived = 0  # Age in years
        self.dragon_followers: Set[str] = set()  # Names of dragon kin followers
        
        # Elemental affinity
        self.elemental_power = 100  # Maximum elemental power (0-100)
        self.breath_weapons: Dict[str, str] = {}  # Type -> description
    
    def add_to_hoard(self, item: str, quantity: int = 1) -> None:
        """Add an item to the dragon's hoard.
        
        Args:
            item: Name of the item/treasure
            quantity: Quantity to add
        """
        if item not in self.hoard:
            self.hoard[item] = 0
        self.hoard[item] += quantity
    
    def add_draconic_magic(self, spell: str) -> None:
        """Add a draconic spell or ability.
        
        Args:
            spell: Name of the spell/ability
        """
        if spell not in self.draconic_magic:
            self.draconic_magic.append(spell)
    
    def add_breath_weapon(self, weapon_type: str, description: str) -> None:
        """Add a breath weapon ability.
        
        Args:
            weapon_type: Type of breath weapon (e.g., 'Fire Breath', 'Frost Breath')
            description: Description of the ability
        """
        self.breath_weapons[weapon_type] = description
    
    def set_territory(self, territory: str) -> None:
        """Set the territory controlled by this dragon god.
        
        Args:
            territory: Name of the territory
        """
        self.territory = territory
    
    def add_follower(self, follower_name: str) -> None:
        """Add a dragon kin follower.
        
        Args:
            follower_name: Name of the follower
        """
        self.dragon_followers.add(follower_name)
    
    def remove_follower(self, follower_name: str) -> None:
        """Remove a dragon kin follower.
        
        Args:
            follower_name: Name of the follower
        """
        self.dragon_followers.discard(follower_name)
    
    def age_dragon(self, years: int) -> None:
        """Age the dragon god.
        
        Args:
            years: Years to age
        """
        self.aeons_lived += years
    
    def __repr__(self) -> str:
        territory_str = f", territory={self.territory}" if self.territory else ""
        return f"DragonGod({self.name}, type={self.dragon_type.value}, race={self.original_race}{territory_str})"


class Wyrmling(Entity):
    """Represents a young dragon kin with potential to become a Dragon God.
    
    Wyrmlings are young dragon kin on the path to becoming Dragon Gods.
    """
    
    def __init__(self, name: str, dragon_type: DragonType, original_race: str):
        """Initialize a Wyrmling.
        
        Args:
            name: Name of the wyrmling
            dragon_type: Type/element of the dragon
            original_race: Dragon kin race
        """
        super().__init__(name, "wyrmling")
        self.dragon_type = dragon_type
        self.original_race = original_race
        
        # Wyrmling capabilities
        self.power_level = 400  # Moderate power, can grow
        self.immortal = False  # Can be killed
        self.can_ascend = True  # Can become dragon god
        
        # Dragon attributes
        self.hoard: Dict[str, int] = {}
        self.draconic_magic: List[str] = []
        self.aeons_lived = 0
        self.elemental_affinity = 30  # Out of 100
    
    def add_to_hoard(self, item: str, quantity: int = 1) -> None:
        """Add an item to the wyrmling's hoard.
        
        Args:
            item: Name of the item/treasure
            quantity: Quantity to add
        """
        if item not in self.hoard:
            self.hoard[item] = 0
        self.hoard[item] += quantity
    
    def learn_draconic_magic(self, spell: str) -> None:
        """Learn a draconic spell.
        
        Args:
            spell: Name of the spell
        """
        if spell not in self.draconic_magic:
            self.draconic_magic.append(spell)
    
    def __repr__(self) -> str:
        return f"Wyrmling({self.name}, type={self.dragon_type.value}, race={self.original_race})"


class DragonGodsManager:
    """Manages the dragon gods hierarchy system."""
    
    def __init__(self):
        """Initialize the dragon gods manager."""
        self.dragon_gods: Dict[str, DragonGod] = {}
        self.wyrmlings: Dict[str, Wyrmling] = {}
        self.dragon_gods_per_race: Dict[str, List[str]] = {}  # race -> list of dragon god names
        self.max_dragon_gods_per_race = 2
        self.dragon_kin_races = [
            "Drakeling",
            "Dragonborn",
            "Kobold",
            "Drake"
        ]
    
    def create_wyrmling(self, name: str, dragon_type: DragonType, race: str) -> Optional[Wyrmling]:
        """Create a wyrmling (young dragon).
        
        Args:
            name: Name of the wyrmling
            dragon_type: Type of dragon
            race: Dragon kin race
            
        Returns:
            Wyrmling entity or None if invalid race
        """
        if race not in self.dragon_kin_races:
            return None
        
        wyrmling = Wyrmling(name, dragon_type, race)
        self.wyrmlings[wyrmling.name] = wyrmling
        return wyrmling
    
    def ascend_to_dragon_god(self, wyrmling: Wyrmling) -> Optional[DragonGod]:
        """Attempt to ascend a wyrmling to dragon god status.
        
        Args:
            wyrmling: The wyrmling attempting to ascend
            
        Returns:
            DragonGod entity if ascension successful, None otherwise
        """
        # Check if race has space for another dragon god
        current_gods = self.dragon_gods_per_race.get(wyrmling.original_race, [])
        
        if len(current_gods) >= self.max_dragon_gods_per_race:
            return None  # Cannot exceed max dragon gods per race
        
        # Create dragon god
        dragon_god = DragonGod(
            wyrmling.name,
            wyrmling.dragon_type,
            wyrmling.original_race,
            "dragon"
        )
        
        # Transfer wyrmling's hoard and knowledge
        dragon_god.hoard = wyrmling.hoard.copy()
        dragon_god.draconic_magic = wyrmling.draconic_magic.copy()
        dragon_god.aeons_lived = wyrmling.aeons_lived
        
        # Register dragon god
        self.dragon_gods[dragon_god.name] = dragon_god
        if wyrmling.original_race not in self.dragon_gods_per_race:
            self.dragon_gods_per_race[wyrmling.original_race] = []
        self.dragon_gods_per_race[wyrmling.original_race].append(dragon_god.name)
        
        # Remove from wyrmlings
        if wyrmling.name in self.wyrmlings:
            del self.wyrmlings[wyrmling.name]
        
        return dragon_god
    
    def ascend_character_to_dragon_god(self, character: Entity, dragon_type: DragonType, dragon_race: str, original_class: str) -> Optional[DragonGod]:
        """Ascend a character directly to dragon god status (for specific cases).
        
        Args:
            character: The character to ascend
            dragon_type: Type of dragon
            dragon_race: Dragon kin race
            original_class: Original class before ascension
            
        Returns:
            DragonGod entity if ascension successful, None otherwise
        """
        if dragon_race not in self.dragon_kin_races:
            return None
        
        # Check if race has space
        current_gods = self.dragon_gods_per_race.get(dragon_race, [])
        
        if len(current_gods) >= self.max_dragon_gods_per_race:
            return None
        
        # Create dragon god
        dragon_god = DragonGod(
            character.name,
            dragon_type,
            dragon_race,
            original_class
        )
        
        # Register dragon god
        self.dragon_gods[dragon_god.name] = dragon_god
        if dragon_race not in self.dragon_gods_per_race:
            self.dragon_gods_per_race[dragon_race] = []
        self.dragon_gods_per_race[dragon_race].append(dragon_god.name)
        
        return dragon_god
    
    def usurp_dragon_god_rank(self, challenger: Entity, target_god: DragonGod) -> bool:
        """Attempt to usurp a dragon god's rank by defeating them.
        
        Args:
            challenger: Character challenging the dragon god
            target_god: The dragon god being challenged
            
        Returns:
            True if usurpation successful, False otherwise
        """
        if not target_god.can_be_defeated:
            return False
        
        return target_god.can_be_defeated
    
    def remove_dragon_god(self, god_name: str) -> bool:
        """Remove a dragon god from the hierarchy (after defeat/death).
        
        Args:
            god_name: Name of the dragon god to remove
            
        Returns:
            True if removal successful, False otherwise
        """
        if god_name not in self.dragon_gods:
            return False
        
        dragon_god = self.dragon_gods[god_name]
        race = dragon_god.original_race
        
        # Remove from dragon gods list
        del self.dragon_gods[god_name]
        
        # Remove from race-specific list
        if race in self.dragon_gods_per_race:
            self.dragon_gods_per_race[race].remove(god_name)
        
        return True
    
    def get_dragon_god(self, name: str) -> Optional[DragonGod]:
        """Get a dragon god by name.
        
        Args:
            name: Name of the dragon god
            
        Returns:
            DragonGod entity or None
        """
        return self.dragon_gods.get(name)
    
    def get_wyrmling(self, name: str) -> Optional[Wyrmling]:
        """Get a wyrmling by name.
        
        Args:
            name: Name of the wyrmling
            
        Returns:
            Wyrmling entity or None
        """
        return self.wyrmlings.get(name)
    
    def get_dragon_gods_by_race(self, race: str) -> List[DragonGod]:
        """Get all dragon gods of a specific race.
        
        Args:
            race: Race name
            
        Returns:
            List of dragon gods of that race
        """
        god_names = self.dragon_gods_per_race.get(race, [])
        return [self.dragon_gods[name] for name in god_names if name in self.dragon_gods]
    
    def get_dragon_gods_by_type(self, dragon_type: DragonType) -> List[DragonGod]:
        """Get all dragon gods of a specific type.
        
        Args:
            dragon_type: Type of dragon
            
        Returns:
            List of dragon gods of that type
        """
        return [god for god in self.dragon_gods.values() if god.dragon_type == dragon_type]
    
    def get_hierarchy_status(self) -> Dict:
        """Get the current status of the dragon gods hierarchy.
        
        Returns:
            Dictionary with hierarchy information
        """
        return {
            "dragon_gods": len(self.dragon_gods),
            "wyrmlings": len(self.wyrmlings),
            "dragon_gods_by_race": {
                race: len(names) for race, names in self.dragon_gods_per_race.items()
            },
            "dragon_gods_by_type": {
                dtype.value: len(self.get_dragon_gods_by_type(dtype))
                for dtype in DragonType
            }
        }
    
    def get_available_dragon_god_slots(self) -> Dict[str, int]:
        """Get available slots for dragon gods by race.
        
        Returns:
            Dictionary with race -> available slots
        """
        available_slots = {}
        for race in self.dragon_kin_races:
            current_gods = len(self.dragon_gods_per_race.get(race, []))
            available_slots[race] = self.max_dragon_gods_per_race - current_gods
        return available_slots
