#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist, Vector3
import traceback

class JoyStickController:
    def __init__(self):
        rospy.init_node('3dx_joy_stick_controller')
        self.pub = rospy.Publisher('/RosAria/cmd_vel',Twist , queue_size=1)
        self.sub = rospy.Subscriber('/joy', Joy, self.callback)

    def callback(self, data):
        leftStick_right_and_left = data.axes[0] # Left stick - Right(-1) and Left(1)
        leftStick_down_and_up = data.axes[1] # Left Stick - Down(-1) and Up(1)

        linear_speed = 5 * leftStick_down_and_up
        angular_speed = 5 * leftStick_right_and_left

        # Publish speed data
        self.pub.publish(Twist(Vector3(linear_speed,0,0), Vector3(0,0,angular_speed)))

        print('Joy Stick Output')
        print (leftStick_right_and_left)
        print(leftStick_down_and_up)
        print('------')

if __name__ == '__main__':
    try:
        js_controller = JoyStickController()
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print("ROSInterruptException: {}".format(e))
    except Exception as e:
        print("Unexpected error:", e)
        traceback.print_exc()
