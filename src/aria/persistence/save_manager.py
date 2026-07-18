"""Save manager - Game state serialization and persistence."""

import json
import pickle
from typing import Any, Dict, Optional
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class SaveManager:
    """Manages game state saving and loading."""

    def __init__(self, save_dir: str = "saves"):
        """Initialize the save manager.
        
        Args:
            save_dir: Directory to store save files
        """
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(exist_ok=True)

    def save_game(self, filename: str, game_state: Dict[str, Any]) -> bool:
        """Save game state to a file.
        
        Args:
            filename: Name of the save file
            game_state: Dictionary containing game state
            
        Returns:
            True if save was successful
        """
        try:
            filepath = self.save_dir / filename
            with open(filepath, 'wb') as f:
                pickle.dump(game_state, f)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    def load_game(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load game state from a file.
        
        Args:
            filename: Name of the save file
            
        Returns:
            Dictionary containing game state or None if failed
        """
        try:
            filepath = self.save_dir / filename
            with open(filepath, 'rb') as f:
                game_state = pickle.load(f)
            return game_state
        except Exception as e:
            print(f"Error loading game: {e}")
            return None

    def load_yaml(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load YAML configuration file.
        
        Args:
            filename: Name of the YAML file
            
        Returns:
            Dictionary containing YAML data or None if failed
        """
        if not HAS_YAML:
            print("PyYAML is not installed")
            return None

        try:
            filepath = self.save_dir / filename
            with open(filepath, 'r') as f:
                data = yaml.safe_load(f)
            return data
        except Exception as e:
            print(f"Error loading YAML: {e}")
            return None

    def delete_save(self, filename: str) -> bool:
        """Delete a save file.
        
        Args:
            filename: Name of the save file
            
        Returns:
            True if deletion was successful
        """
        try:
            filepath = self.save_dir / filename
            filepath.unlink()
            return True
        except Exception as e:
            print(f"Error deleting save: {e}")
            return False

    def list_saves(self) -> list:
        """List all save files.
        
        Returns:
            List of save filenames
        """
        return [f.name for f in self.save_dir.glob("*") if f.is_file()]
