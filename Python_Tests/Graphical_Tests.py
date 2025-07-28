import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Gitterparameter
x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
z = np.linspace(-1, 1, 20)
X, Y, Z = np.meshgrid(x, y, z)

# Darstellung als Punktwolke
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, color='red', s=4)  # s=2: Punktgröße

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Feingranulares 3D-Gitter')

plt.show()