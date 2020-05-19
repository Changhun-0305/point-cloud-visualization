import numpy as np
points = np.fromfile("data/lidar/0001.bin", dtype=np.float32).reshape(-1, 4)
print(points[0])