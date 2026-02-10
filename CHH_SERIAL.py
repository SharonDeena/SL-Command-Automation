import serial
import time


# Configure the serial connection
ser = serial.Serial(
    port='COM12',      # Update with your port
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
#FUNCTION CONTROL

("Input number or symbol for channel select","AA 09 C9 31 31 2E 31 BF FA"),
("Input Volume set to 100","AA 06 CD 64 F8 97"),
("Input Volume set to 80","AA 06 CD 50 8E 40"),
("Input Volume set to 50","AA 06 CD 32 C2 A4"),
("Aging ON","AA 06 C2 01 D4 AA"),
("Aging OFF","AA 06 C2 00 C4 8B"),
("Mute ON","AA 06 C3 00 F7 BA"),
("Mute OFF","AA 06 C3 01 E7 9B"),
("Connect WIFI (changhong-roku)","AA 06 C5 00 5D 1C"),
("Check wifi connection success or fail	","AA 06 C5 01 4D 3D"),
("Turn off wifi","AA 06 C5 02 7D 5E"),
("Connect LAN","AA 06 C6 00 08 4F"),
("Check LAN connection success or fail","AA 06 C6 01 18 6E"),
("Select CHANGHONG factory channel list","AA 06 C7 00 3B 7E"),
("Import channel list from U disk","AA 06 C7 05 6B DB"),
("Switch source to HDMI1","AA 06 C8 00 2B 40"),
("Switch source to HDMI2","AA 06 C8 01 3B 61"),
("Switch source to HDMI3","AA 06 C8 02 0B 02"),
("Switch source to HDMI4","AA 06 C8 03 1B 23"),
("switch source to AV","AA 06 C8 04 6B C4"),
("Switch source to Tuner","AA 06 C8 05 7B E5"),
("Switch source to DTV","AA 06 C8 06 4B 86"),
("Switch source to ATV","AA 06 C8 07 5B A7"),
("CH+","AA 06 CA 00 4D 22"),
("CH-","AA 06 CA 01 5D 03"),
("VOL+","AA 06 CB 00 7E 13"),
("VOL-","AA 06 CB 01 6E 32"),
("Check USB1 Port connection","AA 06 CC 00 E7 84"),
("Check USB2 Port connection","AA 06 CC 01 F7 A5"),
("Show factory menu","AA 06 CF 00 B2 D7"),
("Close factory menu","AA 06 CF 01 A2 F6"),
("Enter keypad test menu","AA 06 D8 00 28 33"),
("Exit keypad test menu","AA 06 D8 01 38 12"),
("Function Exit","AA 05 DA 23 03"),
("Audio banlance Left","AA 06 DE 00 82 95"),
("Audio banlance right","AA 06 DE 01 92 B4"),
("Audio banlance","AA 06 DE 02 A2 D7"),
("Guide right","AA 06 DF 01 A1 85"),
("Guide up","AA 06 DF 02 91 E6"),
("Guide down","AA 06 DF 03 81 C7"),
("OK&Enter","AA 06 DF 04 F1 20"),
("Write data from configuration file(.json file)","AA 05 F0 A6 2B"),
("Enter Port Status Menu","AA 06 F4 00 6B B8"),
("Exit Port Status Menu","AA 06 F4 01 7B 99"),
("Check Bluetooth success or fail","AA 06 F8 00 2E D5"),
("Read Normal Gamma","AA 05 D7 F2 AE"),
("Read Warm Gamma","AA 05 D9 13 60"),
("Read Cool Gamma","AA 05 DB 33 22"),
("Read hdcp14","AA 05 E6 D4 DC"),
("Read hdcp22(receiver ID)","AA 05 E7 C4 FD"),
("Read LAN MAC","AA 05 BE 0F 21"),
("Read ESN","AA 05 DD 53 E4"),
("Read BT MAC","AA 06 DC 01 F4 D6"),
("Read Wired IP","AA 06 F5 00 58 89"),
("Read Wireless IP","AA 06 F5 01 48 A8"),
("Read SW version","AA 06 F6 00 0D DA"),
("Read Project ID","AA 06 F6 01 1D FB"), 
("Read OEM SN","AA 05 A9 6D F7"),
("Read Device ID","AA 05 AD 2D 73"),
("Set HDCP key","AAFE0268E5786F626B0500000033000000200200000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000045232C41C6F67EF7924FF18BAD70ADD65E1BE5275ED9E420091972B2C027B3A5556451A11F04190F5B9B571D1868EE23F386748C4CFAE9D609E943A0B5BEC5F20CBF446EF310B812E7E370673CE48877155911BABCFCE061C2900F8C4E3BEC870DA7ECD985608046C30D9F7D88B03FD03434F9F4BF3A412C5494B506A52A2C19202F22ECC3B7F8D984100B2644B940399B7D232C74C4990746BBE340DA91DD49DA37C3CC29A3927EDF983C86952E0C8CE9F0809CF2DABCB0"),

#WHITE BALANCE

("Serial Communication Test","36 96 00 00 00 00 CC"),
("Enter WB tuning mode(Norma picturebacklight MAX) and source(HDMI2)","AA 06 D0 00 A1 9A"),
("Set Color temp=Warm","36 96 82 00 00 03 51"),
("Set Color temp=Standard","36 96 82 00 00 02 4F"),
("Set Color temp=Cool","36 96 82 00 00 02 50"),
("Set R gain","36 96 89 00 00 7F D4"),
("Set G gain","36 96 8A 00 00 7F D5"),
("Set B gain","36 96 8B 00 00 7F D6"),
("Save RGB gain to Warm","36 96 90 08 00 00 64"),
("Save RGB gain to Standard","36 96 8F 08 00 00 63"),
("Save RGB gain to Cool","36 96 91 08 00 00 65"),

#GAMMA		

("Serial Communication Test","36 96 00 00 00 00 CC"),
("Enter WB tuning mode(Norma picture,backlight MAX) and source(HDMI2)","AA 06 D0 01 B1 BB"),
("Set Pattern","AA 08 C1 C0 C0 C0 47 E8"),
("Close Pattern","AA 05 C0 90 78"),
("Write Warm Gamma","AA FE 06 07 D2"),
("Write Normal Gamma","AA FE 06 07 D1"),
("Write Cool Gamma","AA FE 06 07 D3"),
("Apply Gamma Data","AA 05 D4 C2 CD"),
("Show PASSED info","AA 06 D5 01 4E 4E"),
("Show FAIL info","AA 06 D5 00 5E 6F"),

#FACTORY RESET

("Factory Reset","AA 05 C4 D0 FC")

]

# Send each command with required timing
for i, item in enumerate(commands):
    name, cmd = item   # unpack tuple

    print(f"Switched to: {name}")
    send_hex_command(cmd)

    # if i == 3:
        # time.sleep(10)
    # else:
        # time.sleep(2)

    read_response()



# Close the serial connection
ser.close()
print("Serial connection closed.")
