import matplotlib.pyplot as plt
from sys import exit

def __get_colour():
  while True:
    for colour in ['b', 'g', 'r', 'c', 'm', 'y', 'k']:
      yield colour


def initial_draw(bodies):
  random_colour = __get_colour()

  for body in bodies:
    x, y, r = body['x'], body['y'], body['r']
    body['drawing'] = {}

    if "atmos" in body:
      body['drawing']['atmos'] = plt.Circle((x, y), r, color='w', alpha=0.5)

      inner_r = r - body['atmos']['h']
      if inner_r <= 0:
        exit("One body has a bigger atmosphere ({}) than the radius of the body defined ({})".format(body['atmos']['h'], r))
      
      r = inner_r

    body['drawing']['body'] = plt.Circle((x, y), r, color=next(random_colour))

    for drawing in body['drawing']:
      plt.gca().add_patch(body['drawing'][drawing])

  plt.axis('scaled')
  plt.gca().set_facecolor((0,0,0))
  plt.show()