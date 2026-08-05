import rclpy
import numpy as np
from rclpy.node import Node

from sensor_msgs.msg import JointState
from std_msgs.msg import Float64

class MHLeaderToJointStates(Node):

    def __init__(self):
        super().__init__('mh_leader_to_joint_states')
        # self.joint_state_pub_ = self.create_publisher(JointState, "/leg302/joint_set", 20)
        self.joint_state_pub_ = self.create_publisher(JointState, "/leg302/joint_set_teleop", 30)

        self.feedback1_sub = self.create_subscription(Float64, '/read_joint1_1', self.update_joint1_feedback, 100)
        self.feedback2_sub = self.create_subscription(Float64, '/read_joint1_2', self.update_joint2_feedback, 100)
        self.feedback3_sub = self.create_subscription(Float64, '/read_joint1_3', self.update_joint3_feedback, 100)
        self.feedback4_sub = self.create_subscription(Float64, '/read_joint1_4', self.update_joint4_feedback, 100)
        self.feedback5_sub = self.create_subscription(Float64, '/read_joint1_5', self.update_joint5_feedback, 100)
        self.feedback6_sub = self.create_subscription(Float64, '/read_joint1_6', self.update_joint6_feedback, 100)
        self.feedback7_sub = self.create_subscription(Float64, '/read_joint1_7', self.update_joint7_feedback, 100)
        self.feedback8_sub = self.create_subscription(Float64, '/read_joint1_8', self.update_joint8_feedback, 100)

        self.joint1_pos = 0.0
        self.joint2_pos = 0.0
        self.joint3_pos = 0.0
        self.joint4_pos = 0.0
        self.joint5_pos = 0.0
        self.joint6_pos = 0.0
        self.joint7_pos = 0.0
        self.grip1_pos = 0.01974
        self.grip2_pos = 0.0110 # open 0.0110, close 0.0210

        self.joint1_vel = 0.0
        self.joint2_vel = 0.0
        self.joint3_vel = 0.0
        self.joint4_vel = 0.0
        self.joint5_vel = 0.0
        self.joint6_vel = 0.0
        self.joint7_vel = 0.0

        self.joint1_eff = 0.0
        self.joint2_eff = 0.0
        self.joint3_eff = 0.0
        self.joint4_eff = 0.0
        self.joint5_eff = 0.0
        self.joint6_eff = 0.0
        self.joint7_eff = 0.0
        self.threshold = 0.01
        self.gripper_threshold = 0.001

        joint_states_publish_period = 0.2  # seconds
        self.joint_states_timer = self.create_timer(joint_states_publish_period, self.joint_states_callback)

    def update_joint1_feedback(self, msg):
        if abs(msg.data - self.joint1_pos) > self.threshold:
            self.joint1_pos = msg.data
        self.joint1_vel = 0.0
        self.joint1_eff = 0.0
    def update_joint2_feedback(self, msg):
        if abs(msg.data - self.joint2_pos) > self.threshold:
            self.joint2_pos = msg.data
        self.joint2_vel = 0.0
        self.joint2_eff = 0.0
    def update_joint3_feedback(self, msg):
        if abs(msg.data - self.joint3_pos) > self.threshold:
            self.joint3_pos = msg.data
        self.joint3_vel = 0.0
        self.joint3_eff = 0.0
    def update_joint4_feedback(self, msg):
        if abs(msg.data - self.joint4_pos) > self.threshold:
            self.joint4_pos = msg.data
        self.joint4_vel = 0.0
        self.joint4_eff = 0.0
    def update_joint5_feedback(self, msg):
        if abs(msg.data - self.joint5_pos) > self.threshold:
            self.joint5_pos = msg.data
        self.joint5_vel = 0.0
        self.joint5_eff = 0.0
    def update_joint6_feedback(self, msg):
        if abs(msg.data - self.joint6_pos) > self.threshold:
            self.joint6_pos = msg.data
        self.joint6_vel = 0.0
        self.joint6_eff = 0.0
    def update_joint7_feedback(self, msg):
        if abs(msg.data - self.joint7_pos) > self.threshold:
            self.joint7_pos = msg.data
        self.joint7_vel = 0.0
        self.joint7_eff = 0.0

    def update_joint8_feedback(self, msg):
        if abs(msg.data - self.grip2_pos) > self.gripper_threshold:
            self.grip2_pos = msg.data

    def joint_states_callback(self):
        joint_state = JointState()
        joint_state.header.stamp = rclpy.clock.Clock().now().to_msg()
        joint_state.name = ['leg302_joint1', 'leg302_joint2', 'leg302_joint3', 'leg302_joint4', 'leg302_joint5', 'leg302_joint6', 'leg302_joint7', 'leg302_grip1', 'leg302_grip2']
        joint_state.position = [self.joint1_pos, self.joint2_pos, self.joint3_pos, self.joint4_pos, self.joint5_pos, self.joint6_pos, self.joint7_pos, self.grip1_pos, self.grip2_pos]

        # joint_state.name = ['leg302_joint1', 'leg302_joint2', 'leg302_joint3', 'leg302_joint4', 'leg302_joint5', 'leg302_joint6', 'leg302_joint7']
        # joint_state.position = [self.joint1_pos, self.joint2_pos, self.joint3_pos, self.joint4_pos, self.joint5_pos, self.joint6_pos, self.joint7_pos]
        

        # joint_state.velocity = [self.joint1_vel, self.joint2_vel, self.joint3_vel, self.joint4_vel, self.joint5_vel, self.joint6_vel, self.joint7_vel]
        # joint_state.effort = [self.joint1_eff, self.joint2_eff, self.joint3_eff, self.joint4_eff, self.joint5_eff, self.joint6_eff, self.joint7_eff]
        

        self.joint_state_pub_.publish(joint_state)
        self.get_logger().info('Publishing: "%s"' % str(joint_state))

def main(args=None):
    rclpy.init(args=args)

    mh_leader_to_joint_states_nh = MHLeaderToJointStates()

    rclpy.spin(mh_leader_to_joint_states_nh)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    mh_leader_to_joint_states_nh.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()