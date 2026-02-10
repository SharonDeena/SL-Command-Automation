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
#KTC SL Commands
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

# Gamma debugging preparation
("Enter the factory","AC 00 08 10 00 00 00 3B"),
("Reading barcodes","AC 00 08 10 00 01 00 3A"),
("White balance initialization","AC 00 08 10 00 02 00 39"),
("Turn off localdimming","AC 00 08 10 00 03 00 38"),
("Turn on localdimming","AC 00 08 10 00 03 01 37"),
("Open the built-in pattern","AC 00 08 10 00 04 00 37"),
("Switch to standard color temperature","AC 00 08 10 00 05 00 36"),
("Switch to cool color temperature","AC 00 08 10 00 05 01 35"),
("Switch to warmer color temperature","AC 00 08 10 00 05 02 34"),
("gamma initialization","AC 00 08 10 00 06 00 35"),
("Write the linear gamma array of standard color temperature to the TV end via serial port","AC 00 08 10 02 01 FF 39"),

# Switch 13 patterns to get xyY

("Built-in pattern grayscale selection","AC 00 0A 10 01 01 1A 1A 1A E9"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 33 33 33 9E"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 4D 4D 4D 50"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 66 66 66 05"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 80 80 80 B7"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 99 99 99 6C"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 B3 B3 B3 1E"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 CC CC CC D3"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 E6 E6 E6 85"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 FF FF FF 3A"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 00 FF 00 38"),
("Write gamma array to TV via serial port","AC06071002000000000100030004000600070009000A000C000D000F0010001200130015001600180019001B001C001E001F002100220024002500260028002A002C002E00300032003400360039003B003E004100440047004A004E005100550059005D0069007F0082008400870089008C008F009200950098009A009E00A200A900AF00B600BD00C200C800CD00D200D800DE00E200E600EB00EF00F400F800FD01010106010B01100115011B01200126012C01330139013F01440149014D01520157015C01610165016A016E01730178017D01810186018B01900196019B01A001A501AA01AF01B401B901BE01C301C701CC01D001D501DA01DE01E201E601EA01EE01F201F701FB01FF02030208020D02110216021B021F02240228022C023002340239023D02420246024B024F02540259025E02620266026A026F02730277027C028002850289028E02930298029C02A102A602AC02B102B602BB02C002C502CA02CE02D302D802DD02E202E602EB02F002F502F902FE03030308030C03110316031A031F03230327032B032F03330337033B033F03440348034C035103550359035E036203650369036D037003740378037B037F03830387038B038F03930397039A039E03A203A503A803AC03AF03B203B503B903BC03BF03C303C603C903CC03CF03D203D503D803DB03DF03E103E403E703EA03ED03F003F303F603F903FC03FF0000000100030004000600070009000A000C000D000F0010001200130015001600180019001B001C001E001F002100220024002500260028002A002C002E00300032003400360039003B003E004100440047004A004E005100550059005D0069007F0082008400870089008C008F009200950098009A009E00A200A900AF00B600BD00C200C800CD00D200D800DE00E200E600EB00EF00F400F800FD01010106010B01100115011B01200126012C01330139013F01440149014D01520157015C01610165016A016E01730178017D01810186018B01900196019B01A001A501AA01AF01B401B901BE01C301C701CC01D001D501DA01DE01E201E601EA01EE01F201F701FB01FF02030208020D02110216021B021F02240228022C023002340239023D02420246024B024F02540259025E02620266026A026F02730277027C028002850289028E02930298029C02A102A602AC02B102B602BB02C002C502CA02CE02D302D802DD02E202E602EB02F002F502F902FE03030308030C03110316031A031F03230327032B032F03330337033B033F03440348034C035103550359035E036203650369036D037003740378037B037F03830387038B038F03930397039A039E03A203A503A803AC03AF03B203B503B903BC03BF03C303C603C903CC03CF03D203D503D803DB03DF03E103E403E703EA03ED03F003F303F603F903FC03FF0000000100030004000600070009000A000C000D000F0010001200130015001600180019001B001C001E001F002100220024002500260028002A002C002E00300032003400360039003B003E004100440047004A004E005100550059005D0069007F0082008400870089008C008F009200950098009A009E00A200A900AF00B600BD00C200C800CD00D200D800DE00E200E600EB00EF00F400F800FD01010106010B01100115011B01200126012C01330139013F01440149014D01520157015C01610165016A016E01730178017D01810186018B01900196019B01A001A501AA01AF01B401B901BE01C301C701CC01D001D501DA01DE01E201E601EA01EE01F201F701FB01FF02030208020D02110216021B021F02240228022C023002340239023D02420246024B024F02540259025E02620266026A026F02730277027C028002850289028E02930298029C02A102A602AC02B102B602BB02C002C502CA02CE02D302D802DD02E202E602EB02F002F502F902FE03030308030C03110316031A031F03230327032B032F03330337033B033F03440348034C035103550359035E036203650369036D037003740378037B037F03830387038B038F03930397039A039E03A203A503A803AC03AF03B203B503B903BC03BF03C303C603C903CC03CF03D203D503D803DB03DF03E103E403E703EA03ED03F003F303F603F903FC03FFC2"),

#After the gamma file takes effect, check whether the gamma data meets the requirements	

("Built-in pattern grayscale selection","AC 00 0A 10 01 01 FF FF FF 3A"),
("Built-in pattern grayscale selection","AC 00 08 10 03 01 00 37"),
("Built-in pattern grayscale selection","AC 00 0A 10 01 01 99 99 99 6C"),
("Built-in pattern grayscale selection…3","AC 00 0A 10 01 01 66 66 66 05"),
("Built-in pattern grayscale selection…3","AC 00 0A 10 01 01 4D 4D 4D 50"),
("Disable built-in pattern","AC 00 08 10 03 05 00 33"),
("Athers send debug OK","AC 00 08 10 04 00 00 37"),
("Get the Autogamma flag","AC 00 08 10 05 00 01 35"),
("Athers sends debug NG","AC 00 08 10 04 01 00 36"),
("Copy rgb to all sources","AC 00 08 10 05 00 00 36"),

#Factory Reset

("Factory Reset","AC 00 08 04 04 01 00 42")

]

# Send each command with required timing
for i, item in enumerate(commands):
    name, cmd = item   # unpack tuple

    print(f"Switched to: {name}")
    send_hex_command(cmd)

    if i == 3:
        time.sleep(10)
    elif i == 7:
        time.sleep(21)
    elif i == 68:
        time.sleep(4)
    else:
        time.sleep(2)

    read_response()


# Close the serial connection
ser.close()
print("Serial connection closed.")