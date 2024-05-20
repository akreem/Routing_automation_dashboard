from netmiko import ConnectHandler
import os

hostip = input('Router IP: ')
device = {
    'device_type': 'cisco_ios',
    'host': hostip,
    'username': os.environ.get('ROUTER_USERNAME', 'amine'),
    'password': os.environ.get('ROUTER_PASSWORD', 'amine123'),
    'secret': os.environ.get('ROUTER_SECRET', 'amine123'),
}

myssh = ConnectHandler(**device)
hostname = myssh.send_command('show run | i host')
x = hostname.split()
device = x[1]
vrf=input("donner le nom de vrf:")
eigrpprocid = input('EIGRP ID: ')
routereigrp = 'router eigrp ' + eigrpprocid
r_b='router bgp 1'
add_f= 'address-family ipv4 vrf'+' '+vrf
red='redistribute eigrp'+' '+eigrpprocid
r_e= 'router eigrp '+eigrpprocid
dd_f= 'address-family ipv4 vrf'+' '+vrf
red2='redistribute bgp 1  metric 1 1 1 1 1'
config_commands = [routereigrp,
                            r_b, add_f, red, r_e,dd_f, red2]
output = myssh.send_config_set(config_commands)
print(output)
   
print('Router \"' + device + '\" configured')
print('-'*79)

input("Press ENTER to finish")
