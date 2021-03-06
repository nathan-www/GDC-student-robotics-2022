from math import *
from mimetypes import MimeTypes
from pyexpat.errors import XML_ERROR_UNEXPECTED_STATE

class Motors:
    def __init__(self, w1_power=None, w2_power=None, w3_power=None, mtype=None, turn=None, rotation=None, speed=494.85, time=None, x_pos = None, y_pos = None):
        self.w1_power = w1_power
        self.w2_power = w2_power
        self.w3_power = w3_power
        self.mtype = mtype
        self.turn = turn
        self.rotation = rotation
        self.speed = speed
        self.time = time
        self.x_pos = x_pos
        self.y_pos = y_pos      
motors = Motors()

def input_to_output():
    motors.mtype = "null"
    accepted_types = ["f","r","b"]
    while motors.mtype not in accepted_types:
        print("Rotation or forwards/backwards?")
        motors.mtype = input("r/f/b: ")
    if motors.mtype == "f" or motors.mtype == "b":
        motors.distance = int(input("distance? (s): "))
    else:
        motors.turn = int(input("angle? (-180<a<180): "))
    movements = movement_calc()
    return movements

def movement_calc():
    if motors.mtype == "f" or motors.mtype == "b":
        distance = motors.distance/cos(radians(30))
        motors.time = float(distance / motors.speed)       
        if motors.mtype == "f":
            motors.w1_power = 1
            motors.w2_power = -1
            motors.w3_power = 0
        else:
            motors.w1_power = -1
            motors.w2_power = 1
            motors.w3_power = 0
        return motors.time, motors.w1_power, motors.w2_power, motors.w3_power
    
    else:
        power = 1
        if motors.turn > 180:
            motors.turn = motors.turn - 180
            power = -1
        distance = motors.turn * ((pi * 2 * 280) / 360)
        motors.time = distance / motors.speed
        return motors.time, power, power, power

def coordinates_calc():
    if motors.mtype == "f" or motors.mtype == "b":
        motors.x_pos += (motors.distance * sin(motors.rotation))
        motors.y_pos += (motors.distance * cos(motors.rotation))
    else:
        motors.rotation += (motors.turn)
        if motors.rotation > 360:
            motors.rotation -= 360
        elif motors.rotation < 0:
            motors.rotation += 360

