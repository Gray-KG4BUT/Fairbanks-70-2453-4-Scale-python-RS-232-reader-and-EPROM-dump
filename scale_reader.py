import serial
import time
import msvcrt
import re
from datetime import datetime

# Your legacy byte mappings
byte_map = {
    0xB0: 48,   # '0'
    0xB1: 49,   # '1'
    0xB2: 50,   # '2'
    0xB3: 51,   # '3'
    0xB5: 53,   # '5'
    0xB6: 54,   # '6'
    0xB9: 57,   # '9'
    0xAE: 46,   # '.'
    0xC7: 32,   # Clear 'N'
    0x52: 32,   # Clear 'R'
    0xEC: 108,  # 'l'
    0x62: 98,   # 'b'
    0x8A: 32,   # Clear '\x8a'
    0x04: 32,   # Clear '\x04'
    0xA0: 32    # Clear non-breaking space
}

def translate_data(raw_bytes):
    """Translates bytes based on your provided legacy map."""
    translated = bytearray()
    for b in raw_bytes:
        mapped_val = byte_map.get(b, b)
        translated.append(mapped_val)
    return translated.decode('utf-8', errors='replace')

# Initialize serial BEFORE the loop to avoid NameError
try:
    ser = serial.Serial('COM1', 9600, timeout=2)
    print("Port opened. Press 'Enter' to read the scale (or 'q' to quit)...")
    
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b'\r':
                ser.reset_input_buffer()
                ser.write(b'\r\n')
                time.sleep(0.5)
                
                if ser.in_waiting > 0:
                    raw_line = ser.read(ser.in_waiting)
                    
                    # DEBUG: Print this to see the hex values for negative signs
                    # print(f"\nDEBUG: Raw bytes: {raw_line.hex()}")
                    
                    decoded_text = translate_data(raw_line)
                    
                    # Regex handles optional negative sign and units
                    match = re.search(r"(-?\d+\.?\d*)\s*(lb|kg|kilo|pounds|kilos)", decoded_text, re.IGNORECASE)
                    
                    if match:
                        clean_value = f"{match.group(1)} {match.group(2)}"
                    else:
                        match_num = re.search(r"(-?\d+\.?\d*)", decoded_text)
                        clean_value = match_num.group(1) if match_num else "0.0"
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"[{timestamp}] Reading: {clean_value}")
                else:
                    print("DEBUG: No data received.")
            
            elif key == b'q':
                break

    ser.close()
    print("Port closed.")

except Exception as e:
    print(f"CRASHED: {e}")
    input("Press Enter to close...")