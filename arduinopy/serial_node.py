import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
from arduinopy.joy import Joystick

SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

class SerialNode(Node):

    def __init__(self):
        super().__init__('serial_node')
        print("[Serial] Constructor invoked.")

        self.ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

        self.subscription = self.create_subscription(
            String,
            'arduino',
            self.cmd_callback,
            10)
        
        self.joystick = Joystick(self)

    def cmd_callback(self, msg):
        command = msg.data + "\n"
        self.ser.write(command.encode())

def main():

    rclpy.init()
    node = SerialNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()