# 📄 Template: Báo cáo -  BẢN CHÍNH.docm

> **Nguồn gốc:** `Báo cáo -  BẢN CHÍNH.docm`  

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

| `TOC TITLE` | Times New Roman | 16.0pt |  |  | CONTENTS |

| `toc 1` | — | —pt |  |  | DANH MỤC HÌNH VẼ	xii |

| `toc 2` | — | 11.0pt |  |  | 1.1	Về bố cục nội dung đồ án tốt nghiệp/tổng hợp	3 |

| `toc 3` | — | 11.0pt |  |  | 1.2.1	Soạn thảo văn bản	4 |

| `Heading 1` | — | —pt |  |  | DANH MỤC HÌNH VẼ |

| `Heading 2` | — | —pt |  |  | Topic Introduction |

| `Normal (Web)` | — | —pt |  |  | The system uses a Differential Drive model. The ro |

| `List Paragraph` | — | 12.0pt |  |  | SLAM Toolbox: Utilizes the SLAM Pose-graph mechani |

| `Appendix` | — | —pt |  |  | MÃ NGUỒN MATLAB |


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



# ACKNOWLEDMENT


First of all, I would like to express my sincere gratitude to my instructor, Mr. Vu Tri Vien, who has supported me throughout the process of researching and completing this project. I am deeply thankful for the time, attention, and dedicated guidance that he has given me.

Along with my deepest appreciation, I would also like to thank you for imparting valuable knowledge during his lectures and throughout the subjects he taught. Thanks to his guidance, I was able to complete this embedded systems project thoroughly and smoothly.

I sincerely thank you!

*Ho Chi Minh city, ngày   tháng   năm 2026*

*Author*


# DECLARATION OF AUTHORSHIP


I hereby declare that this thesis was carried out by myself under the guidance and supervision of Dr. Vu Tri Vien; and that the work and the results contained in it are original and have not been submitted anywhere for any previous purposes. The data and figures presented in this thesis are for analysis, comments, and evaluations from various resources by my own work and have been duly acknowledged in the reference part.

In addition, other comments, reviews and data used by other authors, and organizations have been acknowledged, and explicitly cited.

**I will take full responsibility for any fraud detected in my thesis. Ton Duc Thang University is unrelated to any copyright infringement caused on my work (if any).**

*Ho Chi Minh, ngày   tháng   năm 2026*

*Nguyen Huy Thai Nguyen*

SCHEDULE FOR ADVANCED SPECIALIZED PROJECTS

Project title: Autonomous vehicle control (amr) system integrating ros2, esp32, and a multi-platform management interface.

Student's full name:

Class: 22H40302                         ID: 422H


# AUTONOMOUS VEHICLE CONTROL (AMR) SYSTEM INTEGRATING ROS2, ESP32, AND A MULTI-PLATFORM MANAGEMENT INTERFACE



# ABSTRACT


This report details the design, construction, and in-depth analysis of an Autonomous Mobile Robot (AMR) system utilizing a modern three-tier architecture. The system leverages ROS2 as the high-level controller for SLAM Toolbox and intelligent navigation (Nav2). The low-level control layer is implemented on an ESP32-S3 microcontroller, integrating micro-ROS and advanced closed-loop control (PID) algorithms. Key technical innovations include the implementation of the Virtual Axle (Electronic Sync Lock) algorithm to eliminate mechanical steering deviations and a Feedforward mechanism to optimize motor dynamic response. A multi-platform management interface developed with Electron and React incorporates Web Workers for parallel Odometry computation, ensuring 60fps UI performance. Experimental results confirm the system's ability for high-resolution mapping and stable navigation in dynamic environments.

CONTENTS

DANH MỤC HÌNH VẼ	xii

DANH MỤC BẢNG BIỂU	xiii

DANH MỤC CÁC CHỮ VIẾT TẮT	xiv

CHƯƠNG 1.	HƯỚNG DẪN TRÌNH BÀY DATN/ DATH	1

1.1	Về bố cục nội dung đồ án tốt nghiệp/tổng hợp	3

