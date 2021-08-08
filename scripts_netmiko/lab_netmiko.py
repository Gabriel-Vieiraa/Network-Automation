from netmiko import  ConnectHandler

sw2 = {
        'device_type': 'cisco_ios',
        'ip': '10.10.100.4',
        'username': 'cisco',
        'password': 'cisco',
       }

net_connect = ConnectHandler(**sw2)
net_connect.find_prompt()

output = net_connect.send_command("show ip int brief")
print (output)

config_loopback = ['int loop 0','ip addr 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_loopback)
print (output)

for v in range(2,21):
        print 'Creating Vlan'+ str (v)
        config_vlans = ['vlan '+ str(v),'name VLAN PYTHON '+ str(v)]
        output = net_connect.send_config_set(config_vlans)
        print output
