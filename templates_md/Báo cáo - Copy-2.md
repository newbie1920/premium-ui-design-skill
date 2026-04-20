# 📄 Template: Báo cáo - Copy-2.docx

> **Nguồn gốc:** `Báo cáo - Copy-2.docx`  

> **Mục đích:** Tài liệu mẫu chuẩn TDTU — AI học để trình bày báo cáo đúng format


---


## ⚙️ CÀI ĐẶT TRANG (Page Setup)


| Thông số | Giá trị |
|---|---|

| Khổ giấy | 21.0 × 29.7 cm (A4) |

| Lề trên | 3.5 cm |

| Lề dưới | 3.0 cm |

| Lề trái | 3.5 cm |

| Lề phải | 2.0 cm |


## 🎨 FONT & STYLE ĐƯỢC DÙNG


| Style | Font | Cỡ chữ | Bold | Italic | Ví dụ |
|---|---|---|---|---|---|

| `Normal` | Arial | 14.0pt |  |  | VIETNAM GENERAL CONFEDERATION OF LABOR |

| `Heading 1` | — | —pt |  |  | OVERVIEW OF THE TOPIC |

| `Heading 2` | — | —pt |  |  | Topic Introduction |

| `Caption` | — | —pt |  |  | Figure 1: ESP32-S3 Microcontroller |

| `Normal (Web)` | — | 13.0pt |  |  | The system uses a Differential Drive model. The ro |

| `Heading 3` | — | —pt |  |  | System Architecture |

| `Paragraph` | Times New Roman | 13.0pt |  |  | This image illustrates the core workflow of firmwa |


---


## 📝 NỘI DUNG GỐC (Giữ nguyên để AI học format)


VIETNAM GENERAL CONFEDERATION OF LABOR


# TON DUC THANG UNIVERSITY



# DEPARTMENT OF ELECTRICAL AND ELECTRONICS ENGINEERING



# NGUYEN HUY THAI NGUYEN



# AUTONOMOUS VEHICLE CONTROL (AMR) SYSTEM INTEGRATING ROS2, ESP32, AND A MULTI-PLATFORM MANAGEMENT INTERFACE



# ADVANCED SPECIALIZED PROJECT



# CONTROL AND AUTOMATION TECHNOLOGY



# HO CHI MINH CITY, YEAR 2026


VIETNAM GENERAL CONFEDERATION OF LABOR


# TON DUC THANG UNIVERSITY



# DEPARTMENT OF ELECTRICAL AND ELECTRONICS ENGINEERING



# NGUYEN HUY THAI NGUYEN



# AUTONOMOUS VEHICLE CONTROL (AMR) SYSTEM INTEGRATING ROS2, ESP32, AND A MULTI-PLATFORM MANAGEMENT INTERFACE



# ADVANCED SPECIALIZED PROJECT



# CONTROL AND AUTOMATION TECHNOLOGY


Advisor


## Dr. Vu Tri Vien



# HO CHI MINH CITY, YEAR 2026



# AUTONOMOUS VEHICLE CONTROL (AMR) SYSTEM INTEGRATING ROS2, ESP32, AND A MULTI-PLATFORM MANAGEMENT INTERFACE



# ABSTRACT


There are four main areas we need to focus on when researching and working on a project related to this topic:

**1. Three-Layer Control Architecture with ROS2 and Micro-ROS:**

This is the "brain" of AMR. Instead of using older protocols (like simple UART/Serial), the use of micro-ROS on the ESP32-S3 allows the robot to operate as a unified entity.

High Layer (ROS2 Humble/Foxy): Handles resource-intensive algorithms. The SLAM Toolbox helps build dynamic maps better than the old G mapping, while Nav2 handles path planning and obstacle avoidance.

Low Layer (ESP32-S3): Acts as a true ROS Node. Thanks to micro-ROS, data from sensors (IMU, Encoder) is packaged into Topics and Transforms (TFs) and sent directly to the embedded computer (Pi4 or Jetson) without the need for complex converters.

**Benefits: Reduced system latency and increased data synchronization (Timestamping).
2. Virtual Axle Algorithm (Electronic Sync Lock):**

