import getpass
import sys
import telnetlib

user =  raw_input("Entre com o seu username: ")
password = getpass.getpass()
file_switches = open("ip_switches")

for s in file_switches:
        print("Configurando Switch "+str(s)+ "\n")
        tn = telnetlib.Telnet(s)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")

        tn.write("conf t\n")

        for v in range (2,51):
                tn.write("no VLAN " + str(v) +"\n")
                tn.write("no name Python_VLAN_"+ str(v) +"\n")

        tn.write("end\n")
        tn.write("exit\n")

        print tn.read_all()
