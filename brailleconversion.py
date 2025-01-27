import pynput.keyboard
import threading

# Mapping of keys to their respective Braille dots (bits 0-5)
key_to_dot = {
    'f': 0b00000001,  # Dot 1
    'd': 0b00000010,  # Dot 2
    's': 0b00000100,  # Dot 3
    'j': 0b00001000,  # Dot 4
    'k': 0b00010000,  # Dot 5
    'l': 0b00100000,  # Dot 6
}

# Global variables to track the current Braille code and timer
current_code = 0
timer = None
threshold = 0.1  # 100 milliseconds delay threshold
lock = threading.Lock()

def process_braille():
    """Process the accumulated Braille code and print the corresponding character."""
    global current_code, timer
    with lock:
        if current_code != 0:
            # Calculate the Unicode Braille character
            braille_char = chr(0x2800 + current_code)
            print(braille_char, end='', flush=True)
            current_code = 0  # Reset the code
        timer = None

def on_press(key):
    """Handle key press events, updating the current Braille code and managing the timer."""
    global current_code, timer
    try:
        # Convert the key to lowercase to handle case insensitivity
        char = key.char.lower()
    except AttributeError:
        # Ignore non-character keys
        return
    if char not in key_to_dot:
        return  # Skip irrelevant keys

    with lock:
        # Cancel the existing timer if it's active
        if timer is not None:
            timer.cancel()
        # Update the current Braille code with the new dot
        current_code |= key_to_dot[char]
        # Start a new timer to process the Braille code after the threshold delay
        timer = threading.Timer(threshold, process_braille)
        timer.start()

# Start listening for key presses
with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()