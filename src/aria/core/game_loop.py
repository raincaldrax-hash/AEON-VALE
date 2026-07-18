"""Game loop - Orchestrates game tick and update cycles."""

from typing import Optional
import time
from aria.core.world import World


class GameLoop:
    """Main game loop that orchestrates game updates and state management."""

    def __init__(self, world: World, target_fps: int = 60):
        """Initialize the game loop.
        
        Args:
            world: The game world
            target_fps: Target frames per second
        """
        self.world = world
        self.target_fps = target_fps
        self.frame_time = 1.0 / target_fps
        self.running = False
        self.current_tick = 0

    def start(self) -> None:
        """Start the game loop."""
        self.running = True
        last_time = time.time()

        while self.running:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time

            # Cap delta time to prevent large jumps
            if delta_time > self.frame_time * 2:
                delta_time = self.frame_time

            self.update(delta_time)
            self.current_tick += 1

            # Sleep to maintain target FPS
            elapsed = time.time() - current_time
            sleep_time = max(0, self.frame_time - elapsed)
            if sleep_time > 0:
                time.sleep(sleep_time)

    def stop(self) -> None:
        """Stop the game loop."""
        self.running = False

    def update(self, delta_time: float) -> None:
        """Update the game state.
        
        Args:
            delta_time: Time elapsed since last update in seconds
        """
        # Update world
        self.world.update(delta_time)

    def get_tick(self) -> int:
        """Get the current game tick.
        
        Returns:
            The current tick number
        """
        return self.current_tick
