import json
import drawing
import forces
import numpy as np

with open('configs/config.json') as f:
  bodies = np.array(json.load(f))

drawing.initial_draw(bodies)

print(bodies)

forces.compute_forces(bodies)