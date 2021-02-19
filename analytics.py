import matplotlib.pyplot as plt
import numpy as np


'''
p=0 :: [['Astar', 98, 2499], ['BFS', 98, 2500]]
p=.1 :: [['Astar', 98, 2202], ['BFS', 98, 2250], ['Astar', 98, 2197], ['BFS', 98, 2249], ['Astar', 98, 2193], ['BFS', 98, 2250], ['Astar', 98, 2205], ['BFS', 98, 2250], ['Astar', 98, 2213], ['BFS', 98, 2250], ['Astar', 98, 2205], ['BFS', 98, 2250], ['Astar', 98, 2206], ['BFS', 98, 2250], ['Astar', 98, 2224], ['BFS', 98, 2250], ['Astar', 98, 2213], ['BFS', 98, 2250], ['Astar', 98, 2222], ['BFS', 98, 2250], ['Astar', 98, 2212], ['BFS', 98, 2249], ['Astar', 98, 2216], ['BFS', 98, 2250], ['Astar', 0, 2247], ['BFS', 0, 2247], ['Astar', 98, 2192], ['BFS', 98, 2248]]
p=.2 :: [['Astar', 98, 1832], ['BFS', 98, 1997], ['Astar', 98, 1829], ['BFS', 98, 1994], ['Astar', 98, 1917], ['BFS', 98, 1998], ['Astar', 98, 1856], ['BFS', 98, 1979], ['Astar', 98, 1867], ['BFS', 98, 1988], ['Astar', 98, 1801], ['BFS', 98, 1994], ['Astar', 98, 1903], ['BFS', 98, 1998], ['Astar', 98, 1878], ['BFS', 98, 1998], ['Astar', 98, 1852], ['BFS', 98, 1997], ['Astar', 98, 1817], ['BFS', 98, 1997], ['Astar', 98, 1849], ['BFS', 98, 1997], ['Astar', 98, 1849], ['BFS', 98, 1997], ['Astar', 98, 1899], ['BFS', 98, 1993], ['Astar', 98, 1864], ['BFS', 98, 1997], ['Astar', 98, 1848], ['BFS', 98, 1993]]
p=.3 :: [['Astar', 98, 1395], ['BFS', 98, 1704], ['Astar', 98, 1427], ['BFS', 98, 1624], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 1712], ['BFS', 0, 1712], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1713], ['BFS', 0, 1713], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 98, 1082], ['BFS', 98, 1731], ['Astar', 104, 1334], ['BFS', 104, 1691], ['Astar', 98, 1367], ['BFS', 98, 1671], ['Astar', 0, 1666], ['BFS', 0, 1666], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 5], ['BFS', 0, 5], ['Astar', 0, 6], ['BFS', 0, 6], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 44], ['BFS', 0, 44], ['Astar', 0, 1711], ['BFS', 0, 1711], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 100, 1440], ['BFS', 100, 1666], ['Astar', 0, 48], ['BFS', 0, 48], ['Astar', 0, 1639], ['BFS', 0, 1639], ['Astar', 98, 1392], ['BFS', 98, 1622], ['Astar', 0, 1592], ['BFS', 0, 1592], ['Astar', 0, 1690], ['BFS', 0, 1690], ['Astar', 0, 1683], ['BFS', 0, 1683], ['Astar', 98, 1113], ['BFS', 98, 1692], ['Astar', 108, 1609], ['BFS', 108, 1693], ['Astar', 98, 1223], ['BFS', 98, 1647], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 100, 1500], ['BFS', 100, 1687]]
p=.4 :: [['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 11], ['BFS', 0, 11], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 5], ['BFS', 0, 5], ['Astar', 0, 328], ['BFS', 0, 328], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 51], ['BFS', 0, 51], ['Astar', 0, 228], ['BFS', 0, 228], ['Astar', 0, 10], ['BFS', 0, 10], ['Astar', 0, 38], ['BFS', 0, 38], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 11], ['BFS', 0, 11], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 19], ['BFS', 0, 19], ['Astar', 0, 12], ['BFS', 0, 12], ['Astar', 0, 50], ['BFS', 0, 50], ['Astar', 0, 982], ['Astar', 0, 982], ['BFS', 0, 982], ['Astar', 0, 982], ['BFS', 0, 982], ['BFS', 0, 982], ['Astar', 0, 24], ['BFS', 0, 24], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 5], ['BFS', 0, 5]]
p=.5 :: [['Astar', 0, 98], ['BFS', 0, 98], ['Astar', 0, 10], ['BFS', 0, 10], ['Astar', 0, 23], ['BFS', 0, 23], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 63], ['BFS', 0, 63], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 47], ['BFS', 0, 47], ['Astar', 0, 18], ['BFS', 0, 18], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 6], ['BFS', 0, 6], ['Astar', 0, 0], ['BFS', 0, 0]]
p=.6 :: [['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 6], ['BFS', 0, 6], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 11], ['BFS', 0, 11], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 6], ['BFS', 0, 6]]
p=.7 :: [['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 5], ['BFS', 0, 5], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 7], ['BFS', 0, 7], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 5], ['BFS', 0, 5], ['Astar', 0, 5], ['BFS', 0, 5], ['Astar', 0, 0], ['BFS', 0, 0]]
p=.8 :: [['Astar', 0, 4], ['BFS', 0, 4], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 3], ['BFS', 0, 3], ['Astar', 0, 0], ['BFS', 0, 0]]
p=.9 :: [['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0]]


'''
data = [['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 1], ['BFS', 0, 1], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 2], ['BFS', 0, 2], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0], ['Astar', 0, 0], ['BFS', 0, 0]]

'''
len = len(data)
prob = 0
for i in data:
    if i[1] != 0:
        prob += 1
print("{0:.0f}%".format(prob/len * 100))
print(len)
'''
bfsExplored = 0
bfsCount = 0

astarExplored = 0
astarCount = 0

for lst in data:
    if lst[0] == "BFS":
        bfsExplored += lst[2]
        bfsCount += 1
    if lst[0] == "Astar":
        astarExplored += lst[2]
        astarCount += 1

print("BFS: "+str(bfsExplored/bfsCount))
print("Astar: "+str(astarExplored/astarCount))

'''
#Problem 3
p_value = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
astar_ave = np.array([2499, 2208,  1857, 1352, 125, 20, 4, 2, 1, 0, 0])
bfs_ave = np.array([2500,  2250, 1995,  1675, 125, 20, 4, 2, 1, 0, 0])


plt.plot(p_value, bfs_ave, color="black")
plt.plot(p_value, astar_ave, color="red")

plt.scatter(p_value, bfs_ave, color="black")
plt.scatter(p_value, astar_ave, color="red")

plt.xlabel("Obstacle Density P")
plt.ylabel("Average Cells Explored")
'''
strat1_q = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
strat1_success_probability = np.array([10/10, 12/20, 8/20, 8/20, 4/20, 2/10, 0/10, 0/10, 0/10, 0/10, 0/10])

strat2_q = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
strat2_success_probability = np.array([10/10, 8/10, 7/10, 5/10, 3/10, 2/10, 0/10, 0/10, 0/10, 0/10, 0/10])

#Question 4 Bar Chart
x_q4 = np.array(["DFS", "BFS", "A*"])
y_q4 = np.array([300, 310, 255])

plt.bar(x_q4,y_q4)

plt.xlabel("Algorithm")
plt.ylabel("Dimension")

plt.show()
#plt.savefig('img/q4img1.png', dpi=1000)