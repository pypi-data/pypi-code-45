#!python
'''Usage:
  aquael poweron IPADDRESS RBW
  aquael poweroff IPADDRESS
  aquael (-h | --help)
  aquael --version
'''
from docopt import docopt
import socket

OFF_COLOR = '000000000'

def __main():
  arguments = docopt(__doc__, version='0.0.1')
  ip = arguments['IPADDRESS']
  rbw = arguments['RBW']

  if arguments['poweron'] is True:
    poweron(ip, rbw)
  elif arguments['poweroff'] is True:
    poweroff(ip)

def poweron(ip, rbw):
  __set_color(ip, rbw)

def poweroff(ip):
  __set_color(ip, OFF_COLOR)

def __set_color(ip, rbw):
  UDP_IP = ip
  UDP_PORT = 2390
  MESSAGE = 'PWM_SET:' + rbw

  print('UDP target IP:', UDP_IP)
  print('UDP target port:', UDP_PORT)
  print('message:', MESSAGE)

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.bind(('0.0.0.0', 2390))
  sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

if __name__ == '__main__':
  __main()