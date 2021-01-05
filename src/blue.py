import sys
import time as t
import bluetooth

def blue(orders):

    bd_addr = '00:14:03:05:F4:1B'
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr,port))
    distancia=10
    for data in orders:
         print(data)
         if data=='GD':
             sock.send('r'.encode())
             t.sleep(0.45)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='GI':
             sock.send('l'.encode())
             t.sleep(0.45)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A1':
             sock.send('f'.encode())
             t.sleep((1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A2':
             sock.send('f'.encode())
             t.sleep(2*(1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A3':
             sock.send('f'.encode())
             t.sleep(3*(1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A4':
             sock.send('f'.encode())
             t.sleep(4*(1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A5':
             sock.send('f'.encode())
             t.sleep(5*(1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)
         if data=='A6':
             sock.send('f'.encode())
             t.sleep(6*(1.7541+distancia)/58.3)
             sock.send('s'.encode())
             t.sleep(1)

