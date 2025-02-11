#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Image
import numpy as np
import cv2
import yaml
import os
from cv_bridge import CvBridge

class TurtleBot3PathDrawer(Node):
    def __init__(self):
        super().__init__('turtlebot3_path_drawer')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10)
        self.publisher = self.create_publisher(Image, '/path_image', 10)
        self.bridge = CvBridge()
        self.path = []
        self.resolution = 0.05  # meters per pixel
        self.map_size = [500, 500]  # pixels
        self.map_image = np.ones(self.map_size, dtype=np.uint8) * 255  # Initialize with white
        self.origin = None
        self.maps_dir = "maps"

        # Ensure the maps folder exists
        if not os.path.exists(self.maps_dir):
            os.makedirs(self.maps_dir)

    def odom_callback(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if not self.origin:
            self.origin = [x, y]

        pixel_x = int((x - self.origin[0]) / self.resolution) + self.map_size[0] // 2
        pixel_y = self.map_size[1] - (int((y - self.origin[1]) / self.resolution) + self.map_size[1] // 2)

        if self.path:
            prev_pixel_x, prev_pixel_y = self.path[-1]
            cv2.line(self.map_image, (prev_pixel_x, prev_pixel_y), (pixel_x, pixel_y), 0, 1)

        self.path.append((pixel_x, pixel_y))

        # Display the map
        cv2.imshow('TurtleBot3 Path', self.map_image)
        cv2.waitKey(1)  # Refresh the window

        # Publish the image as a ROS2 topic
        image_msg = self.bridge.cv2_to_imgmsg(self.map_image, encoding="mono8")
        self.publisher.publish(image_msg)

    def save_map(self):
        # Get the next map number
        map_number = self.get_next_map_number()

        # Define the map and YAML file names
        map_filename = f"map{map_number}.pgm"
        yaml_filename = f"map{map_number}.yaml"

        # Save the map in the "maps" folder
        map_path = os.path.join(self.maps_dir, map_filename)
        yaml_path = os.path.join(self.maps_dir, yaml_filename)

        # Save the map image
        cv2.imwrite(map_path, self.map_image)

        # Create and save the YAML file
        yaml_data = {
            'image': map_filename,
            'resolution': self.resolution,
            'origin': [-self.map_size[0] // 2 * self.resolution, -self.map_size[1] // 2 * self.resolution, 0.0],
            'negate': 0,
            'occupied_thresh': 0.65,
            'free_thresh': 0.196,
            'mode': 'trinary'
        }

        with open(yaml_path, 'w') as yaml_file:
            yaml.dump(yaml_data, yaml_file, default_flow_style=False)

        self.get_logger().info(f"Map saved as '{map_path}' and YAML saved as '{yaml_path}'.")

    def get_next_map_number(self):
        # Get the list of existing map files in the "maps" folder
        existing_maps = [f for f in os.listdir(self.maps_dir) if f.endswith('.pgm')]
        map_numbers = [int(f[3:-4]) for f in existing_maps if f[3:-4].isdigit()]

        if map_numbers:
            return max(map_numbers) + 1
        else:
            return 1

    # Function to stop mapping and destroy the node
    def stop_mapping(self):
        self.save_map()  # Save map and YAML
        self.get_logger().info("Mapping stopped and map saved.")
        self.destroy_node()  # Destroy the node

def main(args=None):
    rclpy.init(args=args)
    drawer = TurtleBot3PathDrawer()

    print("Press 'Ctrl+C' to stop and save the map.")
    try:
        rclpy.spin(drawer)
    except KeyboardInterrupt:
        pass

    drawer.stop_mapping()  # Call stop_mapping to save and stop
    rclpy.shutdown()

if __name__ == '__main__':
    main()