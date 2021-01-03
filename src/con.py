#!/usr/bin/python3

import datetime
import socket
import sys
import time

import bluetooth

COMMAND_START_CHAR = '<'
COMMAND_END_CHAR = '>'
LOGFILE = 'bt.log'


def SearchForFullCommand(buffer):
  """Puts fully formed commands from buffer into a list, returning the remaining buffer.

  We expect commands to be demarcated by COMMAND_START_CHAR and COMMAND_END_CHAR.  The
  buffer may have zero or more such commands. This function finds all demarcated commands,
  strips off those demarcations, and returns the remaining buffer.  Any text that arrives
  before a COMMAND_START_CHAR is discarded.

  Args:
    buffer: string representing the text received so far.

  Returns:
    A 2-tuple, where the first element is the remaining buffer, and the second element
    is a potentially empty list of identified commands.
  """
  commands = []
  while COMMAND_END_CHAR in buffer:
    end_pos = buffer.find(COMMAND_END_CHAR)
    if COMMAND_START_CHAR in buffer[:end_pos]:
      start_pos = buffer.find(COMMAND_START_CHAR) + len(COMMAND_START_CHAR)
      commands.append(buffer[start_pos:end_pos])
    buffer = buffer[end_pos+len(COMMAND_END_CHAR):]
  return (buffer, commands)  # no command found


def Log(s):
  """Appends message s to the logfile."""
  with open(LOGFILE, 'a') as f:
    f.write('%s\n' % s)


def ConnectBluetooth(address, port):
  """Attempts to make one connection to the given address and port."""
  sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  try:
    sock.connect((address, port))
  except (bluetooth.btcommon.BluetoothError) as e:
    Log('Failed to connect: %s' % e)
    return None
  return sock


def ConnectBluetoothRetry(address, port, seconds):
  """Attempts to make connections for a number of seconds, exiting program on fail."""
  second = 0
  while second < seconds:
    sock = ConnectBluetooth(address, port)
    if sock:
      Log('Connected after %d seconds' % second)
      return sock
    time.sleep(1)
    second += 1
  Log('Failed to connect after %d seconds' % second)
  sys.exit()


def main():
  """Sends sequential numbers over bluetooth, and receives & parses anything sent."""
  sys.stderr = open(LOGFILE, 'a')

  start = time.time()
  timestring = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S')
  Log('Started at %s' % timestring)

  bd_addr = '00:14:03:05:F4:1B' #Change to our address
  port = 1
  sock = ConnectBluetoothRetry(bd_addr, port, 10)

  buffer = ''
  x = 0

  while True:
    send = COMMAND_START_CHAR+str(x)+COMMAND_END_CHAR
    try:
      sock.send(send)
    except (bluetooth.btcommon.BluetoothError) as e:
      Log('Failed to send %s: %s' % (send, e))
      sock.close()
      sock = ConnectBluetoothRetry(bd_addr, port, 10)
    Log('Sent %s' % send)

    x += 1
    time.sleep(1)


main()
