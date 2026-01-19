import numpy as np
import matplotlib.pyplot as plt

# Angle range
theta = np.linspace(0, 2*np.pi, 1000)

# Rose curve function (flower shape)
k = 5  # number of petals (odd = k petals, even = 2k petals)
r = np.sin(k * theta)

# Convert polar to Cartesian
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot
plt.figure(figsize=(6,6))
plt.plot(x, y, color="magenta")
plt.axis("equal")
plt.title(f"Flower with {k} petals")
plt.show()