This is a technical highlight in your report. In AMR robots using independent DC motors, mechanical error or differences between the two motors often cause the robot to deviate from its straight-line trajectory.

Mechanism: Instead of using individual PID controllers for each wheel, the Virtual Axle creates a common "virtual axis." It monitors the position difference between the two wheels (Differential Error) in real time.

Operation: If the left wheel is faster than the right wheel, the system will automatically compensate or decelerate the left wheel immediately to maintain perfect synchronization, as if the two wheels were connected by a rigid mechanical axle.

**3. Optimize recovery with Feedforward:**

Integrating Feedforward into the motor control system demonstrates a deep understanding of drive systems.

Technical depth: Traditional PID controllers always have a delay (an error is necessary for a response). Feedforward (FF) allows the system to "anticipate" by immediately providing a base voltage level based on the target velocity. In your code, this combination reduces the burden on the PID's Integral, enabling the robot to react instantaneously to the cmd_vel command from SLAM/Nav2, especially during sharp turns or when starting to move.

**4. Cross-platform management with Electron & Web Workers**

Your Electron/React interface addresses the real-time monitoring problem.

Technical depth: Odometry calculations (from encoder pulses to X, Y, and Theta coordinates) require continuous real-time computation. If performed on the main Javascript thread, the interface will freeze when the robot moves quickly. Separating this logic into Web Workers leverages the multi-core CPU of the computer, ensuring that the data stream from the robot is processed in parallel with the rendering of the 2D/3D map on the user interface.


# OVERVIEW OF THE TOPIC



## Topic Introduction


In the era of Industry 4.0, the shift from AGVs (Automated Guided Vehicles) to AMRs (Autonomous Mobile Robots) represents a significant leap forward in artificial intelligence and adaptability. AMRs no longer rely on fixed magnetic tracks but utilize spatial data for self-positioning and path planning. Integrating ROS2 (Next-Generation Robotic Operating System) and ESP32 provides an optimal solution in terms of cost and performance. ROS2 offers powerful distributed processing capabilities, while the ESP32-S3, with its dual-core architecture, handles real-time hardware control via the micro-ROS protocol, eliminating unnecessary intermediate layers and reducing system latency.

Develop a complete AMR system capable of:

● Automatically constructing an Occupancy Grid Map.

● Locating and navigating to avoid dynamic obstacles with an accuracy of less than 5cm.

● Providing a multi-platform telemetry monitoring and centralized control interface.


## Research subjects and scope


● Model: Differential Drive Robot (2 drive wheels, 1 free wheel).

● Hardware: ESP32-S3 microcontroller, RPLidar A1M8 LiDAR, 12V DC motor encoder.

In the overall structure of the Automated Maneuvering Robot (AMR) system, the hardware components play a core role in collecting environmental data and executing control commands. Specifically, the system utilizes three main components: the ESP32-S3 microcontroller, the RPLidar A1M8 sensor, and a 12V DC motor with integrated encoding. Each component ensures a specialized function, with a tightly integrated and logical distribution to guarantee the robot's autonomous operation.

First, the ESP32-S3 microcontroller acts as a low-level controller, serving as a communication bridge between the ROS2 central processing unit (high-level) and the hardware actuators. In terms of control, the ESP32-S3 receives speed commands (via cmd_vel messages) from the ROS2, performs PID algorithm calculations, and outputs PWM/Direction signals to the power circuit (Motor Driver) to control the wheel to maintain the required speed. Simultaneously, the microcontroller collects feedback data by reading pulse signals from the encoder, thereby determining the actual speed and rotational speed of the wheel. In particular, thanks to its powerful integrated Wi-Fi module, the ESP32-S3 is an ideal platform for deploying a micro-ROS ecosystem, allowing for the packaging of sensor data sent to ROS2 and the stable receipt of real-time control commands.

*Figure 1: ESP32-S3 Microcontroller*

