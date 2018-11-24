import json
import drawing

with open('configs/config.json') as f:
  bodies = json.load(f)

drawing.initial_draw(bodies)