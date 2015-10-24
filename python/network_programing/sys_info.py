#!/usr/bin/env python
# A system information script

import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print "\n"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])
subprocess.call([uname, uname_arg])

#commnad 2
diskspace = "df"
diskspace_arg = "-h"
print "\n"
print "Gathering diskspace information %s commnad:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])

#command 3
ip_address = "ifconfig"
ip_address_arg = "-a"
print "\n"
print "Gathering ip information %s command:\n" % ip_address
subprocess.call([ip_address, ip_address_arg])

