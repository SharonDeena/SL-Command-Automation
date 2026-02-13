import serial
import time
import os
import pandas as pd  # type: ignore
from datetime import datetime 


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

test_results = []

# Function to send a hex command
def send_hex_command(hex_command):
    byte_command = bytes.fromhex(hex_command.replace(" ", ""))  # remove spaces
    ser.write(byte_command)
    print(f"Sent: {hex_command}")

# Function to read the response
def read_response():
    time.sleep(2)
    response = ser.read(ser.in_waiting)

    if response:
        hex_response = response.hex().upper()
        print(f"Received: {hex_response}\n")
        return hex_response
    else:
        print("No response\n")
        return "No Response"


# List of commands to send
commands = [
("HDMI1", "AC 00 08 01 03 00 00 47"),
("HDMI2","AC 00 08 01 03 01 00 46"),
("HDMI3","AC 00 08 01 03 02 00 45"),
("USB1","AC 00 08 01 05 00 00 45"),
("Get Eth MAC","AC 00 08 02 01 01 00 47"),
("Get BT MAC","AC 00 08 02 03 01 00 45"), 
("Get WiFi MAC","AC 00 08 02 02 01 00 46"),
("open ageing","AC 00 08 04 02 00 00 45"),
("close ageing","AC 00 08 04 02 01 00 44"),
("Mute On","AC 00 08 04 03 00 00 44"),
("Mute Off","AC 00 08 04 03 01 00 43"),
("Set Project ID","AC 00 09 02 0C 13 31 39 BF"), 
("Get Project ID","AC 00 08 02 0B 10 00 2E"),
("Read Model Name","AC 00 08 02 0C 14 00 29"), 
("Read SN of the Device","AC 00 08 02 07 00 00 42"),
("Blue Picture/Pattern","AC 00 08 04 00 03 00 44"),
("Red Picture/Pattern","AC 00 08 04 00 01 00 46"), 
("Green Picture/Pattern","AC 00 08 04 00 04 00 43"),
("Black Picture/Pattern","AC 00 08 04 00 02 00 45"),
("White Picture/Pattern","AC 00 08 04 00 00 00 47"),
("Close single color pattern","AC 00 08 04 00 05 00 42"),
("Get HDCP 1.4 & burning status","AC 00 08 0A 04 05 00 38"),
("Get HDCP 2.2 & burning status","AC 00 08 0A 04 06 00 37"),
("Open the WiFi","AC 00 08 04 01 00 00 46"), 
("One Click to connect the specified WIFI","AC 00 18 04 01 02 66 6F 72 74 69 6E 65 74 3F 66 6F 72 74 69 6E 65 74 1F"),
("Get Wifi network status","AC 00 08 04 01 01 00 45"), 
("Get WiFI RSSI information.","AC 00 08 04 01 03 00 43"),
("Disconnect WIFI","AC 00 08 04 01 06 00 40"),
("Close WIFI","AC 00 08 04 01 04 00 42"), 
("Check Network connection status(Ethernet)","AC 00 08 04 01 05 00 41"), 
("Turn ON BT","AC 00 08 04 01 16 00 30"), 
("Scan BT","AC 00 08 04 01 10 00 36"), 
("Get the number of  BT list","AC 00 08 04 01 15 00 31"), 
("Turn OFF BT","AC 00 08 04 01 14 00 32"), 
("Switch to DVB-T","AC 00 08 01 00 00 00 4A"),
("Switch to DVB-C","AC 00 08 01 00 01 00 49"),
("Switch to DVB-S","AC 00 08 01 00 02 00 48"),
("Switch to AIR-DTV","AC 00 08 01 00 03 00 47"),
("Switch to AIR-ATV","AC 00 08 01 00 04 00 46"),
("Switch to CABLE","AC 00 08 01 00 05 00 45"),
("witch to ATSC-TV Signal Source","AC 00 08 01 00 06 00 44"),
("Switch to ATV Signal Source","AC 00 08 01 00 07 00 43"),
("Switch to AV1 Signal Source","AC 00 08 01 01 00 00 49"),
("Switch to JP ISDB-T", "AC 00 08 01 00 08 00 42"),
("Switch to ISDB-BS","AC 00 08 01 00 09 00 41"),
("Switch to ISDB-CS","AC 00 08 01 00 0A 00 40"),
("Switch to ISDB-BS4K","AC 00 08 01 00 0B 00 3F"),
("Switch to ISDB-CSAK","AC 00 08 01 00 0C 00 3E"),
("Get the general version of motherboard software","AC 00 08 02 0C 15 00 28"), 
("Get SOC ID","AC 00 08 02 0C 11 00 2C"),
("Enter WB tuning mode","AB 07 10 01 00 00 3C"),
("Exit WB tuning mode","AB 07 10 00 00 00 3D"),
("Set R_Gain","AB 07 0C 80 80 80 C1"),
("Set G_Gain","AB 07 0C 78 78 78 D9"),
("Set B_Gain","AB 07 0C 60 65 67 15"),
("Output/return RGB Gain.","AB 07 0B 00 00 00 42"),
("Output RGB contolled 80 IRE white pattern","AB 07 0A 02 00 00 41"),
("Output RGB contolled 70 IRE white pattern","AB 07 0A 03 00 00 40"),
("Output RGB contolled 20 IRE white pattern","AB 07 0A 04 00 00 3F"),
("Switch to Cold Temp","AB 07 01 00 00 00 4C"), 
("Switch to Standard Temperature","AB 07 01 01 00 00 4B"), 
("Switch to Warm Temperature","AB 07 01 02 00 00 4A"), 
("The image switches to standard(Standard)","AB 07 02 00 00 00 4B"),
("The image switches to Bright(Vivid)","AB 07 02 01 00 00 4A"), 
("The image switches to Soft(Energysaving)","AB 07 02 02 00 00 49"), 
("Tuning results will be copied to all the Signal source.","AB 07 08 00 00 00 45"),
("Output internal White pattern(Max luminance","AB 07 0A 01 00 00 42"),
("Close internal White patten","AB 07 0A 00 00 00 43"), 
("Get ESN","AC 00 08 02 0B 05 00 39"),
("Front Panel Button Test (Enable)","AC 00 08 02 09 00 00 40"),
("Front Panel Button Test (Disable)","AC 00 08 02 09 02 00 3E"),
("Factory Reset","AC 00 08 04 04 01 00 42")
]


