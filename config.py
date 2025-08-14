"""
Configuration module for TPAO Bot
Centralizes all constants and configuration settings
"""
from dataclasses import dataclass
from typing import Tuple
import os
from pynput import keyboard

# File paths
CONFIG_FILE = "configuracion.txt"
VERSION = "1.0.0"

# Screen resolution limits
MAX_SCREEN_WIDTH = 1920
MAX_SCREEN_HEIGHT = 1080

# Hotkey combinations
INTERACT_KEYS = [
    { keyboard.KeyCode(char='x'), keyboard.KeyCode(char='c')}
]
CLOSE_KEYS = [
    {keyboard.KeyCode(char='x'), keyboard.KeyCode(char='b')}
]

# Timing constants (in seconds)
CLICK_DELAY = 0.05
MEDITATION_DELAY = 0.07
CYCLE_DELAY = 0.1

# UI constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720
CONFIG_WINDOW_WIDTH_PERCENT = 35
CONFIG_WINDOW_HEIGHT_PERCENT = 25

@dataclass
class BotConfig:
    """Configuration data class for bot settings"""
    meditation_key: str
    golpe_key: str
    click_position: Tuple[int, int]
    
    @classmethod
    def from_file(cls, filepath: str) -> 'BotConfig':
        """Load configuration from file"""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")
        
        config_data = {}
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if '=' in line:
                    key, value = line.strip().split('=', 1)
                    config_data[key] = value
        
        return cls(
            meditation_key=config_data.get('TECLA_MEDITAR', ''),
            golpe_key=config_data.get('TECLA_GOLPE', ''),
            click_position=(
                int(config_data.get('POSICION_LANZAR_X', 0)),
                int(config_data.get('POSICION_LANZAR_Y', 0))
            )
        )
    
    def save_to_file(self, filepath: str) -> None:
        """Save configuration to file"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"TECLA_MEDITAR={self.meditation_key}\n")
            f.write(f"TECLA_GOLPE={self.golpe_key}\n")
            f.write(f"POSICION_LANZAR_X={self.click_position[0]}\n")
            f.write(f"POSICION_LANZAR_Y={self.click_position[1]}\n")
