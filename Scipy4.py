import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()


points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()


from scipy.spatial.distance import euclidean

d1 = (10,2)
d2 = (4,6)

distance = euclidean(d1,d2)
print(distance)

from scipy.spatial.distance import cityblock
city = cityblock(d1,d2)
print(city)

from scipy.spatial.distance import cosine
cos = cosine(d1,d2)
print(cos)

from scipy.spatial.distance import hamming

p1 = (False, True, False)
p2 = (False, False, True)

res = hamming(p1, p2)

print(res)