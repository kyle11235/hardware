#!/usr/bin/env python3
from ev3dev.ev3 import *

mB = LargeMotor('outB')
mC = LargeMotor('outC')
mA = MediumMotor('outA')

mA.stop(stop_action="coast")
mB.stop(stop_action="coast")
mC.stop(stop_action="coast")

