import sys
import time as t
import bluetooth

def blue(orders):

    bd_addr = '00:14:03:05:F4:1B'
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
    for data in orders:
        sock.send('f'.encode())
        t.sleep(5)
        sock.send('s'.encode())
        t.sleep(5)


