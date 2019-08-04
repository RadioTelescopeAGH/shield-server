import RPi.GPIO as GPIO
import threading
from time import sleep

motor_a_pwm = 12
motor_a0 = 13
motor_a1 = 15

motor_b_pwm = 16
motor_b0 = 18
motor_b1 = 19

frequency = 1

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motor_a_pwm, GPIO.OUT)

pwm_a = GPIO.PWM(motor_a_pwm, frequency)

GPIO.setup(motor_a0, GPIO.OUT)
GPIO.setup(motor_a1, GPIO.OUT)

GPIO.setup(motor_b_pwm, GPIO.OUT)

pwm_b = GPIO.PWM(motor_b_pwm, frequency)

GPIO.setup(motor_b0, GPIO.OUT)
GPIO.setup(motor_b1, GPIO.OUT)

shutdown = False

epsilon = 0.01

target = (0.0, 0.0)
current = (0.0, 0.0)


def get_speed(dx):
    return 75.0  # to calculate


def sendTarget(pos):
    (phi, theta) = pos
    if len(pos) == 2:
        target = pos
        return 0
    return 1


def loop():
    while not shutdown:
        (target_phi, target_theta) = target
        (current_phi, current_theta) = current
        
        dPhi = target_phi - current_phi
        dTheta = target_theta - current_theta

        moveA = False
        moveB = False
        
        if dPhi < epsilon:
            GPIO.output(motor_a0, GPIO.LOW)
            GPIO.output(motor_a1, GPIO.LOW)
        if dTheta < epsilon:
            GPIO.output(motor_b0, GPIO.LOW)
            GPIO.output(motor_b1, GPIO.LOW)
        if moveA and dPhi > 0:
            GPIO.output(motor_a0, GPIO.HIGH)
            GPIO.output(motor_a1, GPIO.LOW)
            pwm_a.ChangeDutyCycle(get_speed(dPhi))
        elif moveA:
            GPIO.output(motor_a0, GPIO.LOW)
            GPIO.output(motor_a1, GPIO.HIGH)
            pwm_a.ChangeDutyCycle(get_speed(dPhi))
        if moveB and dTheta > 0:
            GPIO.output(motor_b0, GPIO.HIGH)
            GPIO.output(motor_b1, GPIO.LOW)
            pwm_b.ChangeDutyCycle(get_speed(dTheta))
        elif moveA:
            GPIO.output(motor_b0, GPIO.LOW)
            GPIO.output(motor_b1, GPIO.HIGH)
            pwm_b.ChangeDutyCycle(get_speed(dTheta))
        
        sleep(0.05)
    
    pwm_a.ChangeDutyCycle(100)
    pwm_b.ChangeDutyCycle(100)

    GPIO.output(motor_a0, GPIO.HIGH)
    GPIO.output(motor_a1, GPIO.HIGH)
    GPIO.output(motor_b0, GPIO.HIGH)
    GPIO.output(motor_b1, GPIO.HIGH)

    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()




def stop(t):
    global shutdown
    shutdown = True
    t.join()

def start():
    t = threading.Thread(target=loop)
    t.start()
    return t



t = start()
sleep(1)
stop(t)