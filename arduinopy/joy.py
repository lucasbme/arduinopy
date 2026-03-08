from sensor_msgs.msg import Joy
from std_msgs.msg import String

X   = 0
Y   = 1
Z   = 4
PSI = 3

class Joystick:
    def __init__(self, node):
        print("[Joystick] Constructor invoked.")
        
        self.node = node

        self.subscription = node.create_subscription(
            Joy, '/joy', self.joy_callback, 10
        )

        self.publisher = node.create_publisher(
            String, '/arduino/joy', 10
        )

    def joy_callback(self, msg):
        x   = msg.axes[X]
        y   = msg.axes[Y]
        z   = msg.axes[Z]
        psi = msg.axes[PSI]

        cmd_vel_str = f"{x:.2f},{y:.2f},{z:.2f},{psi:.2f}"

        msg = String()
        msg.data = cmd_vel_str

        self.publisher.publish(msg)