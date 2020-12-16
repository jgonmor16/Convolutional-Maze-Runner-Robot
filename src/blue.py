import sys
import bluetooth

bd_addr = '48:87:2D:12:10:65'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

while True:
    sock.send('f'.encode())

