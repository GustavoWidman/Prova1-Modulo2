import time
import threading
from collections import deque

import rclpy
from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import String

class Node:
    def __init__(self):
        rclpy.init()
        self.queue = deque()

        self.node = rclpy.create_node('subscriber_gustavo_prova1_modulo2') # type: ignore
        self.subscription = self.node.create_subscription(String, 'topic', self.callback, 10)
        self.publisher = self.node.create_publisher(Twist, "turtle1/cmd_vel", 10)

        self.thread = threading.Thread(target=self.queue_consumer)
        self.thread.daemon = True

        time.sleep(5)

        print('Ready to receive commands\n')

    def queue_consumer(self):
        while True:
            if len(self.queue) > 0:
                msg = self.queue.popleft()

                # :sunglasses: cool inline thing
                vx, vy, vtheta, t = map(float, msg.data.split(" "))

                # casting the t to int shouldnt cause any issues since its hard typed as int on the CLI
                print(f'Moving turtle with vx={vx}, vy={vy}, vtheta={vtheta}, t={int(t)}')
                self.move_sync(vx, vy, vtheta, int(t))
                print('Done moving turtle')
            time.sleep(0.1)

    def move_sync(self, vx: float, vy: float, vtheta: float, t: int):
        twist = Twist()
        twist.linear = Vector3(x=vx, y=vy, z=0.0)
        twist.angular = Vector3(x=0.0, y=0.0, z=vtheta)

        start = time.time()
        while time.time() - start < (t / 1000):
            self.publisher.publish(twist)
            time.sleep(0.1)

        # stop the turtle
        twist.linear = Vector3(x=0.0, y=0.0, z=0.0)
        twist.angular = Vector3(x=0.0, y=0.0, z=0.0)
        self.publisher.publish(twist)

    def callback(self, msg: String):
        self.queue.append(msg)

    def init(self):
        self.thread.start()

def main():
    node_wrapper = Node()
    node_wrapper.init()

    rclpy.spin(node_wrapper.node)
    node_wrapper.node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()