 demo-robot

# about
Description of the demo-robot hard and software.

# Hardware
Like shown in the pictures, the robot-demo consists of the main construction, which includes a Pi 3 and a MeArm robot Arm. 
Additionally there are three little Tables, which can be pluged into the main construction on the sides. This ensuders, that the parts don't move. 
The demo-robot needs a 5V Power supply (micro-USB) for the Pi3 and a 6 V power supply for the servo-motors. Both power supplies are connected from the left side. The additional Patch-cable is only if the WiFi cannot be used. 

For transport, the robot arm has to be turned of and with the claw to the left. then the two little side-tables can be stacked next to the claw and the lid can be closed and locked with the little pins in the front and in the back. Just push and pull the pins. If one of them breaks, there are spare parts in the paper box. 

The pictures show how to take it apart and also how to assemble it.

## Features

On the right side of the main housing is a low active button, which is connected to P1-02 pin of the Pi.

## servo-motors

The servo motors are controled via PWM and are co

	  No.	    header Pin No.	Pi Pin No   description
          4              22             P1-15   	rotation: left =+ rotation right =- 
          5              23             P1-16   	claw: open = - close = +
          6              24             P1-18   	up = + down = -
          7              25             P1-22   	vorward = + backward = -

## parts-to-move
there are currently only two parts to move and program the robot arm. Because the claw can not reach below a certain hight, it might be neccessary to place the tranparent coins below the parts. There will be more parts produced in the next days.

# Software
To control the Servo motors, the ServoBlaster drivers from [PiBits](https://github.com/richardghirst/PiBits) are used. All neccessary description can be found in the README.

The drivers have to be enabled by 'sudo ./servod' and can be stopped by 'sudo killall servod'

## Python script
The [servocontrol.py](servocontrol.py) script is used to control the servo drives. Unfortunatelly it is not yet complete for the task. 

# Pi3
all software can be found in the ubirch folder on the SD-card of the Pi.








