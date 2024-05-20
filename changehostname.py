from netmiko import ConnectHandler
import os

iprouter= input('Router IP : ')
hostname= input('nouveau Nom :')
device = {
    'device_type': 'cisco_ios',
    'host': iprouter ,
    'username': os.environ.get('ROUTER_USERNAME', 'amine'),
    'password': os.environ.get('ROUTER_PASSWORD', 'amine123'),
    'secret': os.environ.get('ROUTER_SECRET', 'amine123'),
}
net_connect = ConnectHandler(**device)
net_connect.enable()

nouveau_nom_hote = hostname

net_connect.config_mode()

output = net_connect.send_config_set(['hostname ' + nouveau_nom_hote])

net_connect.exit_config_mode()

output += net_connect.save_config()

print(output)

net_connect.disconnect()
print('Router \"' + hostname + '\" configured')
print('-'*79)

input("Press ENTER to finish")
