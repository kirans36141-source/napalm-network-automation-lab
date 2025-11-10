from napalm import get_network_driver   # import NAPALM

# choose the driver for Cisco IOS devices
driver = get_network_driver("ios")

# define device credentials
device = driver(
    hostname="192.168.1.1",   # IP address of R1's G0/0
    username="admin",
    password="cisco123"
)

print("Connecting to R1...")
device.open()                 # establishes the SSH session
print("✅ Connected successfully!\n")

# get and display basic router information
facts = device.get_facts()
print("Device Facts:")
for key, value in facts.items():
    print(f"{key}: {value}")

device.close()
print("\nConnection closed.")
