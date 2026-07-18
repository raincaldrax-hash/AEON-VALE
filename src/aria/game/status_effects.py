"""Status effects and conditions system."""

from typing import Dict, List, Optional


class EffectType:
    """Types of status effects."""
    BUFF = "buff"
    DEBUFF = "debuff"
    DOT = "dot"  # Damage over time
    HOT = "hot"  # Heal over time
    CROWD_CONTROL = "crowd_control"
    IMMUNITY = "immunity"
    TRANSFORMATION = "transformation"


class StatusEffect:
    """Represents a status effect applied to a character."""
    
    def __init__(self, name: str, effect_type: str, duration: int):
        """Initialize a status effect.
        
        Args:
            name: Name of the effect
            effect_type: Type of effect
            duration: Duration in turns (0 = permanent until removed)
        """
        self.name = name
        self.effect_type = effect_type
        self.duration = duration
        self.remaining_duration = duration
        self.intensity = 1.0  # Intensity multiplier (0.0-2.0)
        self.stacks = 1  # Number of times effect is applied
        self.source = "unknown"  # Who applied this effect
        self.properties: Dict[str, any] = {}
    
    def tick(self) -> bool:
        """Reduce duration by one turn.
        
        Returns:
            True if effect is still active, False if expired
        """
        if self.duration > 0:  # Don't reduce permanent effects
            self.remaining_duration -= 1
        return self.remaining_duration > 0 or self.duration == 0
    
    def stack(self, max_stacks: int = 5) -> None:
        """Add a stack to the effect.
        
        Args:
            max_stacks: Maximum number of stacks
        """
        if self.stacks < max_stacks:
            self.stacks += 1
            # Increase intensity with stacks
            self.intensity = 1.0 + (self.stacks - 1) * 0.2
    
    def is_expired(self) -> bool:
        """Check if effect has expired.
        
        Returns:
            True if effect duration is 0
        """
        return self.remaining_duration <= 0 and self.duration > 0
    
    def __repr__(self) -> str:
        stacks_str = f" x{self.stacks}" if self.stacks > 1 else ""
        return f"StatusEffect({self.name}{stacks_str}, {self.remaining_duration}/{self.duration} turns)"


class Condition:
    """Special permanent conditions (cursed, blessed, etc.)."""
    
    def __init__(self, name: str, description: str = ""):
        """Initialize a condition.
        
        Args:
            name: Name of the condition
            description: Description of the condition
        """
        self.name = name
        self.description = description
        self.active = True
        self.properties: Dict[str, any] = {}
    
    def set_property(self, key: str, value: any) -> None:
        """Set a property.
        
        Args:
            key: Property key
            value: Property value
        """
        self.properties[key] = value
    
    def get_property(self, key: str) -> Optional[any]:
        """Get a property.
        
        Args:
            key: Property key
            
        Returns:
            Property value or None
        """
        return self.properties.get(key)
    
    def __repr__(self) -> str:
        return f"Condition({self.name})"


class StatusEffectManager:
    """Manages status effects for a character."""
    
    def __init__(self):
        """Initialize the status effect manager."""
        self.active_effects: Dict[str, StatusEffect] = {}  # name -> effect
        self.conditions: Dict[str, Condition] = {}  # name -> condition
    
    def apply_effect(self, effect: StatusEffect) -> None:
        """Apply a status effect.
        
        Args:
            effect: The effect to apply
        """
        if effect.name in self.active_effects:
            # Stack effect if it already exists
            existing = self.active_effects[effect.name]
            existing.stack()
        else:
            self.active_effects[effect.name] = effect
    
    def remove_effect(self, effect_name: str) -> bool:
        """Remove a status effect.
        
        Args:
            effect_name: Name of the effect to remove
            
        Returns:
            True if effect was removed, False if not found
        """
        if effect_name in self.active_effects:
            del self.active_effects[effect_name]
            return True
        return False
    
    def get_effect(self, effect_name: str) -> Optional[StatusEffect]:
        """Get a status effect.
        
        Args:
            effect_name: Name of the effect
            
        Returns:
            StatusEffect or None
        """
        return self.active_effects.get(effect_name)
    
    def has_effect(self, effect_name: str) -> bool:
        """Check if character has an effect.
        
        Args:
            effect_name: Name of the effect
            
        Returns:
            True if effect is active
        """
        return effect_name in self.active_effects
    
    def tick_effects(self) -> List[str]:
        """Tick all active effects by one turn.
        
        Returns:
            List of expired effect names
        """
        expired = []
        for effect_name, effect in list(self.active_effects.items()):
            if not effect.tick():
                expired.append(effect_name)
                del self.active_effects[effect_name]
        return expired
    
    def add_condition(self, condition: Condition) -> None:
        """Add a condition.
        
        Args:
            condition: The condition to add
        """
        self.conditions[condition.name] = condition
    
    def remove_condition(self, condition_name: str) -> bool:
        """Remove a condition.
        
        Args:
            condition_name: Name of the condition
            
        Returns:
            True if removed, False if not found
        """
        if condition_name in self.conditions:
            del self.conditions[condition_name]
            return True
        return False
    
    def has_condition(self, condition_name: str) -> bool:
        """Check if character has a condition.
        
        Args:
            condition_name: Name of the condition
            
        Returns:
            True if condition is active
        """
        return condition_name in self.conditions
    
    def get_all_effects(self) -> Dict[str, StatusEffect]:
        """Get all active effects.
        
        Returns:
            Dictionary of all active effects
        """
        return self.active_effects.copy()
    
    def get_all_conditions(self) -> Dict[str, Condition]:
        """Get all conditions.
        
        Returns:
            Dictionary of all conditions
        """
        return self.conditions.copy()
    
    def clear_effects(self) -> int:
        """Clear all temporary effects.
        
        Returns:
            Number of effects cleared
        """
        count = len(self.active_effects)
        self.active_effects.clear()
        return count
