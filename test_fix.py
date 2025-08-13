#!/usr/bin/env python3
"""
Test script to verify the keyboard handling fixes
"""
from pynput import keyboard

# Test the key combinations
INTERACT_KEYS = [
    { keyboard.KeyCode(char='x'), keyboard.KeyCode(char='c')}
]
CLOSE_KEYS = [
    {keyboard.KeyCode(char='x'), keyboard.KeyCode(char='b')}
]

print("Testing key combinations...")
print("INTERACT_KEYS:", INTERACT_KEYS)
print("CLOSE_KEYS:", CLOSE_KEYS)

# Test key matching
test_key_x = keyboard.KeyCode(char='x')
test_key_c = keyboard.KeyCode(char='c')
test_key_b = keyboard.KeyCode(char='b')

print(f"test_key_x in INTERACT_KEYS[0]: {test_key_x in INTERACT_KEYS[0]}")
print(f"test_key_c in INTERACT_KEYS[0]: {test_key_c in INTERACT_KEYS[0]}")
print(f"test_key_b in CLOSE_KEYS[0]: {test_key_b in CLOSE_KEYS[0]}")

# Test the logic
current_keys = set()
current_keys.add(test_key_x)
current_keys.add(test_key_c)

print(f"current_keys: {current_keys}")
print(f"All keys in INTERACT_KEYS[0]: {all(k in current_keys for k in INTERACT_KEYS[0])}")

print("Test completed successfully!")
