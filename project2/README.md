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
cost map | **update_frequency** | def | 0.5
cost map | **publish_frequency** | def | 0.2
cost map | **transform_tolerance** | def | 0.3
cost map | **obstacle_range** | def | 1.0
cost map | **raytrace_range** | def | 1.0
cost map | **inflation_radius** | determines min distance between the robot geometry and the obstacles | 5.0
amcl | **max_particles** | def | 500
amcl | **update_min_d** | def | 0
amcl | **update_min_a** | def | 0
laser | **laser_max_range** | def | 0
laser | **laser_likelihood_max_dist** | def | 0

## Results

## Discussion
