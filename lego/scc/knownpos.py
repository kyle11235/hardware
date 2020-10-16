#!/usr/bin/env python3
from ev3dev.ev3 import *
import time
import sys

# change log
# all sensors included
# initally all sensors existence verified with stop() call
# changing speed to 45 and 60
# move the object based on ultrasonic-sensor
# stop motors once movement is over
# probe for color after grabbing the object
# changing the ports 
# new colors also added 
# halt implemented

BASE_EXTRA = 0.030 #0.035
BASE_GEAR_RATIO = 12.0 / 36.0
SLOW_SPEED = 30 #45
MEDIUM_SPEED = 45 #60
HIGH_SPEED = 60 #90

grab_motor = MediumMotor(OUTPUT_A)
lift_motor = LargeMotor(OUTPUT_B)
base_motor = LargeMotor(OUTPUT_C)
base_limit_sensor = TouchSensor()
lift_limit_sensor = ColorSensor()
object_identifier = ColorSensor()
gyro_sensor = GyroSensor() ##
distance_sensor = UltrasonicSensor()
sound = Sound()
button = Button()

color_dest_dict = {"blue":-45, "green":-90, "red":-135, "yellow":-180}
valid_color_dict = {2:"green", 3:"green",4:"yellow",5:"red"}
file_name = "object_color.txt"
haltarm_file = "halt_basem.txt"
halt_status = "LIVE"
 
# arrange lift motor
def lift_motor_init():
    global lift_motor

    lift_motor.reset()
    time.sleep(1)
    lift_motor.reset()
    time.sleep(1)  #with this, the position would be 0
    lift_motor.run_to_rel_pos(speed_sp=HIGH_SPEED, position_sp=-180,stop_action="hold")
    time.sleep(2.2)
    lift_motor.run_to_rel_pos(speed_sp=HIGH_SPEED, position_sp=180, stop_action="hold")
    time.sleep(2.2)
    lift_motor.reset()
    time.sleep(2)
    lift_motor.reset()
    time.sleep(2)


    curr_pos = 0
    prev_pos = 0
    lift_motor.run_forever(speed_sp=SLOW_SPEED)
    while True:
        time.sleep(1)
        curr_pos = lift_motor.position
        print(str(curr_pos)+":"+str(prev_pos))
        if lift_motor.is_overloaded: #curr_pos - prev_pos < 30:
            lift_motor.stop()
            time.sleep(1)
            lift_motor.reset()
            time.sleep(1)
            lift_motor.reset()
            time.sleep(1) 
            break
        prev_pos = curr_pos

    lift_motor.stop(stop_action="hold")
    time.sleep(1)
    lift_motor.stop(stop_action="hold")
    time.sleep(1)
    lift_motor.reset();
    time.sleep(2);
    lift_motor.run_to_rel_pos(speed_sp=HIGH_SPEED, position_sp=-360, stop_action="hold")
    time.sleep(4.2)
    lift_motor.run_to_rel_pos(speed_sp=HIGH_SPEED, position_sp=90, stop_action="hold")
    time.sleep(1.2)

#now here calibrate gyro sensor 
"""   multi-line comments started here
lift_motor.run_forever(speed_sp=SLOW_SPEED)
while distance_sensor.value(0) > 55:
    time.sleep(0.1)
    print(distance_sensor.value(0))
    pass
    #lift_motor.stop(stop_action="hold")
lift_motor.stop(stop_action="hold")
"""


# to position grab motor
def grab_motor_init():
    global grab_motor

    grab_motor.run_forever(speed_sp=HIGH_SPEED);
    time.sleep(3)
    grab_motor.stop(stop_action="hold");
    grab_motor.reset()
    time.sleep(0.5)
    grab_motor.run_to_rel_pos(position_sp=-75, speed_sp=HIGH_SPEED,stop_action="hold")
    time.sleep(1.2)


#move base motor to known state
def base_motor_init():
    global base_motor

    base_motor.reset()
    base_motor.stop_action = "hold"
    #base_motor.speed_regulation_enabled = "on"
    base_motor.run_forever(speed_sp=HIGH_SPEED)
    while not base_limit_sensor.value(0):
        pass
    base_motor.stop(stop_action="hold")
    pos = int(base_motor.count_per_rot * (0.50 + BASE_EXTRA) / BASE_GEAR_RATIO)
    print("base motor rotating back to:"+str(pos))
    base_motor.position = pos
    base_motor.run_to_abs_pos(speed_sp=HIGH_SPEED, position_sp=0)
    while "holding" not in base_motor.state:
        pass

