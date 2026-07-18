"""Quest system - Quest tracking and progression."""

from typing import Dict, List, Optional
from enum import Enum


class QuestStatus(Enum):
    """Quest status enumeration."""
    AVAILABLE = "available"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    ABANDONED = "abandoned"


class Quest:
    """Represents a quest."""

    def __init__(self, quest_id: str, title: str, description: str):
        """Initialize a quest.
        
        Args:
            quest_id: Unique quest identifier
            title: Quest title
            description: Quest description
        """
        self.quest_id = quest_id
        self.title = title
        self.description = description
        self.status = QuestStatus.AVAILABLE
        self.objectives: List[str] = []
        self.completed_objectives: List[str] = []
        self.rewards: Dict[str, int] = {"experience": 0, "gold": 0}
        self.giver = None

    def add_objective(self, objective: str) -> None:
        """Add an objective to the quest.
        
        Args:
            objective: Description of the objective
        """
        self.objectives.append(objective)

    def complete_objective(self, objective: str) -> bool:
        """Mark an objective as complete.
        
        Args:
            objective: The objective to complete
            
        Returns:
            True if objective was completed, False if not found
        """
        if objective in self.objectives and objective not in self.completed_objectives:
            self.completed_objectives.append(objective)
            return True
        return False

    def is_complete(self) -> bool:
        """Check if all objectives are completed.
        
        Returns:
            True if all objectives are completed
        """
        return len(self.completed_objectives) == len(self.objectives) and len(self.objectives) > 0

    def set_status(self, status: QuestStatus) -> None:
        """Set the quest status.
        
        Args:
            status: The new status
        """
        self.status = status

    def set_reward(self, reward_type: str, amount: int) -> None:
        """Set a reward for the quest.
        
        Args:
            reward_type: Type of reward (e.g., 'experience', 'gold')
            amount: Amount of reward
        """
        self.rewards[reward_type] = amount

    def __repr__(self) -> str:
        return f"Quest(id={self.quest_id}, title={self.title}, status={self.status.value})"
