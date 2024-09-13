import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32


class Publisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.publisher_fl = self.create_publisher(Int32, 'fl_count', 10)
        self.publisher_fr = self.create_publisher(Int32, 'fr_count', 10)
        self.publisher_bl = self.create_publisher(Int32, 'bl_count', 10)
        self.publisher_br = self.create_publisher(Int32, 'br_count', 10)
        timer_period_fl_count = 0.5  # seconds
        timer_period_fr_count = 1.0  # seconds
        timer_period_bl_count = 1.5  # seconds
        timer_period_br_count = 2.5  # seconds
        self.timer_fl = self.create_timer(timer_period_fl_count, self.timer_callback_fl)
        self.timer_fr = self.create_timer(timer_period_fr_count, self.timer_callback_fr)
        self.timer_bl = self.create_timer(timer_period_bl_count, self.timer_callback_bl)
        self.timer_br = self.create_timer(timer_period_br_count, self.timer_callback_br)
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0

    def timer_callback_fl(self):
        msg = Int32()
        msg.data = self.i
        self.publisher_fl.publish(msg)
        self.get_logger().info('fl_count: "%d"' % msg.data)
        self.i += 1

    def timer_callback_fr(self):
        msg = Int32()
        msg.data = self.j
        self.publisher_fr.publish(msg)
        self.get_logger().info('fr_count: "%d"' % msg.data)
        self.j += 1

    def timer_callback_bl(self):
        msg = Int32()
        msg.data = self.k
        self.publisher_bl.publish(msg)
        self.get_logger().info('bl_count: "%d"' % msg.data)
        self.k += 1

    def timer_callback_br(self):
        msg = Int32()
        msg.data = self.l
        self.publisher_br.publish(msg)
        self.get_logger().info('br_count: "%d"' % msg.data)
        self.l += 1


def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
