import bluetooth

target_name = "Galaxy A8 (2018)"
target_address = None

nearby_devices = bluetooth.discover_devices(lookup_names = True)

for bdaddr in nearby_devices:
	if target_name == bluetooth.lookup_name(bdaddr):
		target_address = bdaddr
		break

if target_address is not None:
	print("found target bluetooth device with address", target_address)
else:
	print("could not find target bluetooth device nearby")
