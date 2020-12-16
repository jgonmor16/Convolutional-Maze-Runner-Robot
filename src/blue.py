import sys
import bluetooth

bd_addr = 'd8:8a:dc:d5:36:e0'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

while True:
    sock.send('f'.encode())

