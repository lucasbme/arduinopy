import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class SerialNode(Node):

    def __init__(self):
        super().__init__('serial_node')

        self.ser = serial.Serial('/dev/ttyUSB0', 9600)

        self.subscription = self.create_subscription(
            String,
            'arduino',
            self.cmd_callback,
            10)

    def cmd_callback(self,msg):
        command = msg.data + "\n"
        self.ser.write(command.encode())

def main():

    rclpy.init()
    node = SerialNode()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()