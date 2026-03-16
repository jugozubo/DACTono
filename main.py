# main.py -- put your code here!
from machine import DAC, Pin, ADC
from time import sleep,sleep_us
import math

from machine import DAC, Pin
from time import sleep
import math

salida = DAC(Pin(25))

# tamaño de la tabla seno
N = 100

# tabla seno
seno = [int(127.5*(1+math.sin(2*math.pi*i/N))) for i in range(N)]

# frecuencias de las notas
DO  = 261.63
RE  = 293.66
MI  = 329.63
FA  = 349.23
SOL = 392.00
LA  = 440.00
SI  = 493.88

def nota(freq, dur):
    t0 = ticks_us()
    while ticks_diff(ticks_us(), t0) < dur*1000000:
        for v in seno:
            salida.write(v)
            sleep(1/(freq*N))

while True:
    nota(DO,1)
    salida.write(0)
    sleep(0.5)
    nota(RE,1)
    salida.write(0)
    sleep(0.5)

