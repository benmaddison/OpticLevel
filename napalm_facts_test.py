#!/usr/bin/env python
import getpass
import napalm_base

def main():
  host = raw_input("Hostname: ")
  user = raw_input("Username: ")
  pwd = getpass.getpass()
  vendor = "ios"
  driver = napalm_base.get_network_driver(vendor)
#  with driver(hostname=host, username=user, password=pwd) as device:
#    facts = device.get_facts()
  device = driver(hostname=host, username=user, password=pwd)
  device.open()
  facts = device.get_facts()
  device.close()
  print("vendor: %s" % facts['vendor'])
  print("operating system: %s" % facts['os_version'])
  return

if __name__ == "__main__":
  main()