1.2	Về cách trình bày khóa luận, đồ án tốt nghiệp	4

1.2.1	Soạn thảo văn bản	4

1.2.2	Tiểu mục	4

1.2.3	Bảng biểu, hình vẽ, phương trình	5

1.2.4	Viết tắt	6

1.2.5	Tài liệu tham khảo và cách trích dẫn	7

1.2.6	Cách trình bày Danh mục tài liệu tham khảo	8

1.2.7	Phụ lục	14

1.3	Về hình thức toàn bộ quyển khóa luận/đồ án	14

1.4	Hướng dẫn đóng bìa, ghi đĩa CD	15

1.4.1	Đóng bìa simili và in chữ nhũ vàng	15

1.4.2	Nội dung Khóa luận/Đồ án trong Thư mực/Đĩa CD	15

CHƯƠNG 2.	GIỚI THIỆU ĐỀ TÀI	17

2.1	Mục đích thực hiện đề tài	17

2.2	Yêu cầu của đề tài	18

2.3	Ý tưởng và phương pháp thực hiện	20

CHƯƠNG 3.	MIMO (LÝ THUYẾT LIÊN QUAN)	21

3.1	Nội dung 1	21

3.2	Nội dung 2	21

3.2.1	Nguyên lý thứ nhất	21

3.2.2	Nguyên lý thứ hai	21

3.2.3	Nguyên lý thứ ba	21

CHƯƠNG 4.	GIẢI PHÁP THỰC HIỆN	22

4.1	Mô hình mô phỏng	22

4.2	Kết quả mô phỏng	22

CHƯƠNG 5.	KẾT QUẢ MÔ PHỎNG (HOẶC KẾT QUẢ THI CÔNG MÔ HÌNH)	23

5.1	Kết quả 1	23

CHƯƠNG 6.	KẾT LUẬN	24

6.1	Kết luận	24

6.1.1	Kết luận 1	24

6.1.2	Kết luận 2	24

6.1.3	Kết luận 3	24

6.2	Hướng phát triển	24

TÀI LIỆU THAM KHẢO	25

PHỤ LỤC A	MÃ NGUỒN MATLAB	1


# DANH MỤC HÌNH VẼ


Hình 1-1. Chọn Style thích hợp	1

Hình 1-2. Chọn Style “Normal” cho nội dung DATN	1

Hình 1-1. Copy/paste text từ nguồn khác	2

Hình 1-2. Insert Caption	2

Hình 1-3. Hộp thoại Insert Caption	3

Hình 1-3. Mạch khuếch đại	19


# DANH MỤC BẢNG BIỂU


Bảng 1-1: Ví dụ	5


# DANH MỤC CÁC CHỮ VIẾT TẮT


BDT			Broadband Digital Terminal

AMR 			Autonomous Mobile Robot

ROS2  		Robot Operating System 2 (Humble/Iron)

SLAM  		Simultaneous Localization and Mapping

PID  			Proportional-Integral-Derivative

EKF  			Extended Kalman Filter

WASM  		Web Assembly

DWA  		Dynamic Window Approach

URDF  		Unified Robot Description Format

ODR  			Output Data Register (GPIO)


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

● Software: ROS2 Humble, Ubuntu 22.04, Electron framework


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


- SLAM Toolbox: Utilizes the SLAM Pose-graph mechanism, optimizing loop closures to build accurate Occupancy Grid Maps even in large environments.

- Nav2 Costmaps: Divided into Global Costmap (overall path) and Local Costmap (instantaneous obstacles). The DWA (Dynamic Window Approach) algorithm is used to select the optimal velocity vector to closely follow the trajectory.


## Communication Protocol and Latency Analysis


WebSockets: Used for telemetry. Unlike HTTP (which has a high overhead), WebSockets maintain a robust full-duplex connection, allowing the transmission of 180 LiDAR points/packets with a latency of <10ms.

ROS Bridge: Acts as a JSON-ROS transpiler, allowing web/desktop applications to interact directly with topics without needing to install a complex Linux environment.


# HARDWARE SYSTEM DESIGN AND CONSTRUCTION



