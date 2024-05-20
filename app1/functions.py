from netmiko import ConnectHandler
import paramiko
import os
import time


ROUTER_USERNAME = os.environ.get("ROUTER_USERNAME", "amine")
ROUTER_PASSWORD = os.environ.get("ROUTER_PASSWORD", "amine123")
ROUTER_SECRET = os.environ.get("ROUTER_SECRET", ROUTER_PASSWORD)


def get_cisco_device(host):
    return {
        "device_type": "cisco_ios",
        "host": host,
        "username": ROUTER_USERNAME,
        "password": ROUTER_PASSWORD,
        "secret": ROUTER_SECRET,
    }


def get_router_name(connection):
    hostname = connection.send_command("show run | i host")
    parts = hostname.split()
    return parts[1] if len(parts) > 1 else "unknown"

def HostnameFunc(router_p,verification):
    try:
        router = router_p
        
        # Create an ssh connection and set terminal length 0
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(router, username=ROUTER_USERNAME, password=ROUTER_PASSWORD)
        router_conn = conn.invoke_shell()
        
        print('Successfully connected to %s' % router)

        if verification == 'configuration':
            router_conn.send('show running-config\n')

        elif verification == 'route':
            router_conn.send('show ip route\n')

        elif verification == 'interfaces':
            router_conn.send('show ip interface brief\n')

        elif verification == 'vrf':
            router_conn.send('show ip vrf\n')

        elif verification == 'protocols':
            router_conn.send('show ip protocols\n')

        # Read the output, decode into UTF-8 (ASCII) text, and print
        return router_conn.recv(5000).decode("utf-8")
    
    except Exception as e:
        return f'An error occurred {e}'

def get_results(hostname):
    try:
        # Créer un objet SSHClient
        ssh_client = paramiko.SSHClient()

        # Ignorer les clés SSH inconnues
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Se connecter au périphérique
        ssh_client.connect(
            hostname,
            username=ROUTER_USERNAME,
            password=ROUTER_PASSWORD,
            timeout=10,
        )

        # Créer un canal SSH
        ssh_channel = ssh_client.invoke_shell()

        # Attendre que le périphérique soit prêt
        time.sleep(1)

        # Envoyer la commande "show ip route"
        ssh_channel.send("show ip route\n")

        # Attendre un certain temps pour que la sortie soit générée
        time.sleep(2)

        # Lire la sortie
        output = ssh_channel.recv(65535).decode("utf-8")

        # Fermer la connexion SSH
        ssh_client.close()

        return output
    except Exception as e:
        return str(e)

def eigrpFunc(hostip,eigrpprocid,network_i):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    #eigrpprocid = input('EIGRP Process ID #: ')
    routereigrp = 'router eigrp ' + eigrpprocid
    config_commands = [routereigrp]
    output = myssh.send_config_set(config_commands)
    print(output)
    #network_i = input('Please specify the network and mask to enable[10.1.0.0]: ')
    network_e = 'network ' + network_i
    config_commands = [routereigrp,network_e]
    output = myssh.send_config_set(config_commands)
    print(output)
    return('Router \"' + router_name + '\" configured')

def ospfFunc(hostip,ospfprocid,network_i,area_id):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    #ospfprocid = input('OSPF Process ID #: ')
    routerospf = 'router ospf ' + ospfprocid
    config_commands = [routerospf]
    output = myssh.send_config_set(config_commands)
    print(output)
    #network_i = input('Please specify the network and mask to enable[10.1.0.0 0.0.255.255]: ')
    #area_id = input('Enter the area to assign this network to: ')
    network_e = 'network ' + network_i + ' area ' + area_id
    config_commands = [routerospf,network_e]
    output = myssh.send_config_set(config_commands)
    print(output)
    return('Router \"' + router_name + '\" configured')

