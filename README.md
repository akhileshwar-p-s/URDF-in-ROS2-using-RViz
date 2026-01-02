# URDF-in-ROS2-using-RViz
# Autonomous Mobile Robot (AMR) - URDF Visualization Project

## 🤖 Project Overview

This repository contains the complete URDF (Unified Robot Description Format) model and visualization setup for an Autonomous Mobile Robot (AMR) designed for SLAM and navigation applications. The robot features differential drive kinematics, sensor integration (LiDAR and camera), and has been fully visualized and tested in RViz using ROS2.

## 📁 Project Structure

```
ROBOT_WS/
├── build/
├── install/
├── log/
└── src/
    └── robot_project/
        ├── config/
        │   └── rviz_config.rviz
        ├── launch/
        │   ├── main.launch.py
        │   ├── rviz.launch.py
        │   └── state_publisher.launch.py
        ├── models/urdf/
        │   └── robot_project.xacro
        ├── CMakeLists.txt
        └── package.xml
```

<img width="1026" height="926" alt="image" src="https://github.com/user-attachments/assets/fd07def0-f6d2-4a3f-898a-a8dec7ffefd3" />

<img width="2686" height="658" alt="image" src="https://github.com/user-attachments/assets/63352791-7f2b-4990-9fb1-bfee110bafa5" />

<img width="430" height="469" alt="Screenshot 2026-01-02 at 6 55 14 PM" src="https://github.com/user-attachments/assets/6342d2a7-0df2-4c7c-bda2-31669094d9cc" />


## 🎯 Why Visualization Before Hardware?

### The Critical Importance of Software-First Development

Building physical robots is expensive, time-consuming, and difficult to debug. **Visualization in simulation is not optional—it's essential.** Here's why:

#### 1. **Cost Savings** 💰
- Physical components cost money and time to procure
- Design mistakes in hardware can require complete part replacements
- Testing in simulation is free and instantaneous

#### 2. **Rapid Iteration** ⚡
- Modify designs in minutes, not days
- Test dozens of configurations quickly
- Identify problems before they become expensive mistakes

#### 3. **Debugging is 10x Easier** 🔍
- Visualize coordinate frames, transformations, and sensor data in real-time
- Inspect robot geometry from any angle
- Debug kinematic issues without physical access to the robot

#### 4. **Safety** ⚠️
- Test potentially dangerous movements in simulation first
- Validate control algorithms before risking hardware damage
- Ensure sensor placements won't cause collisions

#### 5. **Design Validation** ✅
- Verify dimensions and clearances
- Check sensor field-of-view coverage
- Validate differential drive kinematics
- Ensure proper center of mass and stability

## 🚀 Robot Features

### Mechanical Design
- **Differential Drive System**: Two powered wheels for precise motion control
- **Caster Wheel**: Passive support wheel for stability
- **Compact Footprint**: Optimized for indoor navigation

### Sensor Suite
- **LiDAR**: 360° environment scanning for mapping and obstacle detection
- **Camera**: Visual perception for object recognition and navigation
- **Odometry**: Wheel encoders for position estimation

### Capabilities
- SLAM (Simultaneous Localization and Mapping)
- Autonomous navigation
- Obstacle avoidance
- Path planning

## 🔧 Development Workflow

### The Visualization-First Approach

1. **Design Phase**
   - Create initial URDF/XACRO model
   - Define robot dimensions and joint configurations
   - Add visual and collision geometries

2. **Visualization Phase** 
   - Load model in RViz
   - Verify all links and joints
   - Check coordinate frame transformations
   - Validate sensor placements and FOV

3. **Simulation Phase**
   - Test in Gazebo with physics
   - Validate control algorithms
   - Test sensor integration
   - Simulate navigation scenarios

4. **Refinement Phase**
   - Iterate on design based on simulation results
   - Optimize parameters (PID gains, sensor positions, etc.)
   - Test edge cases and failure modes

5. **Hardware Phase**
   - Confident in design, proceed to physical build
   - Hardware matches tested virtual model
   - Debugging is minimal because algorithms are proven

## 📊 What Visualization Reveals

### TF Tree Analysis
View the complete transform tree to ensure:
- All frames are properly connected
- No missing or broken transforms
- Parent-child relationships are correct
- Sensor frames are correctly positioned

### Geometry Validation
- Wheel radius and separation distance
- Ground clearance
- Sensor mounting heights
- Collision boundaries

## 🧪 Testing in RViz

### Key Elements to Verify
- ✅ Robot model loads without errors
- ✅ All links are visible and properly positioned
- ✅ Joints move correctly (use joint_state_publisher_gui)
- ✅ TF frames are all green and connected
- ✅ Sensor visualization (camera frustum, LiDAR rays)
- ✅ Coordinate axes match expected orientations

## 📝 Lessons Learned

> **"Hours in simulation save weeks in hardware debugging."**

This project demonstrates that investing time in visualization and simulation pays massive dividends:

- Design flaws caught early save expensive hardware iterations
- Kinematic problems are obvious in RViz but mysterious on physical robots
- Sensor placement issues are immediately visible
- Testing motion algorithms is safe and fast

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Enhanced sensor models
- Additional launch configurations
- Gazebo simulation files
- Navigation stack integration
- Documentation improvements

## 📚 Resources

- [ROS2 URDF Tutorials](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html)
- [RViz User Guide](https://github.com/ros2/rviz)

## 👤 Author
Akhileshwar Pratap Singh

---
