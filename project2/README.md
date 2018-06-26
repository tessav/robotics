# Localization with ROS
The objective of this project is to create a ROS package for localizing a robot in a provided map.  

## Background
Kalman Filter | Particle Filter
:------------|:---------------
Comparison | Comparison

![Map Used]()

## ROS Setup

### Robot Models
2 Wheels | 4 Wheels
:------------|:---------------
Comparison | Comparison

### Navigation & Localization
1. Adaptive Monte Carlo Localization (AMCL) package
2. Navigation Stack package 

## Parameter Tuning
Component | Parameter | Definition | Value
:--------|:---------|:----------|:--------
cost map | **update_frequency** | frequency in Hz for the map to be updated | 0.5
cost map | **publish_frequency** | frequency in Hz for the map to be publish display information | 0.2
cost map | **transform_tolerance** | specifies the delay in transform (tf) data that is tolerable in seconds | 0.3
cost map | **obstacle_range** | max distance from the robot at which an obstacle will be inserted into the cost map in m | 1.0
cost map | **raytrace_range** | range in m at which to raytrace out obstacles from the map using sensor data | 1.0
cost map | **inflation_radius** | determines min distance between the robot geometry and the obstacles | 5.0
amcl | **max_particles** | max allowed number of particles | 500
amcl | **update_min_d** | translational movement required before performing a filter update | 0
amcl | **update_min_a** | rotational movement required before performing a filter update | 0
laser | **laser_max_range** | max scan range to be considered | 0
laser | **max_beams** | how many evenly-spaced beams in each scan to be used when updating the filter | 0
laser | **laser_z_hit** | mixture weight for the z_hit part of the model | 0
planner | **acc_lim_x** | x acceleration limit of the robot in meters/sec^2 | 0
planner | **acc_lim_y** | y acceleration limit of the robot in meters/sec^2 | 0
planner | **acc_lim_theta** | rotational acceleration limit of the robot in radians/sec^2 | 0
planner | **max_vel_x** | max forward velocity allowed for the base in meters/sec | 0
planner | **max_vel_theta** | max rotational velocity allowed for the base in radians/sec | 0
planner | **min_in_place_vel_theta** | min rotational velocity allowed for the base while performing in-place rotations in radians/sec | 0
planner | **escape_vel** | speed used for driving during escapes in meters/sec | 0
goal | **yaw_goal_tolerance** | tolerance in radians for the controller in yaw/rotation when achieving its goal | 0
goal | **xy_goal_tolerance** |  tolerance in meters for the controller in the x & y distance when achieving a goal | 0
simulation | **sim_time** |  amount of time to forward-simulate trajectories in seconds | 0
trajectory | **pdist_scale** | weighting for how much the controller should stay close to the path it was given | 0
trajectory | **occdist_scale** | weighting for how much the controller should attempt to avoid obstacles | 0

## Results

## Discussion

## Reference
[Navigation Guide](http://kaiyuzheng.me/documents/navguide.pdf)
