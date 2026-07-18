"""Celestial hierarchy system - Angels, Archangels, and divine beings."""

from typing import Dict, List, Optional, Set
from enum import Enum
from aria.core.entity import Entity


class CelestialRank(Enum):
    """Enumeration of celestial ranks."""
    MORTAL = "mortal"
    DEMIGOD = "demigod"
    ARCHANGEL = "archangel"


class Archangel(Entity):
    """Represents an Archangel - the highest celestial being (apart from God).
    
    Archangels are immutable in rank and role. Their positions are fixed at world start.
    """
    
    # Biblical Archangels
    ARCHANGELS_DATA = {
        "Michael": {
            "title": "The Warrior",
            "domain": "Protection and Divine Will",
            "description": "Leader of God's armies, defender against evil",
            "symbol": "Sword and Shield",
            "alignment": "Lawful Good"
        },
        "Gabriel": {
            "title": "The Messenger",
            "domain": "Divine Messages and Communication",
            "description": "Messenger of God, announcer of divine will",
            "symbol": "Trumpet",
            "alignment": "Neutral Good"
        },
        "Raphael": {
            "title": "The Healer",
            "domain": "Healing and Guidance",
            "description": "Guide to lost travelers, healer of the wounded",
            "symbol": "Staff with Serpent",
            "alignment": "Lawful Good"
        },
        "Uriel": {
            "title": "The Fire of God",
            "domain": "Divine Retribution and Wisdom",
            "description": "Guardian of divine knowledge, enforcer of divine justice",
            "symbol": "Flaming Sword",
            "alignment": "Lawful Neutral"
        },
        "Raguel": {
            "title": "The Friend of God",
            "domain": "Harmony and Relationships",
            "description": "Mediator of divine disputes, promoter of harmony",
            "symbol": "Wings of Light",
            "alignment": "Chaotic Good"
        },
        "Zadkiel": {
            "title": "The Mercy of God",
            "domain": "Forgiveness and Benevolence",
            "description": "Angel of forgiveness and compassion",
            "symbol": "Violet Flame",
            "alignment": "Chaotic Good"
        },
        "Chamuel": {
            "title": "The Strength of God",
            "domain": "Strength and Courage",
            "description": "Provider of courage and inner strength",
            "symbol": "Spear of Light",
            "alignment": "Neutral Good"
        },
    }
    
    def __init__(self, archangel_name: str):
        """Initialize an Archangel.
        
        Args:
            archangel_name: Name of the archangel (must be in ARCHANGELS_DATA)
            
        Raises:
            ValueError: If archangel name is not recognized
        """
        if archangel_name not in self.ARCHANGELS_DATA:
            raise ValueError(f"Unknown archangel: {archangel_name}")
        
        super().__init__(archangel_name, "archangel")
        self.celestial_rank = CelestialRank.ARCHANGEL
        self.data = self.ARCHANGELS_DATA[archangel_name]
        self.title = self.data["title"]
        self.domain = self.data["domain"]
        self.symbol = self.data["symbol"]
        self.alignment = self.data["alignment"]
        self.immutable = True  # Archangel rank cannot be usurped or changed
        
        # Powers of archangels
        self.power_level = 1000  # Highest power level
        self.immortal = True
        self.can_be_defeated = False  # Cannot be permanently defeated in this world
    
    def get_description(self) -> str:
        """Get full description of the archangel."""
        return f"{self.name} - {self.title}\nDomain: {self.domain}\n{self.data['description']}"
    
    def __repr__(self) -> str:
        return f"Archangel({self.name}, domain={self.domain})"


class Demigod(Entity):
    """Represents a Demigod - an evolved mortal being of immense power.
    
    Demigods can be created through evolution of non-demon/non-angel races.
    A maximum of 2 demigods can exist per race at any time.
    Demigod positions can be usurped by defeating or killing an existing demigod.
    """
    
    def __init__(self, name: str, race: str, original_class: str):
        """Initialize a Demigod.
        
        Args:
            name: Name of the demigod
            race: Race of the demigod (e.g., 'human', 'elf', 'dwarf')
            original_class: Original character class before ascension
        """
        super().__init__(name, "demigod")
        self.celestial_rank = CelestialRank.DEMIGOD
        self.race = race
        self.original_class = original_class
        self.title = f"Demigod of {race}"
        
        # Demigod capabilities
        self.power_level = 750  # Second highest power level
        self.immortal = True
        self.can_be_defeated = True  # Can be permanently defeated and replaced
        self.can_usurp_rank = True  # Position can be taken by defeating them
        
        self.apotheosis_time = 0  # Time when ascended to demigod status
        self.followers: Set[str] = set()  # Names of followers
        self.domain: Optional[str] = None  # Domain of influence
        self.legacy_abilities: List[str] = []  # Abilities gained through apotheosis
    
    def set_domain(self, domain: str) -> None:
        """Set the demigod's domain of influence.
        
        Args:
            domain: Area of influence (e.g., 'War', 'Knowledge', 'Nature')
        """
        self.domain = domain
        self.title = f"Demigod of {self.domain}"
    
    def add_legacy_ability(self, ability: str) -> None:
        """Add a legacy ability granted through ascension.
        
        Args:
            ability: Name of the ability
        """
        self.legacy_abilities.append(ability)
    
    def add_follower(self, follower_name: str) -> None:
        """Add a follower.
        
        Args:
            follower_name: Name of the follower
        """
        self.followers.add(follower_name)
    
    def remove_follower(self, follower_name: str) -> None:
        """Remove a follower.
        
        Args:
            follower_name: Name of the follower
        """
        self.followers.discard(follower_name)
    
    def __repr__(self) -> str:
        domain_str = f", domain={self.domain}" if self.domain else ""
        return f"Demigod({self.name}, race={self.race}{domain_str})"


