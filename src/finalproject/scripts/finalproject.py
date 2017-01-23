#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3

def callback(data):
	leftStick_right_and_left = data.axes[0] # Left stick - Right(-1) and Left(1)
	leftStick_down_and_up = data.axes[1] # Left Stick - Down(-1) and Up(1)
	# Values are from 0 - 1
	# Want to ignore values between 0 - .15 because it makes respones very
	# sensetive

	print('Joy Stick Output')
	print (leftStick_right_and_left)
	print(leftStick_down_and_up)
	if (is_right(leftStick_right_and_left)):
		pass
	elif(is_left(leftStick_right_and_left)):
		pass
	elif(is_down(leftStick_down_and_up)):
		pass
	elif(is_up(leftStick_down_and_up)):
		pass



	print('------')

def is_down(value):
	if value < -.2:
		pub.publish(Twist(Vector3(-5,0,0),Vector3(0,0,0)))
		return True
	else:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
		return False

def is_right(value):
	if value < -.2:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,-5)))
		return True
	else:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
		return False

def is_up(value):
	if value > .2:
		pub.publish(Twist(Vector3(5,0,0),Vector3(0,0,0)))
		return True
	else:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
		return False


def is_left(value):
	if value > .2:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,5)))
		return True
	else:
		pub.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))
		return False




def Subscriber():
    rospy.Subscriber('/joy', Joy, callback)

if __name__ == '__main__':
    try:
    	rospy.init_node('finalproject')
    	pub = rospy.Publisher('/RosAria/cmd_vel',Twist , queue_size=1)
    	while not rospy.is_shutdown():
    		Subscriber()
    		rospy.spin()
    except rospy.ROSInterruptException:
    	pass