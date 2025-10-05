import numpy as np
import matplotlib.pyplot as plt

# Define line: r = (1,-1,0) + λ(1,5,1)
line_point = np.array([1, -1, 0])
line_dir = np.array([1, 5, 1])
λ = np.linspace(-2, 2, 100)
line = line_point[:, None] + line_dir[:, None] * λ

# Define plane: x - y + 4z = 5
xx, yy = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
zz = (5 - xx + yy) / 4

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot line
ax.plot(line[0], line[1], line[2], color='r', label='Line')

# Plot plane
ax.plot_surface(xx, yy, zz, alpha=0.5, edgecolor='k', linewidth=0.3)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Line and Plane in 3D")

# Add legend manually
line_proxy, = ax.plot([], [], [], color='r', label='Line')
ax.legend(handles=[line_proxy], loc='best')

plt.show()