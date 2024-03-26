from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
import os

# Define the path to your inventory
inventory_path = './hosts.yml'

# Create a DataLoader object
loader = DataLoader()

# Create an InventoryManager object
inventory = InventoryManager(loader=loader, sources=[inventory_path])

# Print host names, IP addresses, and group names
for host in inventory.get_hosts():
    print(f"Host name: {host.name}")
    print(f"IP address: {host.vars['ansible_host']}")
    print(f"Group names: {', '.join([group.name for group in host.groups])}")

# Ping all hosts
os.system('ansible all:localhost -m ping') 

