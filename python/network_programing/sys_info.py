#!/usr/bin/env python
# A system information script

import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])
subprocess.call([uname, uname_arg])

#commnad 2
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace information %s commnad:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])

