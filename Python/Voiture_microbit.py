# À ouvrir avec le site : python.microbit.org

from microbit import *

impulsion1 = 1500
impulsion2 = 1500

def set_servo1(impulsion1):
    alpha1 = (impulsion1 / 20000) * 100
    duty1 = (alpha1 / 100 ) * 1023
    pin1.set_analog_period_microseconds(20000)
    pin1.write_analog(duty1)
    print('impulsion1=',impulsion1, ' alpha1=', alpha1, ' duty1=', duty1)

def set_servo2(impulsion2):
    alpha2 = (impulsion2 / 20000) * 100
    duty2 = (alpha2 / 100 ) * 1023
    pin2.set_analog_period_microseconds(20000)
    pin2.write_analog(duty2)
    print('impulsion2=',impulsion2, ' alpha2=', alpha2, ' duty2=', duty2)

def avancer():
    display.show(Image('01910:'
                       '19991:'
                       '93939:'
                       '30903:'
                       '00900'))
    global impulsion1
    global impulsion2
    if impulsion1>500 and impulsion1<2500:
        impulsion1 = impulsion1 - 200
    if impulsion2>500 and impulsion2<2500:
        impulsion2 = impulsion2 + 100
    sleep(250)
    display.clear()
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(1000)

def tourner_gauche():
    display.show(Image('03910:'
                       '00391:'
                       '99999:'
                       '00391:'
                       '03910'))
    global impulsion1
    global impulsion2
    if impulsion1>500 and impulsion1<2500:
        impulsion1 = impulsion1 - 100
    if impulsion2>500 and impulsion2<2500:
        impulsion2 = impulsion2 - 100
    sleep(250)
    display.clear()
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(1000)

def tourner_droite():
    display.show(Image('01930:'
                       '19300:'
                       '99999:'
                       '19300:'
                       '01930'))
    global impulsion1
    global impulsion2
    if impulsion1>500 and impulsion1<2500:
        impulsion1 = impulsion1 + 100
    if impulsion2>500 and impulsion2<2500:
        impulsion2 = impulsion2 + 100
    sleep(250)
    display.clear()
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(1000)

def reculer():
    display.show(Image('00900:'
                       '30903:'
                       '93939:'
                       '19991:'
                       '01910'))
    global impulsion1
    global impulsion2
    if impulsion1>500 and impulsion1<2500:
        impulsion1 = impulsion1 + 200
    if impulsion2>500 and impulsion2<2500:
        impulsion2 = impulsion2 - 100
    sleep(250)
    display.clear()
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(1000)

def arret():
    global impulsion1
    global impulsion2
    display.show(Image.SAD)
    impulsion1 = 1500
    impulsion2 = 1500
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(250)
    display.clear()

def dash():
    global impulsion1
    global impulsion2
    if impulsion1>500 and impulsion1<2500:
        impulsion1 = impulsion1 - 700
    if impulsion2>500 and impulsion2<2500:
        impulsion2 = impulsion2 + 400
    sleep(250)
    display.clear()
    set_servo1(impulsion1)
    set_servo2(impulsion2)
    sleep(1000)

while 1==1 :
    if button_a.was_pressed():
        tourner_droite()
    if button_b.was_pressed():
        tourner_gauche()
    if pin_logo.is_touched():
        avancer()
    if accelerometer.was_gesture('shake'):
        reculer()
    if microphone.current_event() == SoundEvent.LOUD and impulsion1 != 1500 and impulsion2 != 1500:
        arret()
    if microphone.current_event() == SoundEvent.LOUD and impulsion1 == 1500 and impulsion2 == 1500:
        dash()
