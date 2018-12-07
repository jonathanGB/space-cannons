import forces
import numpy as np
import matplotlib.pyplot as plt
# {
#   "x": x-coordinate (in meters)
#   "y": y-coordinate (in meters)
#   "r": radius of the body (in meters)
#   "m": mass of the body (in kg)
#   "atmos": { // optional
#     "p": density of the atmosphere (in kg/m^3)
#     "h": height of the atmosphere (in meters)
#   }
#   "vx": x-component of the velocity of the body (in m/s)
#   "vy": y-component of the velocity of the body (in m/s)
# }
# b1 = {
#     "x": 100,
#     "y": 200,
#     "r": 15,
#     "m": 1e6,
#     "vx": 0,
#     "vy": 1
# }
#
# b2 =  {
#     "x": 200,
#     "y": 200,
#     "r": 1,
#     "m": 10,
#     "vx": 5,
#     "vy": 3
# }


class StationaryParticle(object):
    def __init__(self, x, y, r, m):
        self.x = x
        self.y = y
        self.r = r
        self.m = m

    def get_pos(self):
        return np.array([self.x, self.y])

    def set_pos(self, x, y):
        return

    def get_vel(self):
        return np.array([0.0,0.0])

    def set_vel(self, new_vx, new_vy):
        return

    def get_acc(self):
        return np.array([0.0,0.0])

    def set_acc(self, new_ax, new_ay):
        return


class Particle(object):
    def __init__(self, x, y, r, m, vx, vy, ax = 0, ay = 0):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

    def get_pos(self):
        return np.array([self.x, self.y])

    def set_pos(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_vel(self):
        return np.array([self.vx, self.vy])

    def set_vel(self, new_vx, new_vy):
        self.vx = new_vx
        self.vy = new_vy

    def get_acc(self):
        return np.array([self.ax, self.ay])

    def set_acc(self, new_ax, new_ay):
        self.ax, self.ay = new_ax, new_ay


m1 = StationaryParticle(20, 20, 50, 1)
b1 = Particle(25, 25, 10, 10, -0.02, -0.01)
b2 = Particle(10, 20, 10, 5.2, -0.02, 0.01)
b3 = Particle(14, 14, 0.1, 10, -0.02, 0.01)
b4 = Particle(20, 14, 10, 100, 0.02, -0.01)
b5 = Particle(17, 10, 0.1, 10, 0.2, 0.01)


def pos(x0, y0, vx, vy, ax, ay, t):
    x_pos = 0.5*ax*t**2 + vx*t + x0
    y_pos = 0.5*ay*t**2 + vy*t + y0
    return np.array([[x_pos], [y_pos]])


def in_motion(bodies, t_list):
    positions = {}
    for t in t_list:
        fs = forces.compute_forces(bodies)
        for i, b in enumerate(bodies):
            ax, ay = b.get_acc()
            vx, vy = b.get_vel()
            bx, by = b.get_pos()

            b_pos = pos(bx, by, vx, vy, ax, ay, t).T
            if b in positions.keys():
                positions[b] = np.concatenate((positions[b], b_pos.T), axis=1)
            else:
                positions[b] = b_pos.T

            new_acc = fs[i]/b.m
            b.set_acc(new_acc[0], new_acc[1])
            b.set_vel(b.x - b_pos[0][0], b.y - b_pos[0][1])
            b.set_pos(b_pos[0][0], b_pos[0][1])


    plt.figure(figsize=(10,10))
    for b in positions.keys():
        p = positions[b]
        #plt.scatter(p[0][-1], p[1][-1], s=b.r)
        plt.plot(p[0], p[1], '--.')

    plt.show()

#print(forces.compute_forces([b1, b2]))
print(in_motion([m1, b5], np.linspace(0, 5.8, 10)))
# x_0, y_0 = 0, 0
# tt = np.linspace(0, 10, 40)
# vals = pos(x_0, y_0, -3, 2.4, -1, 0.25, tt)
# plt.plot(vals[0], vals[1])
# plt.show()