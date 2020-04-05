import mindwave, time
import RPi.GPIO as GPIO

# initialise PWM pin
GPIO.setmode(GPIO.BOARD)  # BOARD numbering

LEDATT = 11  # BOARD Pin 11 == BCM Pin 17
LEDMED = 12  # BOARD Pin 12 == BCM Pin 18
GPIO.setup(LEDATT, GPIO.OUT)
GPIO.setup(LEDMED, GPIO.OUT)

pwm_LEDATT = GPIO.PWM(LEDATT, 100)
pwm_LEDATT.start(0)
pwm_LEDMED = GPIO.PWM(LEDMED, 100)
pwm_LEDMED.start(0)

# setup headset
headset = mindwave.Headset('/dev/ttyUSB0', '9771')
time.sleep(2)

headset.connect()
print "Connecting..."

while headset.status != 'connected':
    time.sleep(0.5)
    if headset.status == 'standby':
        headset.connect()
        print "Retrying connect..."
print "Connected."

while True:
    time.sleep(.5)
    print "Attention: %s, Meditation: %s" % (headset.attention, headset.meditation)
    if headset.attention > 30:
        pwm_LEDATT.ChangeDutyCycle(min(100, headset.attention-30))
    else:        
        pwm_LEDATT.ChangeDutyCycle(0)
    if headset.meditation > 30:
        pwm_LEDMED.ChangeDutyCycle(min(100, headset.meditation-30))
    else:        
        pwm_LEDMED.ChangeDutyCycle(0)





