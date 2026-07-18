"""Combat actions and abilities system."""

from typing import Dict, List, Optional, Callable
from enum import Enum
from dataclasses import dataclass


class ActionType(Enum):
    """Types of combat actions."""
    ATTACK = "attack"
    ABILITY = "ability"
    SPELL = "spell"
    DEFEND = "defend"
    DODGE = "dodge"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"
    ITEM = "item"
    FLEE = "flee"


class TargetType(Enum):
    """Types of action targets."""
    SELF = "self"
    SINGLE = "single"
    ALL_ALLIES = "all_allies"
    ALL_ENEMIES = "all_enemies"
    AREA = "area"


@dataclass
class ActionCost:
    """Cost of performing an action."""
    health: int = 0
    mana: int = 0
    energy: int = 0
    stamina: int = 0
    
    def can_afford(self, actor_health: int, actor_mana: int, actor_energy: int = 100, actor_stamina: int = 100) -> bool:
        """Check if actor can afford the cost.
        
        Args:
            actor_health: Actor's current health
            actor_mana: Actor's current mana
            actor_energy: Actor's current energy
            actor_stamina: Actor's current stamina
            
        Returns:
            True if actor can afford the cost
        """
        return (
            actor_health > self.health and
            actor_mana >= self.mana and
            actor_energy >= self.energy and
            actor_stamina >= self.stamina
        )


class CombatAction:
    """Represents a combat action (attack, ability, spell, etc.)."""
    
    def __init__(self, name: str, action_type: ActionType):
        """Initialize a combat action.
        
        Args:
            name: Name of the action
            action_type: Type of action
        """
        self.name = name
        self.action_type = action_type
        self.description = ""
        self.target_type = TargetType.SINGLE
        self.cost = ActionCost()
        self.cooldown = 0  # Turns until action can be used again
        self.current_cooldown = 0
        self.accuracy = 100  # Percentage hit chance
        self.priority = 0  # Higher priority acts first in a turn
        self.effect_function: Optional[Callable] = None
    
    def set_effect(self, effect_func: Callable) -> None:
        """Set the effect function for this action.
        
        Args:
            effect_func: Function that applies the action's effects
        """
        self.effect_function = effect_func
    
    def can_use(self) -> bool:
        """Check if action is off cooldown.
        
        Returns:
            True if action can be used
        """
        return self.current_cooldown == 0
    
    def use(self) -> None:
        """Use the action (sets cooldown)."""
        self.current_cooldown = self.cooldown
    
    def tick_cooldown(self) -> None:
        """Reduce cooldown by one turn."""
        if self.current_cooldown > 0:
            self.current_cooldown -= 1
    
    def __repr__(self) -> str:
        return f"CombatAction({self.name}, type={self.action_type.value})"


class Ability:
    """Represents a character ability."""
    
    def __init__(self, name: str, ability_type: str):
        """Initialize an ability.
        
        Args:
            name: Name of the ability
            ability_type: Type of ability (e.g., 'passive', 'active', 'racial')
        """
        self.name = name
        self.ability_type = ability_type
        self.description = ""
        self.level = 1
        self.max_level = 5
        self.passive = ability_type == "passive"
        self.effects: Dict[str, any] = {}
    
    def upgrade(self) -> bool:
        """Upgrade the ability.
        
        Returns:
            True if upgraded, False if at max level
        """
        if self.level < self.max_level:
            self.level += 1
            return True
        return False
    
    def get_effect_multiplier(self) -> float:
        """Get effect multiplier based on ability level.
        
        Returns:
            Effect multiplier (1.0 at level 1)
        """
        return 1.0 + (self.level - 1) * 0.2
    
    def __repr__(self) -> str:
        return f"Ability({self.name}, level={self.level}/{self.max_level})"


class Skill:
    """Represents a character skill."""
    
    def __init__(self, name: str, skill_type: str):
        """Initialize a skill.
        
        Args:
            name: Name of the skill
            skill_type: Type of skill (e.g., 'combat', 'magic', 'survival')
        """
        self.name = name
        self.skill_type = skill_type
        self.experience = 0
        self.level = 1  # 1-10 scale
        self.proficiency = 0.0  # 0-1.0
    
    def gain_experience(self, amount: int) -> None:
        """Gain skill experience.
        
        Args:
            amount: Amount of experience to gain
        """
        self.experience += amount
        # Level up every 100 exp
        if self.experience >= self.level * 100 and self.level < 10:
            self.level += 1
            self.proficiency = min(1.0, self.level / 10.0)
    
    def get_damage_multiplier(self) -> float:
        """Get damage multiplier based on skill level.
        
        Returns:
            Damage multiplier
        """
        return 1.0 + (self.level - 1) * 0.15
    
    def __repr__(self) -> str:
        return f"Skill({self.name}, level={self.level}, proficiency={self.proficiency:.2f})"
