"""Demonic hierarchy system - Primordial Demons, Demonoids, and Dark Evolution."""

from typing import Dict, List, Optional, Set
from enum import Enum
from aria.core.entity import Entity


class DemonicRank(Enum):
    """Enumeration of demonic ranks."""
    MORTAL = "mortal"
    DEMONOID = "demonoid"
    PRIMORDIAL_DEMON = "primordial_demon"


class DeadlySin(Enum):
    """The seven deadly sins represented by primordial demons."""
    PRIDE = "pride"
    GREED = "greed"
    WRATH = "wrath"
    ENVY = "envy"
    LUST = "lust"
    GLUTTONY = "gluttony"
    SLOTH = "sloth"


class PrimordialDemon(Entity):
    """Represents a Primordial Demon - the darkest of all entities.
    
    Primordial demons embody one of the seven deadly sins.
    Only 7 can exist at any time (one per sin).
    Positions can be usurped by defeating a primordial demon.
    Both demons and humans (who descend into demonoids) can become primordial demons.
    """
    
    # Primordial Demons of the Seven Sins
    DEMONS_DATA = {
        "Lucifer": {
            "sin": DeadlySin.PRIDE,
            "title": "The Proud One",
            "domain": "Arrogance and Self-Exaltation",
            "description": "Embodies pride and rebellion against the divine",
            "symbol": "Crown and Flame",
            "alignment": "Chaotic Evil"
        },
        "Mammon": {
            "sin": DeadlySin.GREED,
            "title": "The Wealthy",
            "domain": "Avarice and Material Hunger",
            "description": "Embodies greed and endless acquisition",
            "symbol": "Gold and Scales",
            "alignment": "Neutral Evil"
        },
        "Azazel": {
            "sin": DeadlySin.WRATH,
            "title": "The Furious",
            "domain": "Rage and Destruction",
            "description": "Embodies wrath and violent destruction",
            "symbol": "Flame and Serpent",
            "alignment": "Chaotic Evil"
        },
        "Leviathan": {
            "sin": DeadlySin.ENVY,
            "title": "The Jealous",
            "domain": "Resentment and Comparison",
            "description": "Embodies envy and corrosive jealousy",
            "symbol": "Serpent and Mirror",
            "alignment": "Chaotic Evil"
        },
        "Asmodeus": {
            "sin": DeadlySin.LUST,
            "title": "The Lustful",
            "domain": "Desire and Temptation",
            "description": "Embodies lust and base desires",
            "symbol": "Chains and Fire",
            "alignment": "Chaotic Evil"
        },
        "Beelzebub": {
            "sin": DeadlySin.GLUTTONY,
            "title": "The Devourer",
            "domain": "Consumption and Excess",
            "description": "Embodies gluttony and endless consumption",
            "symbol": "Mouth and Void",
            "alignment": "Neutral Evil"
        },
        "Belphegor": {
            "sin": DeadlySin.SLOTH,
            "title": "The Lazy",
            "domain": "Apathy and Inertia",
            "description": "Embodies sloth and spiritual torpor",
            "symbol": "Throne and Chains",
            "alignment": "Neutral Evil"
        }
    }
    
    def __init__(self, demon_name: str, original_form: str = "primordial"):
        """Initialize a Primordial Demon.
        
        Args:
            demon_name: Name of the demon (must be in DEMONS_DATA)
            original_form: What form the demon took (e.g., 'demon', 'demonoid', 'primordial')
            
        Raises:
            ValueError: If demon name is not recognized
        """
        if demon_name not in self.DEMONS_DATA:
            raise ValueError(f"Unknown primordial demon: {demon_name}")
        
        super().__init__(demon_name, "primordial_demon")
        self.demonic_rank = DemonicRank.PRIMORDIAL_DEMON
        self.data = self.DEMONS_DATA[demon_name]
        self.sin = self.data["sin"]
        self.title = self.data["title"]
        self.domain = self.data["domain"]
        self.symbol = self.data["symbol"]
        self.alignment = self.data["alignment"]
        self.original_form = original_form  # Track if they were demon or demonoid
        
        # Powers of primordial demons
        self.power_level = 850  # Very high but can be challenged
        self.immortal = True
        self.can_be_defeated = True  # Can be defeated and replaced
        self.can_usurp_rank = True
        
        self.corruption_level = 100  # Maximum corruption (0-100)
        self.cultists: Set[str] = set()  # Names of worshippers
        self.artifacts: List[str] = []  # Demonic artifacts
    
    def get_description(self) -> str:
        """Get full description of the primordial demon."""
        origin = f"(Originally {self.original_form})" if self.original_form != "primordial" else ""
        return f"{self.name} - {self.title} {origin}\nSin: {self.sin.value.capitalize()}\nDomain: {self.domain}\n{self.data['description']}"
    
    def add_cultist(self, cultist_name: str) -> None:
        """Add a cultist/worshipper.
        
        Args:
            cultist_name: Name of the cultist
        """
        self.cultists.add(cultist_name)
    
    def remove_cultist(self, cultist_name: str) -> None:
        """Remove a cultist.
        
        Args:
            cultist_name: Name of the cultist
        """
        self.cultists.discard(cultist_name)
    
    def add_artifact(self, artifact_name: str) -> None:
        """Add a demonic artifact.
        
        Args:
            artifact_name: Name of the artifact
        """
        self.artifacts.append(artifact_name)
    
    def __repr__(self) -> str:
        return f"PrimordialDemon({self.name}, sin={self.sin.value}, origin={self.original_form})"


