import serial
import time


# Configure the serial connection
ser = serial.Serial(
    port='COM12',  # Update with your port
    baudrate=115200,
    timeout=1,
    bytesize=8,
    parity='N',
    stopbits=1
)

if ser.isOpen():
    print("Serial port open successfully.\n")

# Function to send a hex command
def send_hex_command(hex_command):
    byte_command = bytes.fromhex(hex_command.replace(" ", ""))  # remove spaces
    ser.write(byte_command)
    print(f"Sent: {hex_command}")

# Function to read the response
def read_response():
    time.sleep(2)  # small delay to allow response
    response = ser.read(ser.in_waiting)  # read available data
    if response:
        print("Received:")
        print(response.hex(), "\n")
    else:
        print("No response\n")

# List of commands to send
commands = [
    "FF 33 06 03 12 E5",
    "FF330703620094",
    "FF33060351A6",
    "FF3307035D0198",
    "FF 33 1F 03 5C 01 34 33 4A 31 55 41 54 43 2D 32 33 42 48 32 32 35 35 2D 30 30 30 30 35 51 15",
    "FF3307031608D8",
    "FF 33 07 03 16 09 D7",
    "FF 33 07 03 16 0A D6",
    "FF3306030CEB",
    "FF 33 0C 03 0B 1C 2F A2 30 34 B9 DC",
    "FF3307035A019B",
    "FF3307035A029A",
    "FF 33 07 03 17 64 7B",
    "FF 33 07 03 17 50 8F",
    "FF 33 07 03 17 20 BF",
    "FF3307031700DF",
    "FF3307031630B0",
    "FF3307031601DF",
    "FF3307031608D8",
    "FF 33 06 03 22 D5 00",
    "FF33060335C2",
    "FF 33 06 03 31 C6",
    "FF33060338BF",
    "FF33060320D7CD",
    "FF 33 07 03 45 01 B0",
    "FF33060314E3",
    "FF3307031601DF",
    "FF 33 07 03 16 04 DC",
    "FF 33 0B 03 61 00 4B 31 30 31 B4",
    "FF3306031DDA",
    "FF33070368642A",
    "FF 33 07 03 68 50 3E",
    "FF330603698E",
    "FF 33 06 03 33 C4",
    "FF 33 15 03 55 0F 73 65 74 4B 54 43 41 67 69 6E 67 3D 4F 4E 96",
    "FF 33 16 03 55 0F 73 65 74 4B 54 43 41 67 69 6E 67 3D 4F 46 46 57",
    "FF 33 0C 03 55 0F 72 65 73 65 74 6A"
]


# Send each command and read response
for cmd in commands:
    send_hex_command(cmd)
    time.sleep(2)  # wait for device to process command
    read_response()

# Close the serial connection
ser.close()
print("Serial connection closed.")
 