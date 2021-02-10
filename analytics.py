import matplotlib.pyplot as plt
import numpy as np

data = [['BFS', 0, 5], ['BFS', 0, 7], ['BFS', 0, 7], ['BFS', 0, 3], ['BFS', 0, 13], ['BFS', 0, 18], ['BFS', 0, 5], ['BFS', 0, 4], ['BFS', 0, 0], ['BFS', 0, 23], ['BFS', 0, 39], ['BFS', 0, 1], ['BFS', 0, 175], ['BFS', 0, 0], ['BFS', 0, 20], ['BFS', 0, 97], ['BFS', 0, 139], ['BFS', 0, 2], ['BFS', 0, 0], ['BFS', 0, 0], ['BFS', 0, 45], ['BFS', 0, 18], ['BFS', 38, 135], ['BFS', 0, 1], ['BFS', 0, 32], ['BFS', 0, 30], ['BFS', 0, 80], ['BFS', 42, 166], ['BFS', 0, 0], ['BFS', 0, 12], ['BFS', 0, 42], ['BFS', 0, 75], ['BFS', 46, 201], ['BFS', 0, 113], ['BFS', 0, 87], ['BFS', 0, 191], ['BFS', 0, 1], ['BFS', 0, 54], ['BFS', 0, 0], ['BFS', 0, 49], ['BFS', 0, 5], ['BFS', 0, 1], ['BFS', 0, 0], ['BFS', 0, 33], ['BFS', 0, 0], ['BFS', 0, 31], ['BFS', 0, 120], ['BFS', 0, 0], ['BFS', 0, 55], ['BFS', 0, 1], ['BFS', 0, 0], ['BFS', 0, 3], ['BFS', 0, 6], ['BFS', 0, 0], ['BFS', 0, 0], ['BFS', 0, 96], ['BFS', 0, 184], ['BFS', 0, 14], ['BFS', 0, 0], ['BFS', 0, 163], ['BFS', 0, 5], ['BFS', 0, 1], ['BFS', 0, 2], ['BFS', 0, 3], ['BFS', 0, 4], ['BFS', 0, 165], ['BFS', 0, 0], ['BFS', 0, 26], ['BFS', 0, 138], ['BFS', 0, 123], ['BFS', 0, 25], ['BFS', 0, 1], ['BFS', 0, 9], ['BFS', 0, 2], ['BFS', 0, 193], ['BFS', 0, 85], ['BFS', 42, 217], ['BFS', 0, 3], ['BFS', 0, 4], ['BFS', 0, 4]]

len = len(data)
prob = 0
for i in data:
    if i[1] != 0:
        prob += 1
print("{0:.0f}%".format(prob/len * 100))
print(len)

#Problem 1
prob_points = np.array([100, 100, 84, 60, 5, 0, 0, 0, 0, 0, 0])
p_points = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

plt.plot(p_points, prob_points, color="black")
#plt.plot(p_points, bfs_points, color="red")
plt.scatter(p_points, prob_points, color="black")
#plt.scatter(p_points, bfs_points, color="red")
plt.xlabel("Obstacle Density P")
plt.ylabel("Probability that S can be reached from G (%)")

#plt.show()
plt.savefig('img/image2.png')