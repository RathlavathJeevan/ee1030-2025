import numpy as np
import matplotlib.pyplot as plt

# Coordinates of triangle
A = np.array([6, 0])
B = np.array([0, 0])
C = np.array([0, 8])

# Function to get foot of perpendicular from point P to line (Q,R)
def foot_of_perpendicular(P, Q, R):
    PQ = P - Q
    QR = R - Q
    t = np.dot(PQ, QR) / np.dot(QR, QR)
    return Q + t * QR

# D is foot of perpendicular from B to AC
D = foot_of_perpendicular(B, A, C)

# Circle through B, C, D → circumcircle
def circle_from_3pts(p1, p2, p3):
    A = np.array([
        [p1[0], p1[1], 1],
        [p2[0], p2[1], 1],
        [p3[0], p3[1], 1]
    ])
    B = -np.array([
        [p1[0]**2 + p1[1]**2],
        [p2[0]**2 + p2[1]**2],
        [p3[0]**2 + p3[1]**2]
    ])
    coeffs = np.linalg.lstsq(A, B, rcond=None)[0].flatten()
    g, f, c = coeffs
    h, k = -g/2, -f/2
    r = np.sqrt(h**2 + k**2 - c)
    return (h, k, r)

h, k, r = circle_from_3pts(B, C, D)

# Generate circle points
theta = np.linspace(0, 2*np.pi, 400)
circle_x = h + r*np.cos(theta)
circle_y = k + r*np.sin(theta)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [0,0], 'b-')
ax.plot([B[0], C[0]], [B[1], C[1]], [0,0], 'b-')
ax.plot([C[0], A[0]], [C[1], A[1]], [0,0], 'b-')

# Perpendicular BD
ax.plot([B[0], D[0]], [B[1], D[1]], [0,0], 'g--')

# Circle through B, C, D
ax.plot(circle_x, circle_y, np.zeros_like(circle_x), 'r')

# Points
for P, name in zip([A,B,C,D], ["A","B","C","D"]):
    ax.scatter(P[0], P[1], 0, s=50)
    ax.text(P[0], P[1], 0.2, name, fontsize=10)

# Labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Graph of Triangle ABC with Circle ")

# Save as image
plt.savefig("triangle_3_3_10.png", dpi=300)
plt.show()