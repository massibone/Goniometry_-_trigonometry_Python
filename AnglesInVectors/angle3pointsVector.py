import numpy as np

a = np.array([5,3])
b = np.array([3,5])
c = np.array([4,6])

ba = a - b
bc = c - b

cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
angle = np.arccos(cosine_angle)

print np.degrees(angle)
