# TPAO Bot - Improved Version

An automated spell-casting bot for TPAO game with improved code structure and maintainability.

## Features

- **Automated Spell Casting**: Automatically clicks at specified coordinates and presses meditation key
- **Hotkey Controls**: 
  - `X + C`: Start/stop the bot
  - `X + B`: Exit the program
- **Configuration Management**: Save and load bot settings
- **User-Friendly GUI**: Simple interface for configuration and control
- **Error Handling**: Robust error handling and validation

## Installation

1. **Clone or download** the project files
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**:
   ```bash
   python improved_main.py
   ```

## Usage

### First Time Setup

1. Launch the application
2. Click "Configurar" (Configure)
3. Enter your meditation key (single character)
4. Enter click coordinates (X, Y) based on your screen resolution
5. Click "Guardar y Iniciar" (Save and Start)

### Screen Resolution Coordinates

| Resolution | X Position | Y Position |
|------------|------------|------------|
| 1920x1080  | 1446       | 659        |
| 1600x900   | 1300       | 570        |
| 1366x768   | 1192       | 507        |
| 1280x720   | 1143       | 481        |
| Fullscreen | 1138       | 475        |

### Controls

- **X + C**: Toggle bot on/off
- **X + B**: Exit the program completely

## Project Structure

```
Level_Bot_TPAO/
├── improved_main.py      # Main application entry point
├── config.py            # Configuration constants and data classes
├── validators.py        # Input validation logic
├── bot_engine.py        # Core bot automation engine
├── requirements.txt     # Python dependencies
├── README_IMPROVED.md   # This file
└── configuracion.txt    # Saved configuration (auto-generated)
```

## Code Improvements

### ✅ What Was Fixed

1. **Modular Architecture**: Separated concerns into different modules
2. **Type Hints**: Added proper type annotations for better code clarity
3. **Error Handling**: Comprehensive try-catch blocks and validation
4. **Code Reusability**: Eliminated duplicate validation code
5. **Configuration Management**: Centralized configuration handling
6. **Documentation**: Added docstrings and comments
7. **Constants**: Moved magic numbers to configuration constants
8. **Better Naming**: Consistent and descriptive variable names

### 🔧 Key Improvements

- **`config.py`**: Centralizes all constants and configuration
- **`validators.py`**: Dedicated validation module with custom exceptions
- **`bot_engine.py`**: Cleaner bot logic with better state management
- **`improved_main.py`**: Better UI structure and error handling

## Development

### Adding New Features

1. **Configuration**: Add new settings to `config.py`
2. **Validation**: Add validation rules to `validators.py`
3. **Bot Logic**: Extend `bot_engine.py` for new automation features
4. **UI**: Update `improved_main.py` for new interface elements

### Testing

```bash
# Run the improved version
python improved_main.py

# Test configuration loading
python -c "from config import BotConfig; print(BotConfig.from_file('configuracion.txt'))"
```

## Security Notes

⚠️ **Important**: This bot automates game actions. Use responsibly and in accordance with the game's terms of service.

## Troubleshooting

### Common Issues

1. **"Configuration file not found"**: Run the configuration setup first
2. **"Invalid coordinates"**: Check your screen resolution and use correct coordinates
3. **"Permission denied"**: Run as administrator if needed for mouse/keyboard access

### Debug Mode

Add debug prints to `bot_engine.py` to monitor bot activity:

```python
print(f"Bot state: active={self.is_active}, meditating={self.is_meditating}")
```

## License

This project is for educational purposes. Use responsibly.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make improvements
4. Test thoroughly
5. Submit a pull request

---

**Note**: This is an improved version of the original bot with better code structure, error handling, and maintainability.