def calibrateGyro():
    global gyro_sensor
    gyro_sensor.mode = "GYRO-ANG"
    time.sleep(0.1)
    gyro_sensor.mode = "GYRO-RATE"
    time.sleep(0.1)
    gyro_sensor.mode = "GYRO-ANG"
    time.sleep(0.1)

def writeToFile(color):
    global file_name
    print(file_name)
    with open(file_name,"w") as f:
        f.write(color)
    
def readHaltArmFile():
    global haltarm_file
    global halt_status 
    print(haltarm_file)
    with open(haltarm_file, "r") as f:
        halt_status = f.read()
    print(halt_status)
    print(len(halt_status))
    
def init():
    global sound
    stop()
    sound.speak("Wait till you hear Ready").wait()
    base_motor_init()
    lift_motor_init()
    grab_motor_init()
    calibrateGyro()
    calibrateObjectIdentifier("color")
    distance_sensor.mode='US-DIST-CM'
    #base_motor_init()
    writeToFile("none")
    sound.speak("Ready").wait()

def calibrateObjectIdentifier(input):
    global object_identifier
    color_modes = {"reflect":0, "color":1}
    targetMode=color_modes[input]
    calibrationModeTuple = ("COL-REFLECT","COL-COLOR","COL-REFLECT","COL-COLOR")
    object_identifier.mode=calibrationModeTuple[targetMode]
    print("current mode:"+object_identifier.mode)
    time.sleep(0.3)
    object_identifier.mode=calibrationModeTuple[targetMode+1]
    print("current mode:"+object_identifier.mode)
    time.sleep(0.3)
    object_identifier.mode=calibrationModeTuple[targetMode+2]
    print("current mode:"+object_identifier.mode)
    time.sleep(0.3)

def pollObjectColor():
    global object_identifier
    color_counter = {}
    result=-1
    for i in range(10):
        time.sleep(0.5*2)
        color_reading = object_identifier.value(0)
        color_counter[color_reading] = color_counter.get(color_reading,0) + 1
    print(color_counter)
    for col in color_counter:
        if col in valid_color_dict and color_counter[col]>=5:
            result = col
            break
    return result

def pollTillObjectColorFound():
    obj_color=-1
    while "backspace" not in button.buttons_pressed:
        obj_color = pollObjectColor()
        print("color of object:"+str(obj_color))
        if obj_color in valid_color_dict:
            print("color in text:"+valid_color_dict[obj_color])
            break
        #obj_color=-1
    writeToFile(valid_color_dict[obj_color])
    return obj_color

