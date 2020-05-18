# Task Description

Thank you for your interest in joining our journey. Your task is to build a point cloud web-based visualization using a WebGL library (e.g. Three.js)

### Data description
The data is stored in ```data``` folder (30 frames):
1. ```lidar```: pointcloud binary files. If you are using python numpy, you can open it using
```
import numpy as np
points = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)
```
The 4 channels are ```x, y, z, reflection_number```

2. ```label```: 3d bounding boxes information. Each line contains the info:
```
id;center_x;center_y;base_z;size_x;size_y;size_z;yaw_angle;object_class
```
   + Id is unique across the frames
   + center_x, center_y are x, y position of center of the box
   + base_z are the lowest z position of the box
   + size_x, size_y, size z are the sizes of the box
   + yaw angle is yaw angle of the boxes
   + Object classes: "CAR", "PED", "CYC", "SIGN"

### Tasks
You tasks is divided to 3 steps:

1. Build a web-based visualization which can visualize the point cloud frame by frame. The visualization should support:
   
   + Zoom (in, out), rotate, translate
   + 3 option for coloring the points. Based on height (z value of the point), distance or reflection number
   + Can navigate forward and backward between frames

2. Visualize point clouds together with the bounding boxes (in ```label``` folder) of ```CAR, PED, CYC```. ```CAR, PED, CYC`` boxes should have different colors.

3. Visualize the trail of each box of ```CAR, PED, CYC``` (the box id is unique across frames). The trail should have the same color with the box. The visualization method is up to your preference (line segments, dots, or whatever).

### Requirements
1. You should use a WebGL based library for this task. We recommend using Three.js.
2. We care a lot about the code quality. Please submit us a clear, well organized code package.
3. If you could make it Docker based, it should be a plus.


Please ***DO NOT*** share the data and the description of the task, we want to have a fair recruitment process.

Happy coding and have fun.
