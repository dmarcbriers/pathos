#!/usr/bin/env python
"""
start remote server for selected package
"""

from pathos_core import *


if __name__ == '__main__':
  ### ASSUME ALL PACKAGES ARE INSTALLED ###

##### CONFIGURATION & INPUT ########################
  # set the default remote host
 #rhost = 'localhost'
  rhost = 'upgrayedd.danse.us'
 #rhost = 'shc-b.cacr.caltech.edu'
 #rhost = 'login.cacr.caltech.edu'

  # set the default port
  rport = '98909'
  # set the default server command
  server = 'ppserver'  #XXX: "ppserver -p %s" % rport
 #server = 'classic_server'  #XXX: "classic_server -p %s" % rport
 #server = 'registry_server'  #XXX: "registry_server -p %s" % rport

  print """Usage: python start_server.py [server] [remoteport] [hostname] 
    [server] - name of the RPC server (assumed to be already installed)
    [remoteport] - remote port over which the server will communicate
    [hostname] - name of the host on which to run the server
    defaults are: "%s" "%s" "%s".""" % (server, rport, rhost)

  # get server to run from user
  import sys
  try:
    myinp = sys.argv[1]
  except: myinp = None
  if myinp:
    server = myinp #XXX: should test validity here... (filename)
  else: pass # use default
  del myinp

  # get remote port to run server on from user
  import sys
  try:
    myinp = sys.argv[2]
  except: myinp = None
  if myinp:
    rport = myinp #XXX: should test validity here... (filename)
  else: pass # use default
  del myinp

  # get remote hostname from user
  import sys
  try:
    myinp = sys.argv[3]
  except: myinp = None
  if myinp:
    rhost = myinp #XXX: should test rhost validity here... (how ?)
  else: pass # use default
  del myinp

  # my remote environment (should be auto-detected)
  from _known_hosts import get_profile
  profile = get_profile(rhost)

##### CONFIGURATION & INPUT ########################

  # run server
  serve(server,rhost,rport, profile=profile)

  # get server pid  #FIXME: launcher.pid is not pid(server)
  target = 'python[^#]*'+server #XXX: filter w/ regex for python-based server
  pid = getpid(target,rhost)

  # test server
  # XXX: add a simple one-liner...
  print "\nServer running at port=%s with pid=%s" % (rport,pid)
  import sys
  print 'Press <Enter> to kill server'
  sys.stdin.readline()

  # stop server
  print kill(pid,rhost)
# del rserver  #XXX: delete should run self.kill (?)


# EOF