def move():
    global grab_motor
    global lift_motor
    global base_motor
    global lift_limit_sensor

    #base_motor.polarity="inversed"
    # rotate the base 90 degrees and wait for completion
    #pos = int(base_motor.count_per_rot * (0.25 + BASE_EXTRA) / BASE_GEAR_RATIO)
    #base_motor.run_to_abs_pos(position_sp=direction * pos)
    #while "holding" not in base_motor.state:
    #    pass

    # lower the lift arm and wait for completion
    print("lowering the lift arm");
    pos = int(lift_motor.count_per_rot * 225 / 360.0)
    lift_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=pos,stop_action="hold")
    while "holding" not in lift_motor.state:
        pass
    lift_motor.run_forever(speed_sp=0)
    time.sleep(1)
    lift_motor.stop(stop_action="hold")
    time.sleep(1)

    # grab an object
    print("grabbing the object");
    grab_first_pos = grab_motor.position;
    print("grab_motor initial pos1:"+str(grab_motor.position));
    grab_motor.run_forever(speed_sp=HIGH_SPEED)
    time.sleep(2)
    #grab_motor.run_forever(speed_sp=0)
    #time.sleep(1)
    grab_motor.stop(stop_action="hold")
    print("grab_motor initial pos2:"+str(grab_motor.position));
    time.sleep(1)
    print("grab_motor initial pos3:"+str(grab_motor.position));
    grab_second_pos = grab_motor.position; 
    grab_diff_pos = grab_second_pos - grab_first_pos; 

    #find the color of the object
    obj_color=pollTillObjectColorFound()
    obj_color=valid_color_dict[obj_color]

    # raise the lift to the limit
    print("raising the lift arm");
    pos = int(lift_motor.count_per_rot * 225 / 360.0)
    lift_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=-pos,stop_action="hold")
    while "holding" not in lift_motor.state:
        pass
    lift_motor.run_forever(speed_sp=0)
    time.sleep(1)
    lift_motor.stop(stop_action="hold")
    time.sleep(1)

    # rotate the base to the target position and wait for completion
    print("moving the base arm");
    adjuster = (color_dest_dict[obj_color]/360.0) * BASE_EXTRA * 2 
    pos = int(base_motor.count_per_rot * ((color_dest_dict[obj_color]/360.0) + adjuster) / BASE_GEAR_RATIO)
    #pos = -pos
    print("target pos relative to currrent pos:"+str(pos))
    print("base motor position:"+str(base_motor.position));
    base_start_pos = base_motor.position
    base_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=-pos,stop_action="hold")
    while "holding" not in base_motor.state:
        pass
    base_motor.run_forever(speed_sp=0)
    time.sleep(1)
    base_motor.stop(stop_action="hold")
    time.sleep(1)

    if "WAIT" in halt_status:
        print("waiting for 10 seconds")
        time.sleep(30)

    # lower the lift arm and wait for completion
    print("lowering the lift arm");
    pos = int(lift_motor.count_per_rot * 225 / 360.0)
    lift_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=pos, stop_action="hold")
    while "holding" not in lift_motor.state:
        pass
    lift_motor.run_forever(speed_sp=0)
    time.sleep(1)
    lift_motor.stop(stop_action="hold")
    time.sleep(1)

    
    # release the object
    print("releasing the object");
    pos = int(grab_motor.count_per_rot * 0.25)
    grab_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=-pos,stop_action="hold") #-grab_diff_pos
    while "holding" not in grab_motor.state:
        pass
    #grab_motor.run_forever(speed_sp=0)
    #time.sleep(0.5)
    grab_motor.stop(stop_action="hold")
    time.sleep(0.5)
    
    """
    #release the object
    print("releasing the object");
    grab_motor_init();
    """

    # raise the lift arm to the limit
    print("raising the lift arm");
    pos = int(lift_motor.count_per_rot * 225 / 360.0)
    lift_motor.run_to_rel_pos(speed_sp=SLOW_SPEED, position_sp=-pos, stop_action="hold")
    while "holding" not in lift_motor.state:
        pass
    lift_motor.run_forever(speed_sp=0)
    time.sleep(1)
    lift_motor.stop(stop_action="hold")
    time.sleep(1)


    # rotate the base to the source/start position and wait for completion
    print("rotating the base motor to bring to start position");
    pos = int(base_motor.count_per_rot *  ((color_dest_dict[obj_color]/360.0) + adjuster) / BASE_GEAR_RATIO)
    print("moving to start pos:"+str(pos))
    #base_start_pos
    base_motor.run_to_abs_pos(speed_sp=SLOW_SPEED, position_sp=0,stop_action="hold")
    #print("base motor position:"+str(base_motor.position_sp));
    while "holding" not in base_motor.state:
        pass
    print("base motor position:"+str(base_motor.position));
    base_motor.run_forever(speed_sp=0)
    time.sleep(1)
    base_motor.stop(stop_action="hold")
    time.sleep(1)
    base_motor.polarity="normal"
    writeToFile("none")

    #firm the grab arm
    print("reposition the grab arm");
    grab_motor_init();
 
    print("brought to start position");

def stop():
    global lift_limit_sensor
    global grab_motor
    global lift_motor
    global base_motor
    global sound
    global base_limit_sensor
    global gyro_sensor
    global distance_sensor 

    lift_limit_sensor.mode = "COL-AMBIENT"
    grab_motor.reset()
    time.sleep(0.2)
    lift_motor.reset()
    time.sleep(0.2)
    base_motor.reset()
    time.sleep(0.2)
    distance_sensor.mode='US-DIST-CM'
    gyro_sensor.mode='GYRO-RATE'
    time.sleep(0.5)


if __name__ == "__main__":
    #base_motor_init();
    #sys.exit("exiting program");
    init()
    while "backspace" not in button.buttons_pressed:
        #obj_color=pollTillObjectColorFound()
        try:
            distance_sensor.mode='US-DIST-CM'
            print("distance of the object:"+str(distance_sensor.value()))
            if distance_sensor.value()>=25 and distance_sensor.value()<=55:
                readHaltArmFile()
                move()
        except (Exception, OSError):
            print("oops! something wrong... Reinitializing ultrasonic sensor")
            distance_sensor = UltrasonicSensor()
 
        time.sleep(0.5)

    stop()
    sound.speak("Goodbye!").wait()