To meet the requirements for environmental perception (Perception), the system is equipped with the RPLidar A1M8 sensor. This LiDAR sensor provides 360-degree 2D panoramic scanning with a maximum range of up to 12 meters. In the ROS2 ecosystem, point cloud data collected from this sensor is essential input for autonomous navigation. Specifically, when the robot moves into a new environment, the SLAM algorithm uses the Lidar scan data to create a 2D spatial map (Mapping). Based on the saved map, the system applies the AMCL algorithm to compare real-time Lidar data, thereby accurately determining the robot's current coordinates (Localization). Furthermore, Lidar greatly assists the navigation subsystem (Nav2) in obstacle avoidance, helping the robot automatically recalculate a safe trajectory when encountering static or dynamic obstacles.

*Figure 2: RPLidar A1M8 LiDAR*

Finally, the actuator that generates the movement for the entire system is a 12V DC motor assembly with an integrated rotary encoder. The use of a standard 12V motor allows for easy integration with common power circuits (such as L298N, BTS7960). The encoder is the crucial component for autonomous operation. When the wheels move, this component generates a series of electrical pulses for the ESP32 microcontroller to read and calculate the odometry (Odom) parameter. The odometry provides ROS2 with vital kinematic data, accurately reflecting the translational distance and rotation angle of the robot in space. All of ROS2's navigation algorithms depend heavily on this data; therefore, the encoder ensures the system is always aware of its actual movement state.

*Figure 3: 12V-DC motor encode*

● Software: Ubuntu 22.04, ROS2 Humble, Electron framework:

Ubuntu 22.04 LTS (codename Jammy Jellyfish) is a Linux-based operating system developed by Canonical. It is a Long Term Support (LTS) version, extremely popular in the programming and robotics research community.

*Figure 4: Ubuntu 22.04*

ROS2 Humble Hawksbill and this is currently the most important distribution version of Robot Operating System 2, released in May 2022. It's an LTS (Long Term Support) version, meaning it receives continuous security updates and bug fixes for 5 years (until 2027), making it extremely suitable for long-term research projects and industrial products like your AMR.

*Figure 5: ROS2 Humble*

