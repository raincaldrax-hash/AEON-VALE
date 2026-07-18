"""Offline engine - Single-player game engine."""

from aria.core.world import World
from aria.core.game_loop import GameLoop


class OfflineEngine:
    """Single-player game engine that runs offline."""

    def __init__(self, world: Optional['World'] = None):
        """Initialize the offline engine.
        
        Args:
            world: The game world (creates new if None)
        """
        self.world = world or World()
        self.game_loop = GameLoop(self.world)
        self.paused = False

    def start(self) -> None:
        """Start the game."""
        if not self.paused:
            self.game_loop.start()

    def pause(self) -> None:
        """Pause the game."""
        self.paused = True
        self.game_loop.stop()

    def resume(self) -> None:
        """Resume the game."""
        self.paused = False
        self.game_loop.start()

    def stop(self) -> None:
        """Stop the game."""
        self.game_loop.stop()