class CelestialHierarchyManager:
    """Manages the celestial hierarchy system."""
    
    def __init__(self):
        """Initialize the celestial hierarchy manager."""
        self.archangels: Dict[str, Archangel] = {}
        self.demigods: Dict[str, Demigod] = {}
        self.demigods_per_race: Dict[str, List[str]] = {}  # race -> list of demigod names
        self.max_demigods_per_race = 2
    
    def initialize_archangels(self) -> None:
        """Initialize all archangels at world start."""
        for archangel_name in Archangel.ARCHANGELS_DATA.keys():
            archangel = Archangel(archangel_name)
            self.archangels[archangel_name] = archangel
    
    def ascend_to_demigod(self, character: Entity, race: str, domain: str) -> Optional[Demigod]:
        """Attempt to ascend a character to demigod status.
        
        Args:
            character: The character attempting to ascend
            race: Race of the character
            domain: Domain of influence for the demigod
            
        Returns:
            Demigod entity if ascension successful, None otherwise
        """
        # Check if race has space for another demigod
        current_demigods = self.demigods_per_race.get(race, [])
        
        if len(current_demigods) >= self.max_demigods_per_race:
            return None  # Cannot exceed max demigods per race
        
        # Create demigod
        demigod = Demigod(
            character.name,
            race,
            character.entity_type
        )
        demigod.set_domain(domain)
        
        # Register demigod
        self.demigods[demigod.name] = demigod
        if race not in self.demigods_per_race:
            self.demigods_per_race[race] = []
        self.demigods_per_race[race].append(demigod.name)
        
        return demigod
    
    def usurp_demigod_rank(self, challenger: Entity, target_demigod: Demigod) -> bool:
        """Attempt to usurp a demigod's rank by defeating them.
        
        Args:
            challenger: Character challenging the demigod
            target_demigod: The demigod being challenged
            
        Returns:
            True if usurpation successful, False otherwise
        """
        if not target_demigod.can_be_defeated:
            return False
        
        # In a real system, this would be based on combat results
        # For now, we assume successful defeat and return True
        # The actual combat logic would be handled by the combat system
        return target_demigod.can_be_defeated
    
    def remove_demigod(self, demigod_name: str) -> bool:
        """Remove a demigod from the hierarchy (after defeat/death).
        
        Args:
            demigod_name: Name of the demigod to remove
            
        Returns:
            True if removal successful, False otherwise
        """
        if demigod_name not in self.demigods:
            return False
        
        demigod = self.demigods[demigod_name]
        race = demigod.race
        
        # Remove from demigods list
        del self.demigods[demigod_name]
        
        # Remove from race-specific list
        if race in self.demigods_per_race:
            self.demigods_per_race[race].remove(demigod_name)
        
        return True
    
    def get_archangel(self, name: str) -> Optional[Archangel]:
        """Get an archangel by name.
        
        Args:
            name: Name of the archangel
            
        Returns:
            Archangel entity or None
        """
        return self.archangels.get(name)
    
    def get_demigod(self, name: str) -> Optional[Demigod]:
        """Get a demigod by name.
        
        Args:
            name: Name of the demigod
            
        Returns:
            Demigod entity or None
        """
        return self.demigods.get(name)
    
    def get_demigods_by_race(self, race: str) -> List[Demigod]:
        """Get all demigods of a specific race.
        
        Args:
            race: Race name
            
        Returns:
            List of demigods of that race
        """
        demigod_names = self.demigods_per_race.get(race, [])
        return [self.demigods[name] for name in demigod_names if name in self.demigods]
    
    def get_hierarchy_status(self) -> Dict:
        """Get the current status of the celestial hierarchy.
        
        Returns:
            Dictionary with hierarchy information
        """
        return {
            "archangels": len(self.archangels),
            "demigods": len(self.demigods),
            "demigods_by_race": {
                race: len(names) for race, names in self.demigods_per_race.items()
            }
        }
