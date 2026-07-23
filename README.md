# Fairbanks-70-2453-4-Scale-python-RS-232-reader-and-EPROM-dump
Fairbanks 70-2453-4 Scale python RS-232 reader for windows

NOTICE
this firmware is for educational purposes only and is a official dump from an EPROM

Configuration

By default, the script attempts to open `COM1` at `9600` baud. If your USB-to-Serial adapter or hardware is connected to a different port (e.g., `COM3`), open `scale_reader.py` and change the port string on this line:

ser = serial.Serial('COM #YOUR PORT', 9600, timeout=2)

Right-click the Start menu icon. Select Device Manager. Scroll down and double-click Ports (COM & LPT). Right-click your specific COM port (e.g., USB Serial Port COM3). Click Properties. and put in these settings: Data Bits: 7. Parity: Odd. Baud Rate: 9600. Stop Bits: 2.

License
This project is completely free and unrestrictive. Use it, modify it, or share it however you like—no license required.

you will need to install python, you can do that by going here: https://www.python.org/ftp/python/3.15.0/python-3.15.0b4-amd64.exe (x64) or https://www.python.org/ftp/python/3.15.0/python-3.15.0b4.exe (x86)

you will need to install pyserial you can do that by doing this in command prompt: python -m pip install pyserial

the 70-2453-40 use the MBM27C128-25 EPROM (Erasable Programmable Read-Only Memory) for the firmware and the 24C01A eeprom (Electrically Erasable Programmable Read-Only Memory) for calibration and user set preferences (I only have the dump of the firmware). it utilizes the M37451SFP microprocessor.
