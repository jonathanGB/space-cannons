import unittest
import numpy as np
import forces

# Test the Forces module
class ForcesTest(unittest.TestCase):
  G = 6.67408e-11

  # Test `dist`
  def test_dist1(self):
    p1, p2 = (0, 0), (5,0)

    self.assertEqual(forces.dist(p1[0], p1[1], p2[0], p2[1]), 5)

  def test_dist2(self):
    p1, p2 = (0, 0), (3,4)

    self.assertEqual(forces.dist(p1[0], p1[1], p2[0], p2[1]), 5)


  # Test `compute_gravitational_force`
  def test_compute_gravitational_force1(self):
    self.assertEqual(forces.compute_gravitational_force(1, 1, 1), ForcesTest.G)

  def test_compute_gravitational_force2(self):
    self.assertEqual(forces.compute_gravitational_force(1, 10, 2), ForcesTest.G * 10 / 4)


  # Test `get_x_and_y_components`
  def test_get_x_and_y_components1(self):
    self.assertEqual(forces.get_x_and_y_components(1, 5, 3, 4), (3/5, 4/5))

  def test_get_x_and_y_components2(self):
    approx_x_comp, approx_y_comp = 3.84615381934, 9.23076924194
    calculated_x_comp, calculated_y_comp = forces.get_x_and_y_components(10, 13, 5, 12)

    self.assertAlmostEqual(calculated_x_comp, approx_x_comp)
    self.assertAlmostEqual(calculated_y_comp, approx_y_comp)

  
  # Test `compute_forces`
  def test_compute_forces1(self):
    bodies = [
      {'x': 0, 'y': 0, 'm': 1},
      {'x': 1, 'y': 0, 'm': 1}
    ]

    output = forces.compute_forces(bodies)
    expected_output = np.array([
      [ForcesTest.G, 0],
      [-ForcesTest.G, 0]
    ])

    self.assertEqual(output.shape, expected_output.shape)

    for i in range(len(output)):
      for j in range(len(output[i])):
        self.assertEqual(output[i,j], expected_output[i,j])

  def test_compute_forces2(self):
    bodies = [
      {'x': 0, 'y': 0, 'm': 1},
      {'x': 1, 'y': 0, 'm': 1},
      {'x': -1, 'y': 0, 'm': 1}
    ]

    output = forces.compute_forces(bodies)
    expected_output = np.array([
      [0, 0],
      [-ForcesTest.G - ForcesTest.G/4, 0],
      [ForcesTest.G + ForcesTest.G/4, 0]
    ])

    self.assertEqual(output.shape, expected_output.shape)

    for i in range(len(output)):
      for j in range(len(output[i])):
        self.assertEqual(output[i,j], expected_output[i,j])

  def test_compute_forces3(self):
    bodies = [
      {'x': 0, 'y': 0, 'm': 1},
      {'x': 1, 'y': 0, 'm': 1},
      {'x': 0, 'y': -1, 'm': 1}
    ]

    output = forces.compute_forces(bodies)
    expected_output = np.array([
      [ForcesTest.G, -ForcesTest.G],
      [-ForcesTest.G - np.sqrt(2) * ForcesTest.G / 4, -np.sqrt(2) * ForcesTest.G/ 4],
      [np.sqrt(2) * ForcesTest.G/4, ForcesTest.G + np.sqrt(2) * ForcesTest.G/4]
    ])

    self.assertEqual(output.shape, expected_output.shape)

    for i in range(len(output)):
      for j in range(len(output[i])):
        self.assertAlmostEqual(output[i,j], expected_output[i,j])