## Block Diagrams and Resource Management


The system uses a 12V Li-ion battery. The power supply is split into two branches: a power branch (12V) for the L298N driver and a logic branch (5V/3.3V via Buck Converter) for the ESP32 and LiDAR to avoid electromagnetic interference during motor startup (Back-EMF).


## Detailed wiring diagram (Hardware Revision 2.0)


- The GPIO pinout diagram on the ESP32-S3 microcontroller has been recalculated and restructured to match the UART communication module of the LiDAR sensor and the motor/encoder control circuit.

The redesigned pinout is detailed in Table 1 below:

- Hardware Design Evaluation:

A key refinement in this design scheme is the removal of GPIO pin 18 from controlling the Motor IN2 signal (of the left motor). Instead, this hardware resource is exclusively allocated to the LiDAR's UART signal. This adjustment aims to ensure the integrity of high-speed communication data from the LiDAR, eliminate crosstalk from the motor, and thereby enhance the reliability and accuracy of the environmental mapping data.


# SOFTWARE IMPLEMENTATION AND CONTROL ALGORITHMS



## Programming ESP32 Firmware (Low-level Control)



## Tư duy lập trình kỹ thuật của hệ thống tập trung mạnh vào việc quản lý và tối ưu hóa tài nguyên phần cứng. Để đảm bảo robot di chuyển mượt mà và triệt tiêu hiện tượng trượt bánh (wheel slip) khi thay đổi trạng thái đột ngột, thuật toán điều khiển tốc độ dạng dốc (Ramp Speed Control) đã được áp dụng với phương trình:



## v_current = v_current + sign(v_target - v_current) * a_max * Δt



## Trong đó:



## v_current: Vận tốc hiện tại của robot.



## v_target: Vận tốc mục tiêu do hệ thống cấp trên (Nav2) yêu cầu.



## a_max: Gia tốc tối đa cho phép của hệ cơ khí.



## Δt: Chu kỳ thời gian lấy mẫu của hệ thống.



## Đồng thời, bộ điều khiển PID trong mã nguồn cũng được nâng cấp với cơ chế chống bão hòa tích phân (Anti-windup). Kỹ thuật này đóng vai trò giới hạn sự tích lũy sai số quá mức của thành phần I (Integral), từ đó ngăn chặn hiệu quả hiện tượng vọt lố (overshoot) và giúp hệ thống nhanh chóng ổn định lại khi robot phải đối mặt với vật cản lớn hoặc khi tải trọng động cơ bị thay đổi đột ngột.



## ROS2 and TF Tree configuration


Hệ thống tọa độ (Transform Tree) của robot được thiết lập chuẩn mực theo quy ước không gian của ROS 2, bao gồm các chuỗi biến đổi (transform) sau:

**Map => Dom: Biểu diễn mức độ sai số định vị tích lũy (drift) của hệ thống theo thời gian.**

**Odom => Base footprint: Ước lượng vị trí và góc hướng hiện tại của robot trên mặt sàn dựa vào dữ liệu cảm biến đo lường (Odometry).**

**Base link => Laser frame: Xác định khoảng cách và góc lệch tĩnh của cảm biến LiDAR tương đối so với tâm cơ học của robot.**

Bên cạnh đó, các tham số vận hành trong tệp cấu hình nav2_params.yaml cũng được tinh chỉnh một cách tối ưu. Cụ thể, thông số controller_frequency được đặt ở mức 20.0 Hz nhằm đảm bảo bộ điều khiển cục bộ (Local Planner) xuất các lệnh vận tốc (cmd_vel) một cách liên tục, giúp robot phản hồi mượt mà với những thay đổi của môi trường.


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


# CONCLUSION AND FUTURE DEVELOPMENT



## Conclude


The project successfully built a complete stand-alone AMR system. Mastering the 3-layer architecture and low-level control algorithms (Virtual Axle, PID) enabled the robot to operate stably, far surpassing typical toy models.


## Development direction: "Re-inventing ROS"


The project's next vision is to bring high-level navigation algorithms directly into desktop applications using Web Assembly (WASM).

