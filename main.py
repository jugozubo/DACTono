# main.py -- put your code here!
from machine import DAC, Pin, ADC
from time import sleep,sleep_us
import math


salida=DAC(Pin(25))

N=32
frecuencias=[261.63,293.66,329.63,349.23]

def nota(f):
    T=1/f
    t=T/32
    print(f)
    for i in range(32):
        valor=int(127.5*(math.sin(2*math.pi*f*t)+1))
        salida.write(valor)
        t=t+T/32
        sleep_us(int(t*1000000))


while True:
    nota(frecuencias[0])
    sleep(1)
    salida.write(0)
    sleep(1)
    nota(frecuencias[1])
    sleep(1)
    salida.write(0)
    sleep(1)
