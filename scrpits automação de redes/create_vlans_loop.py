import getpass
import sys
import telnetlib

host = "10.10.100.2"
user =  raw_input("Entre com o seu username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(host)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
for v in range (2,150):
        tn.write("VLAN " + str(v) +"\n")
        tn.write("name Python_VLAN_"+ str(v) +"\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
