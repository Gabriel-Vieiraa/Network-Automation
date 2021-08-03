import getpass
import sys
import telnetlib

host = "10.10.100.2"
host2 = "10.10.34.3"

user = raw_input("Entre com o seu username: ")
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
tn.write("int loo 1\n")
tn.write("end\n")

tn2 = telnetlib.Telnet(host2)

tn2.read_until("Username: ")
tn2.write(user + "\n")
if password:
        tn2.read_until("Password: ")
        tn2.write(password + "\n")

tn2.write("enable\n")
tn2.write("cisco\n")
tn2.write("conf t\n")
tn2.write("int loo 1\n")
tn2.write("end\n")
tn2.write("exit\n")
