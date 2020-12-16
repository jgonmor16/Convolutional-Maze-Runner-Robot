import bluetooth

print("Scaning for devices...")

devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)

num = len(devices)
print("Num of devices found: %d" % num)

for addr, name, device_class in devices:
    print("\nDevice:")
    print("Name: %s" % (name))
    print("MAC: %s" % (addr))
    print("Class: %s" % (device_class))