class Demonoid(Entity):
    """Represents a Demonoid - a mortal (typically human) who has chosen the path of darkness.
    
    Demonoids are mortals who embraced demonic power and corruption.
    They can potentially ascend to Primordial Demon status by claiming a sin.
    """
    
    def __init__(self, name: str, original_race: str, original_class: str):
        """Initialize a Demonoid.
        
        Args:
            name: Name of the demonoid
            original_race: Original race before demonification
            original_class: Original class before demonification
        """
        super().__init__(name, "demonoid")
        self.demonic_rank = DemonicRank.DEMONOID
        self.original_race = original_race
        self.original_class = original_class
        
        # Demonoid capabilities
        self.power_level = 600  # Powerful but below demigods
        self.immortal = False  # Can be killed
        self.can_be_defeated = True
        self.can_ascend = True  # Can ascend to primordial demon
        
        self.corruption_level = 50  # Current corruption (0-100, ascending path)
        self.affiliated_sin: Optional[DeadlySin] = None  # Which sin they embody
        self.demonic_abilities: List[str] = []
        self.dark_pacts: Set[str] = set()  # Pacts made
    
    def set_affiliated_sin(self, sin: DeadlySin) -> None:
        """Set the sin this demonoid is aligned with.
        
        Args:
            sin: The deadly sin
        """
        self.affiliated_sin = sin
    
    def add_demonic_ability(self, ability: str) -> None:
        """Add a demonic ability.
        
        Args:
            ability: Name of the ability
        """
        self.demonic_abilities.append(ability)
    
    def increase_corruption(self, amount: float) -> None:
        """Increase corruption level.
        
        Args:
            amount: Amount to increase (can exceed 100 for ascension readiness)
        """
        self.corruption_level = min(amount, self.corruption_level + amount)
    
    def make_pact(self, pact_description: str) -> None:
        """Make a dark pact.
        
        Args:
            pact_description: Description of the pact
        """
        self.dark_pacts.add(pact_description)
    
    def __repr__(self) -> str:
        sin_str = f", sin={self.affiliated_sin.value}" if self.affiliated_sin else ""
        return f"Demonoid({self.name}, original_race={self.original_race}{sin_str})"


