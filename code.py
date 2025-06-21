import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sun_radius = 1
sun_color = 'yellow'
moon_radius = 0.25
moon_color = 'lightgray'
earth_radius = 0.75
earth_color = 'blue'

earth_orbit_radius = 2
moon_orbit_radius = 0.5

earth_x = earth_orbit_radius
earth_y = 0
earth_z = 0

moon_x = earth_x + moon_orbit_radius
moon_y = earth_y
moon_z = earth_z

def update(frame):
    global earth_x, earth_y, moon_x, moon_y
    earth_angle = 2 * np.pi * frame / 100
    earth_x = earth_orbit_radius * np.cos(earth_angle)
    earth_y = earth_orbit_radius * np.sin(earth_angle)
    moon_angle = 2 * np.pi * frame / 100 * 2
    moon_x = earth_x + moon_orbit_radius * np.cos(moon_angle)
    moon_y = earth_y + moon_orbit_radius * np.sin(moon_angle)
    ax.clear()
    ax.scatter(0, 0, 0, color=sun_color, s=sun_radius * 500, label="Sun")
    ax.scatter(earth_x, earth_y, 0, color=earth_color, s=earth_radius * 100, label="Earth")
    ax.scatter(moon_x, moon_y, 0, color=moon_color, s=moon_radius * 50, label="Moon")
    ax.set_xlim(-earth_orbit_radius * 2, earth_orbit_radius * 2)
    ax.set_ylim(-earth_orbit_radius * 2, earth_orbit_radius * 2)
    ax.set_zlim(-earth_orbit_radius * 2, earth_orbit_radius * 2)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Sun-Moon Cycle")
    ax.legend()
    return ax

ani = FuncAnimation(fig, update, frames=100, blit=False)
ani.save('sun_moon_cycle.mp4', writer='ffmpeg', fps=24)
plt.show()
