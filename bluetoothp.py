from bluetooth import *
from pprint import pprint

target_name = 'Galaxy A8 (2018)'
target_address = None

while target_address is None:
	nearby_devices = discover_devices(lookup_names = True)
	print("%d devices found" % len(nearby_devices))
	for bdaddr, bname in nearby_devices:
		print(bdaddr, bname)
		if target_name == bname:
			target_address = bdaddr
			break

if target_address is not None:
	print("found target bluetooth device with address", target_address)
else:
	print("could not find target bluetooth device nearby")

port = 3
s = BluetoothSocket(RFCOMM)
s.connect((target_address, port))

s.send("Test")
s.close()