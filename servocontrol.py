# Start the servod daemon from ./servoblaster/PiBits/servoblaster/
# It sets up a named pipe device named /dev/servoblaster.
# Writing pulse width to /dev/servoblaster actuates the servo.
#
# Example: echo 0=150 > /dev/servoblaster
# The example means send pulse width of 150 steps (each step is 10us, so pulse width is 1500us or 1.5ms)
# to servo #0 (which by default should be connected to pin 7, unless the defaults are overridden from servod command line).
# Note that 'sudo' is not required because all users have write permission on /dev/servoblaster
#
# The list of default pins and servo numbers are shown below. What this means is if you connect
# servo to board pin 7, that servo can be addresses as '0'.
#      Servo number    GPIO number   Pin in P1 header

#          4              22             P1-15   rotation: left =+ rotation right =- 
#          5              23             P1-16   claw: open = - close = +
#          6              24             P1-18   up = + down = -
#          7              25             P1-22   vorward = + backward = -

#       P1-02 = input pin for the button on the right side. low active

# rotation positions:
# left    = 99%
# middle1 = 64% 
# middle2 = 52%
# middle3 = 38%
# right   = 4%


from time import sleep

import subprocess

hold_position_time = 0.02 # secs
step_size = 5  # ie, change pulse width by 10*10us = 100us or 0.1ms in each step

# Dont buffer the writes to the device file, to avoid explicit flush()es.
dont_buffer = 0

wait_time = 1

def init():
    pos_open = 50
    cmd="4=50%\n"  #claw
    print (cmd)
    servo_blaster_device.write(cmd)
    cmd="5=50%\n"  #rotate
    print (cmd)
    servo_blaster_device.write(cmd)
    cmd="6=80%\n"   # up/down
    print (cmd)
    servo_blaster_device.write(cmd)
    cmd="7=20%\n"   # forward/backward
    print (cmd)
    servo_blaster_device.write(cmd)

    

def openClaw():
    pos_open = 50
    cmd="5=" + str(pos_open) + "%\n"
    print (cmd)
    servo_blaster_device.write(cmd)
    sleep(wait_time)

def closeClaw():
	pos_close = 69
	cmd="5=" + str(pos_close) + "%\n"
	print (cmd)
	servo_blaster_device.write(cmd)
	sleep(wait_time)


def openClaw2():
	for pulse_width in range(100,200,step_size):
		cmd="5=" + str(pulse_width) + "\n"
		print (cmd)
		servo_blaster_device.write(cmd)
		sleep(hold_position_time)

def closeClaw2():
	for pulse_width in range(200,100,step_size):
		cmd="5=" + str(pulse_width) + "\n"
		print (cmd)
		servo_blaster_device.write(cmd)
		sleep(hold_position_time)

def runServoMaster():
    # this does not work yet, because I don't know how to get into the right directory
    # which is /ubirch/PiBits/ServoMaster/user
    # from there the following command has to be called
    subprocess.call('sudo ./servod --cycle-time=30000 --step-size=100',shell=True)
    
def endServoMaster():
    subprocess.call('sudo killall servod',shell=True)
    


# start
runServoMaster()


with open('/dev/servoblaster', "w", dont_buffer ) as servo_blaster_device:
    init()
    while True:
        openClaw()
        closeClaw()