def changehostnameFunc(iprouter,hostname):
    device = get_cisco_device(iprouter)
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    nouveau_nom_hote = hostname
    net_connect.config_mode()
    output = net_connect.send_config_set(['hostname ' + nouveau_nom_hote])
    net_connect.exit_config_mode()
    output += net_connect.save_config()
    print(output)
    net_connect.disconnect()
    return('Router \"' + hostname + '\" configured')

def set_interfaceFunc(iprouter,interface,description,network,Masque):
    device = get_cisco_device(iprouter)
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    #interface= input('Interface à configurer: ')
    #description= input('description : ' )
    description_conf= 'description' +' '+ description
    #network = input(' Network : ')
    #Masque = input(' Masque: ')
    network_conf= 'ip add' +' '+ network +' '+ Masque
    interface_conf= 'interface' +' ' + interface
    interface_config = [interface_conf,description_conf,network_conf,'no shutdown','exit']
    output = net_connect.send_config_set(interface_config)
    # Disconnect from the device
    net_connect.disconnect()
    return output


def rip_Func(hostip,network_i):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)

    routerrip = 'router rip '
    network_e = 'network ' + network_i
    config_commands = [routerrip,
                            network_e]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + router_name + '\" configured'

def vrfcreate(hostip,vrf_id,rd_id,rt_id,interface,ip_int,masque):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    vrf = "ip vrf" + " " + vrf_id
    rd = "rd " +" "+ rd_id +':'+ rt_id
    rt = "route-target"+" "+"both"+" "+ rd_id + ":" + rt_id
    inte="int"+" "+interface
    int_f="ip vrf forwarding"+" "+vrf_id
    ip_add="ip add"+" "+ip_int+" "+masque
    config_commands = [vrf, rd, rt, inte, int_f, ip_add
                        ]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + router_name + '\" configured'

def clientrip(hostip,vrf,network_i):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    routerrip = 'router rip '
    add_f= 'address-family ipv4 vrf'+' '+vrf
    network_e = 'network ' + network_i
    r_b='router bgp 1'
    add_f= 'address-family ipv4 vrf'+' '+vrf
    red='redistribute rip'
    r_o= 'router rip'
    add_f= 'address-family ipv4 vrf'+' '+vrf
    red2='redistribute bgp 1 metr trans'
    config_commands = [routerrip,
                            add_f, network_e, r_b, add_f, red, r_o, red2]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + router_name + '\" configured'

def clientospf(hostip,vrf,ospfprocid,network_i,area_id):
    device = get_cisco_device(hostip)

    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    routerospf = 'router ospf ' + ospfprocid+" "+"vrf"+" "+vrf
    config_commands = [routerospf
                        ]

    network_e = 'network ' + network_i + ' area ' + area_id
    r_b='router bgp 1'
    add_f= 'address-family ipv4 vrf'+' '+vrf
    red='redistribute ospf'+' '+ospfprocid+' vrf '+vrf
    r_o= 'router ospf '+ospfprocid+' vrf '+vrf
    red2='redistribute bgp 1 subnets'
    config_commands = [routerospf,
                            network_e, r_b, add_f, red, r_o, red2]
    output = myssh.send_config_set(config_commands)
    return output + 'Router \"' + router_name + '\" configured'

def clienteigrp(hostip,vrf,eigrpprocid):
    #hostip = input('Router IP: ')
    device = get_cisco_device(hostip)

    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    #vrf=input("donner le nom de vrf:")
    #eigrpprocid = input('EIGRP ID: ')
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
    return  output+ 'Router \"' + router_name + '\" configured'

def supp_routage(hostip,p):
    device = get_cisco_device(hostip)

    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    sup_p = 'no router ' + p
    config_commands = [sup_p]
    output = myssh.send_config_set(config_commands)
    return 'Router \"' + router_name + '\" configured'


def supp_vrf(hostip,vrf):
    device = get_cisco_device(hostip)
    myssh = ConnectHandler(**device)
    router_name = get_router_name(myssh)
    sup_vrf = 'no ip vrf ' + vrf
    config_commands = [sup_vrf]
    output = myssh.send_config_set(config_commands)
    return 'Router \"' + router_name + '\" configured'




