"""AI base system - Foundation for intelligent agents."""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class AIBase(ABC):
    """Base class for all AI agents in the game."""

    def __init__(self, name: str):
        """Initialize an AI agent.
        
        Args:
            name: Name of the AI agent
        """
        self.name = name
        self.state: Dict[str, Any] = {}
        self.memory: Dict[str, Any] = {}

    @abstractmethod
    def think(self, world_state: Dict[str, Any]) -> str:
        """Process world state and make a decision.
        
        Args:
            world_state: Current world state
            
        Returns:
            Action to perform
        """
        pass

    @abstractmethod
    def act(self, action: str) -> None:
        """Execute an action.
        
        Args:
            action: The action to execute
        """
        pass

    def update_memory(self, key: str, value: Any) -> None:
        """Update the AI's memory.
        
        Args:
            key: Memory key
            value: Memory value
        """
        self.memory[key] = value

    def recall(self, key: str) -> Optional[Any]:
        """Recall a memory.
        
        Args:
            key: Memory key
            
        Returns:
            The memory value or None
        """
        return self.memory.get(key)
