pts = np.linspace(0, 4 * np.pi, 30)
x = np.sin(2 * pts)
y = np.cos(pts)
z = np.cos(2 * pts)
s = 2+np.sin(pts)
mlab.points3d(x, y, z)