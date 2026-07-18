"""Combat system - Battle mechanics and resolution."""

import random
from typing import Dict, List, Tuple
from aria.game.character import Character


class Combat:
    """Handles combat between characters."""

    def __init__(self):
        """Initialize the combat system."""
        self.combatants: List[Character] = []
        self.turn_order: List[Character] = []
        self.current_turn = 0

    def start_combat(self, *characters: Character) -> None:
        """Start a combat encounter.
        
        Args:
            *characters: Characters participating in combat
        """
        self.combatants = list(characters)
        self.turn_order = sorted(
            self.combatants,
            key=lambda c: c.stats["dexterity"],
            reverse=True
        )
        self.current_turn = 0

    def attack(self, attacker: Character, defender: Character) -> int:
        """Perform an attack action.
        
        Args:
            attacker: The attacking character
            defender: The defending character
            
        Returns:
            Damage dealt
        """
        # Base damage from strength
        base_damage = attacker.stats["strength"]
        # Add variance
        damage = base_damage + random.randint(-5, 10)
        damage = max(1, damage)  # Minimum 1 damage
        
        # Apply defense reduction
        defense = defender.stats["constitution"]
        final_damage = max(1, damage - defense // 2)
        
        defender.take_damage(final_damage)
        return final_damage

    def next_turn(self) -> Character:
        """Get the next character in turn order.
        
        Returns:
            The next character to take a turn
        """
        if not self.turn_order:
            return None
        
        current = self.turn_order[self.current_turn % len(self.turn_order)]
        self.current_turn += 1
        return current

    def get_combat_status(self) -> Dict:
        """Get the current status of combat.
        
        Returns:
            Dictionary with combat status
        """
        status = {}
        for character in self.combatants:
            status[character.name] = {
                "health": character.health,
                "max_health": character.max_health,
                "alive": character.is_alive(),
            }
        return status
