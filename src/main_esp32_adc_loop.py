from machine import Pin, ADC, PWM, Timer
from time import sleep



pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
# while True:
#   pot_value = pot.read()
#   print(pot_value)
#   sleep(0.5)

def read_adc():
    nVal = pot.read()
    vVal = nVal*3.3/4095 - 0.03
    print("Voltage", vVal)

    


#pwm2 = PWM(Pin(27), freq=2000, duty=512)  # create and configure in one go
#print(pwm2) 

tim1 = Timer(1)
tim1.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:read_adc())
