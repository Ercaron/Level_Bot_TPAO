"""
Bot engine module for TPAO Bot
Handles the automated clicking and keyboard input
"""
import time
import threading
from typing import Tuple
from pynput.mouse import Button, Controller
from pynput import keyboard
from tkinter import messagebox
from config import INTERACT_KEYS, CLOSE_KEYS, CLICK_DELAY, MEDITATION_DELAY, CYCLE_DELAY


class BotEngine(threading.Thread):
    """
    Main bot engine that handles automated spell casting
    """
    
    def __init__(self, meditation_key: str, golpe_key: str, click_position: Tuple[int, int]):
        super().__init__()
        self.meditation_key = keyboard.KeyCode(char=meditation_key)
        self.golpe_key = keyboard.KeyCode(char=golpe_key)
        self.click_position = click_position
        self.mouse = Controller()
        self.start_position = (0, 0)
        
        # State flags
        self.is_running = True
        self.is_active = False
        self.is_meditating = False
        
        # Keyboard state tracking
        self.current_keys = set()
        
        print("Bot engine initialized and ready")
    
    def toggle_bot(self) -> None:
        """Toggle bot on/off"""
        self.is_active = not self.is_active
        if self.is_active:
            self.start_position = self.mouse.position
            print("Bot activated")
        else:
            print("Bot deactivated")
            self._stop_meditation()
    
    def _stop_meditation(self) -> None:
        """Stop meditation if active"""
        if self.is_meditating:
            keyboard.Controller().release(self.meditation_key)
            self.is_meditating = False
    
    def stop_bot(self) -> None:
        """Stop the bot completely"""
        self.is_active = False
        self.is_running = False
        self._stop_meditation()
        print("Bot stopped")
    
    def _perform_actions(self) -> None:
        """Perform one complete spell casting cycle"""
        # Move to click position and click
        self.mouse.position = self.click_position
        self.mouse.click(Button.left)
        
        # Return to original position and click
        self.mouse.position = self.start_position
        time.sleep(CLICK_DELAY)
        self.mouse.click(Button.left)
        
        # Start meditation
        
        keyboard.Controller().press(self.meditation_key)
        time.sleep(MEDITATION_DELAY)
        keyboard.Controller().release(self.meditation_key)
        self.is_meditating = True

        # Stop meditation
        keyboard.Controller().press(self.meditation_key)
        time.sleep(MEDITATION_DELAY)
        keyboard.Controller().release(self.meditation_key)
        self.is_meditating = False

        #Start golpe
        keyboard.Controller().press(self.golpe_key)
        time.sleep(0.02)
        keyboard.Controller().release(self.golpe_key)
        
        # Wait before next cycle
        time.sleep(CYCLE_DELAY)
    
    def run(self) -> None:
        """Main bot loop"""
        print("Bot engine started")
        
        while self.is_running:
            if self.is_active:
                try:
                    self._perform_actions()
                except Exception as e:
                    print(f"Error in bot loop: {e}")
                    self.is_active = False
            else:
                time.sleep(0.1)  # Small delay when inactive
    
    def on_key_press(self, key) -> None:
        """Handle key press events"""
        # If one of the action keys is pressed, we add it to the list
        if any([key in combo for combo in INTERACT_KEYS]):
            if key not in self.current_keys:
                self.current_keys.add(key)      
            
            # If all of the action required keys are pressed, change the state of the bot
            if any(all(k in self.current_keys for k in combo) for combo in INTERACT_KEYS):
                self.start_position = self.mouse.position
                self.toggle_bot()

        # Same as above but for closing the bot
        if any([key in combo for combo in CLOSE_KEYS]):
            if key not in self.current_keys:
                self.current_keys.add(key)
            if any(all(k in self.current_keys for k in combo) for combo in CLOSE_KEYS):
                self.stop_bot()
                return False  # Stop listener
    
    def on_key_release(self, key) -> None:
        """Handle key release events"""
        if any([key in combo for combo in INTERACT_KEYS]):
            if key in self.current_keys:
                self.current_keys.remove(key)
        elif any([key in combo for combo in CLOSE_KEYS]):
            if key in self.current_keys:
                self.current_keys.remove(key)


def start_bot(meditation_key: str, golpe_key: str, click_position: Tuple[int, int]) -> None:
    """
    Start the bot with the given configuration
    
    Args:
        meditation_key: Key to press for meditation
        golpe_key: Key to press for golpe
        click_position: (x, y) coordinates to click
    """
    bot = BotEngine(meditation_key, golpe_key, click_position)
    bot.start()
    
    # Set up keyboard listener
    with keyboard.Listener(
        on_press=bot.on_key_press,
        on_release=bot.on_key_release
    ) as listener:
        print("Bot ready - Press X+C to start/stop, X+B to exit") #TODO change for dynamic keys
        listener.join()
    
    messagebox.showinfo("Finalizado", "Gracias, vuelva pronto")