# Send each command with required timing
for i, item in enumerate(commands,start=1):
    name, cmd = item   # unpack tuple

    print(f"Switched to: {name}")
    send_hex_command(cmd)
    hex_response = read_response()

    status = "FAIL"

    if hex_response == "No Response":
        status = "FAIL"
    elif hex_response == "AC04004F":
        print("Result: PASS\n")
        status = "PASS"
    elif hex_response == "AC04014E":
        print("Result: FAIL\n")
        status = "FAIL"
    elif hex_response =="FC0017032300303032653038303531303030363666353A":
        print("SOC ID:39090210000162.00\n")
        print("Result: PASS\n")
        status = "FAIL"
    elif hex_response == "FC000D0301001C2FA2DCE0FB4E":
        print("Result: Eth MAC - 1C 2F A2 DC E0 FB\n")
        status = "PASS"
    elif hex_response == "FC000D030500E8519E2211776D":
        print("Result: BT MAC - E8 51 9E 22 11 77\n")
        status = "PASS"
    elif hex_response == "FC000D030400E8519E2211766F":
        print("Result: Wifi MAC - E8 51 9E 22 11 76\n")
        status = "PASS"
    elif hex_response == "AC04004F":
        print("Result: WiFi connected(pass)\n")
        status = "PASS"
    elif hex_response == "AC04014E":
        print("Result: WiFi port not open\n")
        status = "FAIL"
    elif hex_response == "AC04024D":
        print("Result: WiFi port is open but not connected\n")
        status = "FAIL"


    else: 
        if hex_response != "No Response":
            status = "PASS"

    if i == 3:
        time.sleep(25)
    elif i == 7:
        time.sleep(21)
    elif i == 68:
        time.sleep(4)
    else:
        time.sleep(2)


   # -------- STORE RESULT --------
    test_results.append({
        "S.NO": i,
        "FUNCTION": name,
        "SERIAL COMMAND": cmd,
        "RESPONSE RECEIVED": hex_response,
        "STATUS": status
    })


# Close the serial connection
ser.close()
print("Serial connection closed.")

# ---------------- GENERATE EXCEL REPORT ----------------
df = pd.DataFrame(test_results)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"KTC_Test_Report_{timestamp}.xlsx"
file_path = os.path.join(os.getcwd(), file_name)

df.to_excel(file_path, index=False)

print("Test Completed")
print("Excel Report Generated at:", file_path)

# ---------------- OPEN EXCEL FILE ----------------
os.startfile(file_path)
