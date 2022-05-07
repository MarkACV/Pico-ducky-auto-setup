
import shutil
import time
import os
import pyfiglet



banner = pyfiglet.figlet_format("Pico ducky\nAuto setup")

print(banner)
input('Make sure your Pico ducky is plugged in and on setup mode (Enter)')

#add menu -add script -favourite scripts to txt

print("[+] Cleaning Pico ducky")
shutil.copy("files/flash_nuke.uf2","D:")
time.sleep(12)


print("[+] Loading CircuitPython")
shutil.copy("files/adafruit-circuitpython-raspberry_pi_pico-en_US-7.2.5.uf2","D:")
time.sleep(15)        

print("[+] Turning drive into HID")
try:
    os.mkdir("D:/lib/adafruit_hid")
except:
    pass

ada_dir = os.listdir("files/adafruit_hid")

for element in ada_dir:
    shutil.copy("files/adafruit_hid/"+element,"D:/lib/adafruit_hid")

print('[+] Payloads saved: ')

payloads = os.listdir('scripts')

for option in payloads:
    print(option)

payload = input("Payload to load: ")



shutil.copy("scripts/"+payload,"D:")
os.rename('D:/'+payload,'D:/payload.dd')

print("Make sure you disconnect it IMMEDIATELY afrer 'ready' message")
time.sleep(1)
print("Be prepared...")
time.sleep(3)

os.remove('D:code.py')
shutil.copy("files/duckyinpython.py","D:")
os.rename("D:/duckyinpython.py","D:/code.py")

print('[+] Ready')
