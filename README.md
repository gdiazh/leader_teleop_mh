# leader_teleop_mh
Simple remapping node for the leader to follower teleoperation

# lauch dynamixel motors interface
```bash
cd dynamixel_hotplug_ros2_python/
ros2 launch src/motor_controller/launch/multi_port_launch.py
```

# check joint angles
```bash
ros2 topic echo /read_joint1_[1-7]
```

# lauch dynamixel mapping to hero joint states
```bash
cd ~/ros2_ws
ros2 run leader_teleop_mh leader_to_joint_states
```
