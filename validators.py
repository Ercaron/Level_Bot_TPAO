"""
Validation module for TPAO Bot
Centralizes all input validation logic
"""
from typing import Tuple
from tkinter import messagebox
from config import MAX_SCREEN_WIDTH, MAX_SCREEN_HEIGHT


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


def validate_meditation_key(key: str) -> bool:
    """
    Validate meditation key input
    
    Args:
        key: The key to validate
        
    Returns:
        True if valid, raises ValidationError otherwise
    """
    if not key:
        raise ValidationError("Debe ingresar un caracter para la Tecla de Meditación")
    
    if len(key) != 1:
        raise ValidationError("La tecla de meditación debe ser un único caracter")
    
    return True


def validate_position(x: str, y: str) -> Tuple[int, int]:
    """
    Validate position coordinates
    
    Args:
        x: X coordinate as string
        y: Y coordinate as string
        
    Returns:
        Tuple of (x, y) as integers
        
    Raises:
        ValidationError: If coordinates are invalid
    """
    try:
        pos_x = int(x)
        pos_y = int(y)
    except ValueError:
        raise ValidationError("Las posiciones deben ser numéricas")
    
    if pos_x < 0 or pos_x > MAX_SCREEN_WIDTH:
        raise ValidationError(f"La posición en X debe ser un número entre 0 y {MAX_SCREEN_WIDTH}")
    
    if pos_y < 0 or pos_y > MAX_SCREEN_HEIGHT:
        raise ValidationError(f"La posición en Y debe ser un número entre 0 y {MAX_SCREEN_HEIGHT}")
    
    return pos_x, pos_y


def show_validation_error(error_message: str) -> None:
    """Show validation error in a message box"""
    messagebox.showerror("Error de Validación", error_message)


def validate_and_show_errors(meditation_key: str, pos_x: str, pos_y: str) -> Tuple[str, int, int]:
    """
    Validate all inputs and show errors if any
    
    Returns:
        Tuple of (meditation_key, pos_x, pos_y) as validated values
        
    Raises:
        ValidationError: If any validation fails
    """
    try:
        validate_meditation_key(meditation_key)
        validated_x, validated_y = validate_position(pos_x, pos_y)
        return meditation_key, validated_x, validated_y
    except ValidationError as e:
        show_validation_error(str(e))
        raise
