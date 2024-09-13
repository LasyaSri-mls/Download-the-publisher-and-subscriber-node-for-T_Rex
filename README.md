# Download-the-publisher-and-subscriber-node-for-T_Rex

First, use the "export ROS_DOMAIN_ID=0" to have both devices connected to the same local network.

Create a package using 
     "ros2 pkg create --build-type ament_python --license Apache-2.0 py_pubsub"

Refer the publisher node code from the give 'publisher.py' file.
Now refer the subscriber node code from 'subscriber.py' file.

now build the code using 'colcon build' command.
then setup the source using 'source install/setup.bash'.
Now run the file using 'ros2 run <package_name> <node_name>


Ensure T-REX is publishing to the correct nodes by using "ros2 topic list".
Then check if data is being published correctly by using "ros2 topic echo /fl_count".


 Run the Publisher file to get input for the Subscriber node to read. The publisher node here, will register counts for each wheel (fl, fr, bl, br) at different intervals. We used different intervals to differentiate between each wheel.
 The Subscriber node then receives this information and prints the output of each count registered for the user to read. It will continuously update the count whenever the publisher node updates the count value.
 When connected to T-REX, whenever T-REX is moved and the motor publishes a new count value, the subscriber node will receive this information and display it to the user.
