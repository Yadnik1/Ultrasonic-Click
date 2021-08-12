from machine import UART,Pin
import time,utime
import sys

bytes (buf0) = (0x55, 0x00, 0x01,0xFE)
bytes (buf1) = (0x55, 0x01, 0x01, 0xFD)
bytes (buf5)= (0x55, 0x05, 0xFA)
bytes (buf10)= (0x55, 0x0A, 0x26, 0x00, 0xCF)
bytes (buf17)= (0x55, 0x11, 0x01, 0xED)
bytes (buf19) = (0x55, 0x13, 0x01, 0xEB)
bytes (buf25) =  (0x55, 0x19, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x84, 0x21, 0x08, 0x42, 0x10, 0x80, 0x80, 0x80, 0x80, 0x00, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x84, 0x21, 0x08, 0x42, 0x10, 0x80, 0x80, 0x80, 0x80, 0x00, 0x7C)


class Ultrsonic:

    def __init__(self,uart):
        self.uart = uart

    def distance_mm(self):
            
            utime.sleep_ms(1)
            uart.write(b'\buf25')
            utime.sleep_ms(100)
            uart.write(b'\buf10')
            utime.sleep_ms(100)
            t = 0
            buf = bytearray(2)
            while t < 1000:
                t = t + 1
                utime.sleep_ms(5)
            if t < 1000:
                uart.readinto(buf, 2)           
            dist = buf[0] * 256 + buf[1]
            if dist > 1100:
                    dist = -1                
            print(dist)
            utime.sleep_ms(1)
            uart.write(b'\buf17')
            utime.sleep_ms(100)
            uart.write(b'\buf5')
            utime.sleep_ms(100)

uart=UART("UART_1")
sonar=Ultrsonic(uart)
while True:
    obstacle_distance=sonar.distance_mm()
    print(obstacle_distance)

    
