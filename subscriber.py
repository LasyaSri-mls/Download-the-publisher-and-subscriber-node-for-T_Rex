import rclpy
from rclpy.node import Node

from std_msgs.msg import String, Int32


class Subscriber(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription_fl = self.create_subscription(Int32, 'fl_count', self.listener_callback_fl, 10)
        self.subscription_fr = self.create_subscription(Int32, 'fr_count', self.listener_callback_fr, 10)
        self.subscription_bl = self.create_subscription(Int32, 'bl_count', self.listener_callback_bl, 10)
        self.subscription_br = self.create_subscription(Int32, 'br_count', self.listener_callback_br, 10)

    def listener_callback_fl(self, msg):
        self.get_logger().info('fl_count: "%d"' % msg.data)

    def listener_callback_fr(self, msg):
        self.get_logger().info('fr_count: "%d"' % msg.data)

    def listener_callback_bl(self, msg):
        self.get_logger().info('bl_count: "%d"' % msg.data)
    
    def listener_callback_br(self, msg):
        self.get_logger().info('br_count: "%d"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
