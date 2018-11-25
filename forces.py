import numpy as np

def dist(x1, y1, x2, y2):
  return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def compute_gravitational_force(m1, m2, r):
  G = 6.67408e-11
  return G * m1 * m2 / r**2

def get_x_and_y_components(f, r, deltax, deltay):
  cos_theta, sin_theta = deltax / r, deltay / r
  fx, fy = f * cos_theta, f * sin_theta

  return fx, fy

def compute_forces(bodies):
  N = len(bodies)

  g_forces = np.zeros((N, 2)) # x and y dimensions of the forces on each body

  for i in range(N-1):
    for j in range(i+1, N):
      body1, body2 = bodies[i], bodies[j]
      r = dist(body1['x'], body1['y'], body2['x'], body2['y'])
      fg = compute_gravitational_force(body1['m'], body2['m'], r)
      x_comp, y_comp = get_x_and_y_components(fg, r, body2['x'] - body1['x'], body2['y'] - body1['y'])

      g_forces[i,0] += x_comp
      g_forces[i,1] += y_comp
      # notice that we substract for the 2nd body, because the components are in the opposite direction of what
      # they are for the 1st body
      g_forces[j,0] -= x_comp
      g_forces[j,1] -= y_comp

  return g_forces

