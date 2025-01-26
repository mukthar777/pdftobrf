# from pynput import keyboard

# # Mapping of keys to Braille dots
# braille_mapping = {
#     'a': 0b100000,  # Dot 1
#     's': 0b010000,  # Dot 2
#     'd': 0b001000,  # Dot 3
#     'f': 0b000100,  # Dot 4
#     'j': 0b000010,  # Dot 5
#     'k': 0b000001   # Dot 6
# }

# # Function to convert binary representation to Unicode Braille character
# def binary_to_braille(binary):
#     return chr(0x2800 + binary)

# # Store currently pressed keys
# current_keys = set()

# def on_press(key):
#     try:
#         if key.char in braille_mapping:
#             current_keys.add(key.char)
#             # Calculate the combined braille representation
#             braille_value = sum(braille_mapping[k] for k in current_keys)
#             print("Current Braille:", binary_to_braille(braille_value))
#     except AttributeError:
#         pass

# def on_release(key):
#     try:
#         if key.char in braille_mapping:
#             current_keys.discard(key.char)
#     except AttributeError:
#         pass

# # Start listening for key events
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()


from pynput import keyboard

# Mapping of keys to Braille dots
braille_mapping = {
    'f': 0b000001,  # Dot 1
    'd': 0b000010,  # Dot 2
    's': 0b000100,  # Dot 3
    'j': 0b001000,  # Dot 4
    'k': 0b010000,  # Dot 5
    'l': 0b100000   # Dot 6
}

# Function to convert binary representation to Unicode Braille character
def binary_to_braille(binary):
    return chr(0x2800 + binary)

# Store currently pressed keys
current_keys = set()

def on_press(key):
    try:
        # Check if the pressed key corresponds to one of the Braille dots
        if hasattr(key, 'char') and key.char in braille_mapping:
            current_keys.add(key.char)
            # Calculate the combined Braille representation
            braille_value = sum(braille_mapping[k] for k in current_keys)
            # Print only the Braille dots as a Unicode character
            print(binary_to_braille(braille_value), end='', flush=True)
    except AttributeError:
        pass

def on_release(key):
    try:
        # Remove the key from the pressed keys set when released
        if hasattr(key, 'char') and key.char in braille_mapping:
            current_keys.discard(key.char)
    except AttributeError:
        pass

# Start listening for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
