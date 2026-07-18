"""Monster system - Monster definitions and AI."""

from typing import Dict, List, Any
from aria.core.entity import Entity


class Monster(Entity):
    """Represents a monster in the game world."""

    def __init__(self, name: str, level: int = 1):
        """Initialize a monster.
        
        Args:
            name: Monster name
            level: Monster level
        """
        super().__init__(name, "monster")
        self.level = level
        self.health = 50 * level
        self.max_health = self.health
        self.attack_power = 5 * level
        self.defense = 2 * level
        self.experience_reward = 100 * level
        self.loot_table: Dict[str, float] = {}
        self.ai_behavior = "passive"

    def set_ai_behavior(self, behavior: str) -> None:
        """Set the AI behavior type.
        
        Args:
            behavior: AI behavior type (e.g., 'passive', 'aggressive', 'defensive')
        """
        self.ai_behavior = behavior

    def add_loot(self, item: str, drop_chance: float) -> None:
        """Add an item to the loot table.
        
        Args:
            item: Item name
            drop_chance: Probability of dropping (0.0 to 1.0)
        """
        self.loot_table[item] = min(1.0, max(0.0, drop_chance))

    def take_damage(self, amount: int) -> None:
        """Take damage.
        
        Args:
            amount: Damage amount
        """
        # Apply defense reduction
        actual_damage = max(1, amount - self.defense)
        self.health = max(0, self.health - actual_damage)

    def is_alive(self) -> bool:
        """Check if monster is alive.
        
        Returns:
            True if health > 0
        """
        return self.health > 0

    def update(self, delta_time: float) -> None:
        """Update monster state.
        
        Args:
            delta_time: Time elapsed
        """
        # AI behavior implementation would go here
        pass