class DemonicHierarchyManager:
    """Manages the demonic hierarchy system."""
    
    def __init__(self):
        """Initialize the demonic hierarchy manager."""
        self.primordial_demons: Dict[str, PrimordialDemon] = {}
        self.demons_by_sin: Dict[DeadlySin, str] = {}  # sin -> demon name
        self.demonoids: Dict[str, Demonoid] = {}
        self.max_primordial_demons = 7  # One per sin
    
    def initialize_primordial_demons(self) -> None:
        """Initialize all primordial demons at world start."""
        for demon_name in PrimordialDemon.DEMONS_DATA.keys():
            demon = PrimordialDemon(demon_name, "primordial")
            self.primordial_demons[demon_name] = demon
            self.demons_by_sin[demon.sin] = demon_name
    
    def create_demonoid(self, character: Entity, original_race: str) -> Demonoid:
        """Transform a character into a demonoid.
        
        Args:
            character: The character to demonify
            original_race: The character's original race
            
        Returns:
            New Demonoid entity
        """
        demonoid = Demonoid(
            character.name,
            original_race,
            character.entity_type
        )
        self.demonoids[demonoid.name] = demonoid
        return demonoid
    
    def ascend_to_primordial_demon(self, demonoid: Demonoid, target_sin: DeadlySin) -> Optional[PrimordialDemon]:
        """Attempt to ascend a demonoid to primordial demon status.
        
        Args:
            demonoid: The demonoid attempting to ascend
            target_sin: The sin they wish to embody
            
        Returns:
            PrimordialDemon if ascension successful, None otherwise
        """
        # Check if the sin slot is occupied
        if target_sin in self.demons_by_sin:
            existing_demon_name = self.demons_by_sin[target_sin]
            existing_demon = self.primordial_demons[existing_demon_name]
            
            # Cannot ascend without defeating existing demon
            if existing_demon.can_be_defeated:
                return None  # Must defeat current holder
            else:
                return None  # Slot is immutable
        
        # Create primordial demon from demonoid
        primordial = PrimordialDemon(
            demonoid.name,
            demonoid.original_race
        )
        primordial.original_form = "demonoid"
        
        self.primordial_demons[primordial.name] = primordial
        self.demons_by_sin[target_sin] = primordial.name
        
        # Remove from demonoids
        if demonoid.name in self.demonoids:
            del self.demonoids[demonoid.name]
        
        return primordial
    
    def demon_ascend_to_primordial(self, demon_entity: Entity, target_sin: DeadlySin) -> Optional[PrimordialDemon]:
        """Demon entity ascends to primordial demon status.
        
        Args:
            demon_entity: The demon attempting to ascend
            target_sin: The sin they wish to embody
            
        Returns:
            PrimordialDemon if ascension successful, None otherwise
        """
        # Check if the sin slot is occupied
        if target_sin in self.demons_by_sin:
            existing_demon_name = self.demons_by_sin[target_sin]
            existing_demon = self.primordial_demons[existing_demon_name]
            
            if existing_demon.can_be_defeated:
                return None  # Must defeat current holder
            else:
                return None  # Slot is immutable
        
        # Create primordial demon from demon
        primordial = PrimordialDemon(
            demon_entity.name,
            "primordial"
        )
        
        self.primordial_demons[primordial.name] = primordial
        self.demons_by_sin[target_sin] = primordial.name
        
        return primordial
    
    def usurp_primordial_demon(self, challenger: Entity, target_demon: PrimordialDemon) -> bool:
        """Attempt to usurp a primordial demon's position by defeating them.
        
        Args:
            challenger: Character challenging the demon
            target_demon: The primordial demon being challenged
            
        Returns:
            True if usurpation successful, False otherwise
        """
        if not target_demon.can_be_defeated:
            return False
        
        # In a real system, this would be based on combat results
        return target_demon.can_be_defeated
    
    def remove_primordial_demon(self, demon_name: str) -> bool:
        """Remove a primordial demon from the hierarchy (after defeat/death).
        
        Args:
            demon_name: Name of the demon to remove
            
        Returns:
            True if removal successful, False otherwise
        """
        if demon_name not in self.primordial_demons:
            return False
        
        demon = self.primordial_demons[demon_name]
        
        # Remove from hierarchy
        del self.primordial_demons[demon_name]
        
        # Remove from sin mapping
        if demon.sin in self.demons_by_sin:
            del self.demons_by_sin[demon.sin]
        
        return True
    
    def get_primordial_demon(self, name: str) -> Optional[PrimordialDemon]:
        """Get a primordial demon by name.
        
        Args:
            name: Name of the demon
            
        Returns:
            PrimordialDemon entity or None
        """
        return self.primordial_demons.get(name)
    
    def get_primordial_demon_by_sin(self, sin: DeadlySin) -> Optional[PrimordialDemon]:
        """Get the primordial demon of a specific sin.
        
        Args:
            sin: The sin
            
        Returns:
            PrimordialDemon entity or None if sin is unclaimed
        """
        if sin in self.demons_by_sin:
            demon_name = self.demons_by_sin[sin]
            return self.primordial_demons.get(demon_name)
        return None
    
    def get_demonoid(self, name: str) -> Optional[Demonoid]:
        """Get a demonoid by name.
        
        Args:
            name: Name of the demonoid
            
        Returns:
            Demonoid entity or None
        """
        return self.demonoids.get(name)
    
    def get_hierarchy_status(self) -> Dict:
        """Get the current status of the demonic hierarchy.
        
        Returns:
            Dictionary with hierarchy information
        """
        claimed_sins = {}
        unclaimed_sins = []
        
        for sin in DeadlySin:
            if sin in self.demons_by_sin:
                demon_name = self.demons_by_sin[sin]
                claimed_sins[sin.value] = demon_name
            else:
                unclaimed_sins.append(sin.value)
        
        return {
            "primordial_demons": len(self.primordial_demons),
            "claimed_sins": claimed_sins,
            "unclaimed_sins": unclaimed_sins,
            "demonoids": len(self.demonoids)
        }
