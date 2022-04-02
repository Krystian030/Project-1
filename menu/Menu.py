from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

INTERVAL = 50  # ms
HOLD_MS  = 1000
HOLD_COUNT = HOLD_MS // INTERVAL

def frame_generator():
    for frame in range(1, 251):
        # Yield the frame first
        yield frame
        # If we should "sleep" here, yield None HOLD_COUNT times
        if frame % 50 == 0:
            for _ in range(HOLD_COUNT):
                yield None


f, ax = plt.subplots()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

radius = 1
dp = 2*np.pi / 50
circles = [[(radius, 0)]]
plots = ax.plot([radius], [0])

def update(frame):
    global radius

    if frame is None: return   #--------------------------------- Added

    if frame % 50 == 0:
        radius += 1
        circles.append([(radius, 0)])
        plots.extend(ax.plot([radius], [0]))
        #-------------------------------------------------------- sleep removed

    angle = (frame % 50) * dp
    circles[-1].append((radius * np.cos(angle), radius * np.sin(angle)))
    plots[-1].set_data(*zip(*circles[-1]))
    return plots[-1]

# Slightly changed
animation = FuncAnimation(f, update, frames=frame_generator(), interval=INTERVAL, repeat=False)
plt.show()