● Goal: Run SLAM and Nav2 purely in a browser/Electron.

● Benefits: Eliminate dependence on Linux/WSL for end users, transforming the system into a true plug-and-play solution.

● AI Fusion: Integrate EKF Filter to incorporate additional data from the IMU, enhancing accuracy when the robot moves on slippery surfaces.


# TÀI LIỆU THAM KHẢO


*Macenski, S., et al. (2021). "SLAM Toolbox for Real-Time Simultaneous Localization and Mapping".  Journal of Open Source Software .*

*Open Robotics. (2023).  ROS 2 Documentation: Humble Hawksbill .*

*Espressif Systems. (2023).  ESP-IDF Programming Guide .*

Source Code: github.com/newbie1920/AMR (Dữ liệu thực nghiệm & Thuật toán Virtual Axle).

MÃ NGUỒN MATLAB

// Cấu trúc PID với giới hạn Anti-windup

struct PID {

float Kp, Ki, Kd;

float integral, prev_error;

float limit;

float update(float target, float current, float dt) {

float error = target - current;

integral += error * dt;

// Anti-windup logic

if (integral > limit) integral = limit;

if (integral < -limit) integral = -limit;

float derivative = (error - prev_error) / dt;

prev_error = error;

return (Kp * error) + (Ki * integral) + (Kd * derivative);

}

};

// Thuật toán Virtual Axle (Khóa đồng bộ ảo)

void applyVirtualAxle(long left_ticks, long right_ticks, int &pwm_l, int &pwm_r) {

long diff = left_ticks - right_ticks;

float k_sync = 1.5; // Hệ số đồng bộ

pwm_l -= (int)(diff * k_sync);

pwm_r += (int)(diff * k_sync);

}


---

## 📊 CÁC BẢNG


### Bảng 1


| TON DUC THANG UNIVERSITY FACULTY OF ELECTRICAL & ELECTRONICS ENGINEERING ------------------ | SOCIALIST REPUBLIC OF VIETNAM Independence – Freedom – Happiness --------------------- |

|---|---|



### Bảng 2


| Week/Day | Workload | Workload | Instructor signed |

|---|---|---|---|

| Week/Day | Done | Keep doing it | Instructor signed |

| Week 1 |  |  |  |

| Week 2 |  |  |  |

| Week 3 |  |  |  |

| Week 4 |  |  |  |

| Week 5 |  |  |  |

| Week 6 |  |  |  |

| Week 7 |  |  |  |

| Midterm exam | Evaluate completed volume ……..%                             	continue/discontinue embedded project | Evaluate completed volume ……..%                             	continue/discontinue embedded project | Evaluate completed volume ……..%                             	continue/discontinue embedded project |

| Week 8 |  |  |  |

| Week 9 |  |  |  |

| Week 10 |  |  |  |

| Week 11 |  |  |  |

| Week 12 |  |  |  |

| Submit Embedded System Project | Completed ……..% Embedded Projects Protected/Unprotected Embedded Projects | Completed ……..% Embedded Projects Protected/Unprotected Embedded Projects | Completed ……..% Embedded Projects Protected/Unprotected Embedded Projects |



### Bảng 3


| Accessory | ESP32-S3 Pin | Active function | Additional notes |

|---|---|---|---|

| LiDAR TX/RX | GPIO 18, 17 | UART1 | Communicating and transmitting data with the RPLidar A1M8. |

| LiDAR Motor | GPIO 16 | Output | Control the rotation motor of the LiDAR cluster. |

| Left Motor | GPIO 19, 5, 4 | PWM, IN1, IN2 | This corresponds to the signals supplied to ENA, IN1, and IN2 of the Motor Driver. |

| Motor Right | GPIO 27, 26, 25 | PWM, IN3, IN4 | This corresponds to the signals supplied to ENB, IN3, and IN4 of the Motor Driver. |

| Left Encoder | GPIO 32, 33 | Phase A, B | Reads the surroundings via interrupts. |

| Right Encoder | GPIO 34, 35 | Phase A, B | Input-only pin (only receives A/D input signals). |


