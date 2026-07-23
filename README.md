# Fairbanks-70-2453-4-Scale-python-RS-232-reader-and-EPROM-dump
Fairbanks 70-2453-4 Scale python RS-232 reader for windows 

#Configuration

By default, the script attempts to open `COM1` at `9600` baud. If your USB-to-Serial adapter or hardware is connected to a different port (e.g., `COM3`), open `scale_reader.py` and change the port string on this line:

ser = serial.Serial('COM #YOUR PORT', 9600, timeout=2)

#License
This project is completely free and unrestrictive. Use it, modify it, or share it however you like—no license required.