Electron is an open-source framework that allows you to build desktop applications using standard web technologies like HTML, CSS, and JavaScript. Instead of having to learn specialized languages ​​for each operating system (like Swift for macOS or C# for Windows), you can use your web programming skills to create an application that runs on all three platforms: Windows, macOS, and Linux.

*Figure 6: Electron framework*


## The three-layer architectural approach


The system is highly modularized to ensure stand-alone functionality and easy upgrades:

1. High-level Control Layer: Runs on the SBC or host computer. Handles "heavy-duty" algorithms such as SLAM Toolbox (Karto/Graph-based) and Nav2.

2. Interface Layer: Desktop applications (Electron + React) connect via WebSockets and ROS Bridge. This is where future "Off-board Navigation" will be implemented.

3. Low-level Control Layer: ESP32 firmware handles high-frequency (>1kHz) encoder interrupts, calculates PID, and performs Virtual Axle algorithms.


# THEORETICAL FOUNDATIONS AND TECHNICAL STANDARDS



## Robotics Dynamics (Kinematics)


The system uses a Differential Drive model. The robot's position is represented by a state vector  .

Forward Kinematics: Calculate robot velocity (v, ω) from left wheel speed (vL) and right wheel speed (vR): Where R is the wheel radius and L is the distance between the two wheels.

Inverse Kinematics: Nav2 will send the command (v, ω), ESP32 needs to reverse-engineer to find the target velocity for each wheel:

Update the position using Euler's integral in each time interval Δt:


## Advanced control algorithm: Virtual Axle


The system uses a Differential Drive model. The robot's position is represented by a state vector q = [x, y, θ].

Forward Kinematics: Calculate robot velocity (v, ω) from left wheel speed (vL) and right wheel speed (vR):

v = () * (vR + vL) ω = () * (vR - vL)

Where R is the radius of the wheel and L is the distance between the two wheels..

Inverse Kinematics: Nav2 will send the command (v, ω), ESP32 needs to reverse-engineer to find the target velocity for each wheel:

vL = (2v - ω * L) / (2R) vR = (2v + ω * L) / (2R)

Update the position using Euler's integral in each time interval Δt:

x(t+1) = x(t) + v * cos(θ) * Δt y(t+1) = y(t) + v * sin(θ) * Δt θ(t+1) = θ(t) + ω * Δt


## Navigation and SLAM systems


SLAM Toolbox: To perform environmental mapping, the system utilizes the it suite on the ROS2 platform. The core advantage of this algorithm lies in its use of pose-graph optimization. By efficiently processing and optimizing loop closures, the algorithm effectively eliminates cumulative measurement errors (drift) generated during robot movement. Thanks to this mechanism, SLAM Toolbox allows the system to construct highly accurate spatial grid maps (Occupancy Grid Maps) while maintaining stability and reliability even when deploying mapping in large-scale environments.

*Figure 7: SLAM Toolbox*

Nav2 Costmaps: Regarding the autonomous navigation subsystem, the application system uses the Nav2 architecture on the ROS2 platform, with the Costmaps system at its core. To optimize processing performance, the Costmap system is hierarchically structured into two parallel layers: Global Costmap and Local Costmap. Global Costmap uses static map data (from SLAM) to allow the Global Planner to plot the overall movement trajectory from the starting point to the target. Conversely, Local Costmap continuously updates point cloud data in real time from LiDAR sensors to identify and process dynamic obstacles or instantaneous obstructions appearing within a narrow range. To execute movement, the system uses the DWA (Dynamic Window Approach) algorithm as the local controller. The DWA algorithm will continuously simulate, calculate, and evaluate to select the optimal velocity vector (including translational and angular velocity) within the allowed velocity space, thereby controlling the robot to move smoothly, safely avoid obstacles, and closely follow the planned trajectory.

*Figure 8: Nav2 Costmaps*


## Communication Protocol and Latency Analysis


WebSockets: To ensure real-time monitoring and transmission of telemetry data between the AMR robot and the multi-platform management interface, the system utilizes the WebSockets protocol as the core communication solution. In network communication techniques, the traditional HTTP protocol operates on a stateless model with a Request-Response cycle, accompanied by a large amount of header overhead, thus failing to meet the latency requirements for robot control. In contrast to that architecture, WebSockets establishes and maintains a continuous and robust full-duplex connection between the client and the server. Within the scope of this project, the superior bandwidth advantage of WebSockets allows the system to transmit point cloud data streams from LiDAR sensors at high density, reaching 180 data points per packet. In particular, this transmission process maintains an extremely ideal network latency of less than 10ms. This performance is crucial, enabling the management interface to accurately update the environment status in real time, thereby ensuring smooth and absolutely secure remote monitoring.

*Figure 9: WebSockets*

ROS Bridge: To address the communication challenges between the ROS2 core control system and the multi-platform management interface, the integrated ROS Bridge toolkit is implemented. In the network architecture, ROS Bridge acts as a protocol transpiler, responsible for bidirectional conversion between the standard JSON data format of the web environment and the message structure specific to the ROS ecosystem. This mechanism establishes a seamless communication channel, allowing web- or desktop-based management applications to publish commands and subscribe directly to robot topics in real time. The breakthrough advantage of this solution is its complete environmental isolation: it frees the client side from stringent technical constraints. Thanks to this, users can comprehensively monitor and control autonomous robots through a regular web browser without having to install a Linux operating system or configure a complex ROS ecosystem on their personal devices.

*Figure 10: ROS Bridge*


# HARDWARE SYSTEM DESIGN AND CONSTRUCTION



## Block Diagrams and Resource Management



### System Architecture


This diagram illustrates the overall architecture of the AMR system, describing the tight bidirectional communication flow between the three main blocks: Robot Hardware, ESP32 Central Processing Unit, and Client App Control Interface. Specifically, it shows how the ESP32 collects hardware data (from the MPU6050, Encoder) for internal PID processing, while continuously transmitting kinematic data (30Hz Telemetry) via WebSocket to the React/Tauri application for monitoring and receiving navigation commands.

*Figure 11: System Architecture*


### Dynamics and Control Config (PID) Loop Diagram


Sensor Preprocessing and Forward Kinematics: The flowchart describes the process of initiating the control loop at 50Hz, performing parallel reading and processing of data from the encoder and the MPU6050 sensor. Here, the system calculates the actual velocity of each wheel to infer the overall velocity through the forward kinematics model, and simultaneously filters out Gyro signal noise to prepare for the data merging step.

*Figure 12: PID Control Dynamics & Loop Diagram*

Data Merging and Coordination: This phase focuses on the Complementary Filter algorithm to merge data from the sensors, enabling accurate real-time updating of odometry coordinates (X, Y, ). After determining the position, the system performs logical routing to select the target velocity source from the automatic navigation system (Navigator) or from manual control commands (Joystick).

*Figure 13: Data combination and traffic flow management*

Inverse Kinematics and Actuator Control: This stage implements an inverse kinematics algorithm to convert the robot's target velocity into the required speed for each wheel (vL, vR). The data is then processed through a PI controller with Feedforward static compensation to accurately calculate the PWM pulse and output a control signal to the L298N H-bridge circuit, completing a closed-loop control cycle.

*Figure 14: Inverse Kinematics and Actuator Control*


### Autonomous State Machine Diagram


This image is a State Machine diagram detailing the robot's Waypoint Navigation logic. The diagram clearly shows the basic movement cycle: from receiving the coordinate array, turning in place (NAV_TURNING), moving straight to the target (NAV_DRIVING), to the final adjustment of the rotation angle (NAV_FINAL_TURN). Importantly, the system always includes an emergency braking mechanism in all states to immediately return the robot to a safe standby mode (NAV_IDLE) in case of an incident.

*Figure 15: Navigator State Machine*


### Flowchart Logic for this system


This image illustrates the core workflow of firmware on a microcontroller, starting from hardware initialization (I2C, Interrupts), network connection (WiFi, OTA), and entering an infinite processing loop (Main Loop). The key technical aspect of this architecture is its ability to maintain parallel network tasks (WebSocket, HTTP) in close conjunction with a safety mechanism (Watchdog Timer): the system automatically reduces speed to zero and immediately shuts off the motor if control connection is lost for more than 1 second, ensuring the robot never loses control.

*Figure 16: Main Loop 1*

This flowchart details the time-based task scheduling mechanism within the microcontroller's main loop, using asynchronous (non-blocking) programming techniques. It allows the ESP32 to handle multiple workflows in parallel at different frequencies: prioritizing the PID control loop at a high frequency of 50Hz (every 20ms) to maintain motor smoothness, while assigning a 30Hz (every 33ms) cycle for encapsulating and transmitting Telemetry data (JSON Broadcast) to the application. This time-division structure, combined with a safety monitor (motor shutdown after 1 second of signal loss), helps the system thoroughly optimize hardware resources while ensuring absolute reliability.

*Figure 17: Main Loop 2*

This flowchart details the time-based task scheduling mechanism within the microcontroller's main loop, using asynchronous (non-blocking) programming techniques. It allows the ESP32 to handle multiple workflows in parallel at different frequencies: prioritizing the PID control loop at a high frequency of 50Hz (every 20ms) to maintain motor smoothness, while assigning a 30Hz (every 33ms) cycle for encapsulating and transmitting Telemetry data (JSON Broadcast) to the application. This time-division structure, combined with a safety monitor (motor shutdown after 1 second of signal loss), helps the system thoroughly optimize hardware resources while ensuring absolute reliability.

*Figure 18: Main Loop 3*


### Backend & Frontend Communication Sequence Diagram


This image is a sequence diagram illustrating the real-time communication flow via WebSocket protocol between the control application (Client) and the ESP32 microcontroller (Server). The diagram highlights two parallel operating mechanisms: a continuous loop (30Hz cycle) pushes kinematic data and battery status from the robot to the interface to update the 3D map; and the system is always ready to receive asynchronous events when the user issues navigation commands (sending a JSON string containing the trajectory) to activate the autonomous driving system.

*Figure 19: Sequence Diagram 1*

The next part of this sequence diagram clarifies the control command validation process and the high-priority emergency interrupt handling mechanism. After receiving the trajectory command, the ESP32 will send an acknowledgment (ACK) response to the App and automatically run an independent PID loop to track the path. In particular, the diagram emphasizes the E-STOP safety feature: in case of an incident, the emergency braking packet will immediately intervene, forcing the microcontroller to cancel the state machine and "lock" the PWM pulse to stop the robot instantly.

*Figure 20: Sequence Diagram 2*

The system uses a 12V LiPo battery. The power supply is split into two branches: a power branch (12V) for the L298N driver and a logic branch (5V/3.3V via Buck Converter) for the ESP32 and LiDAR to avoid electromagnetic interference during motor startup (Back-EMF).

*Figure 21: L298N driver*

*Table 3.1: Specifications of L298N driver*

*Table 3.2: Pinout of L298N driver*

*Figure 22: LiPo battery (Lithium Polymer)*

*Table 3.3: Specifications of LiPo Battery driver*


## Detailed wiring diagram (Hardware Revision 2.0)


The GPIO pinout diagram on the ESP32-S3 microcontroller has been recalculated and restructured to match the UART communication module of the LiDAR sensor and the motor/encoder control circuit.

The redesigned pinout is detailed in Table 1 below:

Hardware Design Evaluation:

A key refinement in this design scheme is the removal of GPIO pin 18 from controlling the Motor IN2 signal (of the left motor). Instead, this hardware resource is exclusively allocated to the LiDAR's UART signal. This adjustment aims to ensure the integrity of high-speed communication data from the LiDAR, eliminate crosstalk from the motor, and thereby enhance the reliability and accuracy of the environmental mapping data.


# SOFTWARE IMPLEMENTATION AND CONTROL ALGORITHMS



## Programming ESP32 Firmware (Low-level Control)



## The system's engineering programming philosophy focuses on optimizing management power and hardware resources. To ensure smooth robot movement and eliminate wheel slippage during sudden state changes, ramp speed control algorithms have been applied using the following method:



## v_current = v_current + sign(v_target - v_current) * a_max * Δt



## In that:



## v_current: The robot's current speed.



## v_target: Target velocity as required by the superior system (Nav2).



## a_max: Maximum allowable acceleration of a mechanical system.



## Δt: The sampling period of the system.



## Simultaneously, the PID controller in the source code has been upgraded with an anti-windup mechanism. This technique limits the accumulation of excessive error in the integral component, effectively preventing overshoot and helping the system quickly stabilize when the robot encounters large obstacles or when the motor load changes suddenly.



## ROS2 and TF Tree configuration


The robot's coordinate system (Transform Tree) is standardized according to the spatial conventions of ROS 2, including the following transformation sequences:

**Map => Dom: Represents the cumulative positional error (drift) of the system over time.**

**Odom => Base footprint: Estimate the robot's current position and orientation angle on the floor based on sensor data (Odometry).**

**Base link => Laser frame: Determine the distance and static angle of the LiDAR sensor relative to the robot's mechanical center.**

In addition, the operating parameters in the nav2_params.yaml configuration file have been optimally fine-tuned. Specifically, the controller_frequency parameter is set to 20.0 Hz to ensure that the local controller (Local Planner) continuously outputs velocity commands (cmd_vel), allowing the robot to respond smoothly to changes in the environment.


## Desktop Application (Electron and React)



## To maintain high performance, the application uses Web Workers.



## Why are Web Workers needed? JavaScript runs single-threaded. Dynamic calculations and processing thousands of LiDAR points per second can cause UI bottlenecks (main thread). Web Workers enable parallel calculations in the background, allowing Canvas/WebGL to render maps at a stable 60fps, providing a smooth control experience similar to industrial systems.



# EXPERIMENTAL RESULTS AND ANALYSIS



## SLAM Results and Navigation


Experiments in a 50m² lab environment showed that SLAM Toolbox generates maps with extremely low loop closure error. The robot was able to detect thin obstacles such as table legs thanks to the 5Hz scanning frequency of the LiDAR.


## Telemetry and PID Tuning Analysis


Based on real-time graphs from the Desktop App:

● Chattering: When Kp is too high, the motor makes a screeching sound and the robot shakes.

● Steady-state Error: When Ki is too low, the robot does not reach its target speed under heavy load.

● Virtual Axle Validation: When Virtual Axle is off, the robot deviates 10cm after every 2m of straight-line travel. When the algorithm is on, the error is reduced to <2cm.


## Troubleshooting


The problem of losing connection to the micro-ROS Agent is often due to the firewall on Ubuntu. The solution is to open port 8888 UDP: sudo ufw allow 8888/udp


## Actual image of the model


After soldering the components and sensors, we cut and fix the two pieces of PVC plastic together to form a box. We then insert the soldered circuit board and secure it to the body of the plastic box with a drill. This completes the model car, which is now ready to run.

*Figure 23: Complete model*


## Simulating a map in real life


This is a 3D simulation map that recreates the actual warehouse space. It includes shelving (Shelf 1-4), entry/exit gates, and charging stations:

*Figure 24: 3D panoramic view of the simulated warehouse*

At the front of the warehouse are facilities intended as a goods handling point, including 3 inlet gates, 3 outlet gates, and 1 faulty outlet gate. This is the terminal transfer station where AMR robots run to receive new goods or hand over goods for shipment.

*Figure 25: Front view of the 3D simulated warehouse*

This is an automated charging station system for the AMR system. A highlight of this area is the four charging stations arranged in a straight line. When the robot's battery is low (0%), it will automatically find one of the four empty charging stations.

*Figure 26: The back of the 3D simulated warehouse*


# CONCLUSION AND FUTURE DEVELOPMENT



## Conclude


The project successfully built a complete stand-alone AMR system. Mastering the 3-layer architecture and low-level control algorithms (Virtual Axle, PID) enabled the robot to operate stably, far surpassing typical toy models.


## Development direction: "Re-inventing ROS"


The project's next vision is to bring high-level navigation algorithms directly into desktop applications using Web Assembly (WASM).

● Goal: Run SLAM and Nav2 purely in a browser/Electron.

● Benefits: Eliminate dependence on Linux/WSL for end users, transforming the system into a true plug-and-play solution.

● AI Fusion: Integrate EKF Filter to incorporate additional data from the IMU, enhancing accuracy when the robot moves on slippery surfaces


---

## 📊 CÁC BẢNG


### Bảng 1


| Main control IC | L298N |

|---|---|

| Voltage supplied to the logic (Vss) | 5V to 35V DC |

| Logic current | 0mA - 36mA |

| Maximum power consumption | 25W |

| Input control signal voltage (IN1-IN4, ENA, ENB) | Low level: -0.3V ≤ Vin ≤ 1.5V High level: 2.3V ≤ Vin ≤ Vss |



### Bảng 2


| Foot | Features |

|---|---|

| VCC | Power Pin |

| GND | Ground Pin |

| OUT1 & OUT2 OUT3 & OUT4 | 2 poles of Motor A 2 poles of Motor B |

| ENA (Enable A) ENB (Enable B) | Control the speed of Motor A and B using a PWM signal. |



### Bảng 3


| Number of Cells | 3S |

|---|---|

| Nominal Voltage | 3.7V / 1 cell |

| Fully-charged voltage | 0mA - 36mA |

| Cut-off Voltage | 3.2V to 3.3V / 1 cell |

| Capacity (mAh/Ah) | 2200mAh to 5200mAh. |



### Bảng 4


| Accessory | ESP32-S3 Pin | Active function | Additional notes |

|---|---|---|---|

| LiDAR TX/RX | GPIO 18, 17 | UART1 | Communicating and transmitting data with the RPLidar A1M8. |

| LiDAR Motor | GPIO 16 | Output | Control the rotation motor of the LiDAR cluster. |

| Left Motor | GPIO 19, 5, 4 | PWM, IN1, IN2 | This corresponds to the signals supplied to ENA, IN1, and IN2 of the Motor Driver. |

| Motor Right | GPIO 27, 26, 25 | PWM, IN3, IN4 | This corresponds to the signals supplied to ENB, IN3, and IN4 of the Motor Driver. |

| Left Encoder | GPIO 32, 33 | Phase A, B | Reads the surroundings via interrupts. |

| Right Encoder | GPIO 34, 35 | Phase A, B | Input-only pin (only receives A/D input signals). |


