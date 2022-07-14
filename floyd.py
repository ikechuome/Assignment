import unittest
# Number of vertices in the graph
V = 4

INF = 99999


def floydWarshall(graph):
    """ Python Program for Floyd Warshall Algorithm """


graph = [[0, 7, INF, 8], [INF, 0, 5, INF], [INF, INF, 0, 2], [INF, INF, INF, 0]]

dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

for k in range(V):

    # pick all vertices as source one by one
    for i in range(V):

        # Pick all vertices as destination for the
        # above picked source
        for j in range(V):
            # If vertex k is on the shortest path from
            # i to j, then update the value of dist[i][j]
            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j]
                             )
print(dist)

# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V - 1:
                print()


# Driver program to test the above program
# Let us create the following weighted graph
"""
            8
       (0)------->(3)
        |         /|\
      7 |          |
        |          | 2
       \|/         |
       (1)------->(2)
            5           """

# Print the solution
MAX_LENGTH = len(dist)

floydWarshall(dist)

printSolution(dist)





def vertice_number(dist):

    """# Unit testing"""

    if len(dist) > 4:
        raise ValueError('A maximum for 4 element should be in the list')
    return {'floyd_g': dist}


class Testvertice(unittest.TestCase):
    def test_vertice_success(self):
        actual = vertice_number(dist=[[0, 7, 12, 8], [99999, 0, 5, 7],
                                      [99999, 99999, 0, 2], [99999, 99999, 99999, 0]])
        expected = {"floyd_g": [[0, 7, 12, 8], [99999, 0, 5, 7],
                                [99999, 99999, 0, 2], [99999, 99999, 99999, 0]]}
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()


