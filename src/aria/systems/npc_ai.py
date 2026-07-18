"""NPC AI system - Behavior trees and decision-making for NPCs."""

from typing import List, Dict, Any, Optional
from aria.systems.ai_base import AIBase
from aria.game.character import Character


class NPCBehavior(AIBase):
    """AI behavior for NPCs."""

    def __init__(self, npc_name: str, personality: str = "neutral"):
        """Initialize NPC behavior.
        
        Args:
            npc_name: Name of the NPC
            personality: Personality type (e.g., 'friendly', 'hostile', 'neutral')
        """
        super().__init__(npc_name)
        self.personality = personality
        self.dialogue_tree: Dict[str, Any] = {}
        self.relationships: Dict[str, float] = {}  # NPC name -> affinity
        self.daily_routine: List[str] = []
        self.current_location = "home"

    def add_dialogue(self, key: str, response: str) -> None:
        """Add dialogue option.
        
        Args:
            key: Dialogue key
            response: NPC response
        """
        self.dialogue_tree[key] = response

    def get_dialogue(self, key: str) -> Optional[str]:
        """Get NPC dialogue.
        
        Args:
            key: Dialogue key
            
        Returns:
            NPC response or None
        """
        return self.dialogue_tree.get(key)

    def set_relationship(self, character_name: str, affinity: float) -> None:
        """Set relationship with a character.
        
        Args:
            character_name: Name of the character
            affinity: Affinity level (-100 to 100)
        """
        self.relationships[character_name] = max(-100, min(100, affinity))

    def modify_relationship(self, character_name: str, change: float) -> None:
        """Modify relationship with a character.
        
        Args:
            character_name: Name of the character
            change: Amount to change affinity
        """
        current = self.relationships.get(character_name, 0)
        self.set_relationship(character_name, current + change)

    def think(self, world_state: Dict[str, Any]) -> str:
        """Make a decision based on world state.
        
        Args:
            world_state: Current world state
            
        Returns:
            Action to perform
        """
        # Simple behavior based on personality
        if self.personality == "friendly":
            return "greet"
        elif self.personality == "hostile":
            return "attack"
        else:
            return "idle"

    def act(self, action: str) -> None:
        """Execute an action.
        
        Args:
            action: Action to execute
        """
        # Action execution would go here
        pass
