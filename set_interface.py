from netmiko import ConnectHandler
import os

iprouter = input('Router IP :' )
device = {
    'device_type': 'cisco_ios',
    'ip': iprouter,        
    'username': os.environ.get('ROUTER_USERNAME', 'amine'),
    'password': os.environ.get('ROUTER_PASSWORD', 'amine123'),
    'secret': os.environ.get('ROUTER_SECRET', 'amine123'),
}

# Connect to the device
net_connect = ConnectHandler(**device)
net_connect.enable()

interface= input('Interface à configurer: ')
description= input('description : ' )
description_conf= 'description' +' '+ description
network = input(' Network : ')
Masque = input(' Masque: ')
network_conf= 'ip add' +' '+ network +' '+ Masque
interface_conf= 'interface' +' ' + interface
interface_config = [
    interface_conf,   
    description_conf,
    network_conf,
    'no shutdown',
    'exit',
]

output = net_connect.send_config_set(interface_config)
print(output)

# Disconnect from the device
net_connect.disconnect()
