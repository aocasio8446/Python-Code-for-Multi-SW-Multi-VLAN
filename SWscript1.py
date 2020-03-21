#!/usr/bin/python

import getpass
import sys
import telnetlib


user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

for n in range(17, 22):
    HOST = "192.168.255." + str(n)

    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    # tn.write("en\n")
    # tn.write("smu\n")

    tn.write("config t\n")
    # tn.write("vtp mode transparent")

    for n in range(2, 3):
        tn.write("vlan " + str(n) + "\n")
        tn.write("name Python_vlan_" + str(n) + "\n")

    tn.write("end\n")
    tn.write("show vlan brief\n")
    tn.write("wr\n")
    tn.write("exit\n")

    print(tn.read_all())
