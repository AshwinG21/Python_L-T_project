import socket
import math
from RPi import GPIO

global DUTY
DUTY = 0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
UDP_IP = "192.168.43.181"
UDP_PORT = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind((UDP_IP, UDP_PORT))

# for horizontal rotation
pl = GPIO.PWM(18, 50)
pl.start(0)

# for vertical rotation
pr = GPIO.PWM(13, 50)
pr.start(0)


def SET_ANGLE(angle):
    """ A Dummy docstring. """
    return (angle + 90) / 18 + 2


def dist(a_s, b_s):
    """ A Dummy docstring. """
    return math.sqrt((a_s * a_s) + (b_s * b_s))


def get_y_rotation(x_s, y_s, z_s):
    """ A Dummy docstring. """
    radians = math.atan2(x_s, dist(y_s, z_s))
    return math.degrees(radians)


def get_x_rotation(x_s, y_s, z_s):
    """ A Dummy docstring. """
    radians = math.atan2(y_s, dist(x_s, z_s))
    return math.degrees(radians)


def get_acc(data):
    """ A Dummy docstring. """
    imu_op = data.split(',')
    acc_x = float(imu_op[2])
    acc_y = float(imu_op[3])
    acc_z = float(imu_op[4])
    return [acc_x, acc_y, acc_z]


Flag = True
while True:
    data, addr = sock.recvfrom(1024)
    acc_op = get_acc(data)

    y_theta = get_y_rotation(acc_op[0], acc_op[1], acc_op[2])
    x_theta = get_x_rotation(acc_op[0], acc_op[1], acc_op[2])

    DUTY_x = int(SET_ANGLE(x_theta))
    DUTY_y = int(SET_ANGLE(-y_theta))

    if Flag:
        pr.ChangeDUTYCycle(DUTY_x)
        pl.ChangeDUTYCycle(DUTY_y)
        x_old = DUTY_y
        y_old = DUTY_y
        Flag = False

    # to stablize the movement of gimbal
    if abs(DUTY_x - x_old) >= 1:
        pr.ChangeDUTYCycle(DUTY_x)
        x_old = DUTY_x
    else:
        pr.ChangeDUTYCycle(0)

    # time.sleep(2)

    if abs(DUTY_y - y_old) >= 1:
        pl.ChangeDUTYCycle(DUTY_y)
        y_old = DUTY_y
    else:
        pl.ChangeDUTYCycle(0)

    # flag = False;
    # print(y_theta , "y_th" )
    # print(x_theta , "x_th")
    # print(duty_x , "duty_x" )
    # print(duty_y , "duty_y")
    # print( "")
    # time.sleep(3)

pl.stop()
pr.stop()
GPIO.cleanup()
