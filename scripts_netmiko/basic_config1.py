interface ether 1/2
  switchport mode access
  switchport access vlan 10

interface ether 1/3
  switchport mode access
  switchport access vlan 10

vtp domain PYTHON
vtp mode transparent

username cciepython priv 15 password python