# code I copied from the hopcroftKrap pip module
from copy import deepcopy


class HopcroftKarp(object):
    def __init__(self, graph):
        """
        :param graph: an unweighted bipartite graph represented as a dictionary.
        Vertices in the left and right vertex set must have different labelling
        :return: a maximum matching of the given graph represented as a dictionary.
        """
        self._matching = {}
        self._dfs_paths = []
        self._dfs_parent = {}

        self._graph = deepcopy(graph)
        self._left = set(self._graph.keys())
        self._right = set()

        for value in self._graph.values():
            self._right.update(value)
        for vertex in self._left:
            for neighbour in self._graph[vertex]:
                if neighbour not in self._graph:
                    self._graph[neighbour] = set()
                    self._graph[neighbour].add(vertex)
                else:
                    self._graph[neighbour].add(vertex)

    def __bfs(self):
        layers = []
        layer = set()
        for vertex in self._left:  # for each free vertex in the left vertex set
            if vertex not in self._matching:  # confirms that the vertex is free
                layer.add(vertex)
        layers.append(layer)
        visited = set()  # to keep track of the visited vertices
        while True:
            # we take the most recent layer in the partitioning on every repeat
            layer = layers[-1]
            new_layer = set()  # new list for subsequent layers
            for vertex in layer:
                if vertex in self._left:  # if true, we traverse unmatched edges to vertices in right
                    visited.add(vertex)
                    for neighbour in self._graph[vertex]:
                        # check if the neighbour is not already visited
                        # check if vertex is matched or the edge between neighbour and vertex is not matched
                        if neighbour not in visited and (vertex not in self._matching or neighbour != self._matching[vertex]):
                            new_layer.add(neighbour)
                else:  # we traverse matched edges to vertices in left
                    # we don't want to traverse the vertex again
                    visited.add(vertex)
                    for neighbour in self._graph[vertex]:
                        # check if the neighbour is not already visited
                        # check if vertex is in the matching and if the edge between vertex and neighbour is matched
                        if neighbour not in visited and (vertex in self._matching and neighbour == self._matching[vertex]):
                            new_layer.add(neighbour)
            # we add the new layer to the set of layers
            layers.append(new_layer)
            # if new_layer is empty, we have to break the BFS while loop....
            if len(new_layer) == 0:
                return layers   # break
            # else, we terminate search at the first layer k where one or more free vertices in V are reached
            if any(vertex in self._right and vertex not in self._matching for vertex in new_layer):
                return layers  # break
                # break

    # --------------------------------------------------------------------------------------------------------------
    # if we are able to collate these free vertices, we run DFS recursively on each of them
    # this algorithm finds a maximal set of vertex disjoint augmenting paths of length k (shortest path),
    # stores them in P and increments M...
    # --------------------------------------------------------------------------------------------------------------
    def __dfs(self, v, index, layers):
        """
        we recursively run dfs on each vertices in free_vertex,

        :param v: vertices in free_vertex
        :return: True if P is not empty (i.e., the maximal set of vertex-disjoint alternating path of length k)
        and false otherwise.
        """
        if index == 0:
            path = [v]
            while self._dfs_parent[v] != v:
                path.append(self._dfs_parent[v])
                v = self._dfs_parent[v]
            self._dfs_paths.append(path)
            return True
        for neighbour in self._graph[v]:  # check the neighbours of vertex
            if neighbour in layers[index - 1]:
                # if neighbour is in left, we are traversing unmatched edges..
                if neighbour in self._dfs_parent:
                    continue
                if (neighbour in self._left and (v not in self._matching or neighbour != self._matching[v])) or \
                        (neighbour in self._right and (v in self._matching and neighbour == self._matching[v])):
                    self._dfs_parent[neighbour] = v
                    if self.__dfs(neighbour, index-1, layers):
                        return True
        return False

    def maximum_matching(self, keys_only=False):
        while True:
            layers = self.__bfs()
            # we break out of the whole while loop if the most recent layer added to layers is empty
            # since if there are no vertices in the recent layer, then there is no way augmenting paths can be found
            if len(layers[-1]) == 0:
                break
            free_vertex = set([vertex for vertex in layers[-1]
                               if vertex not in self._matching])

            # the maximal set of vertex-disjoint augmenting path and parent dictionary
            # has to be cleared each time the while loop runs
            # self._dfs_paths.clear() - .clear() and .copy() attribute works for python 3.3 and above
            del self._dfs_paths[:]
            self._dfs_parent.clear()

            # O(m) - every vertex considered once, each edge considered once
            for vertex in free_vertex:
                # this creates a loop of the vertex to itself in the parent dictionary,
                self._dfs_parent[vertex] = vertex
                self.__dfs(vertex, len(layers)-1, layers)

            # if the set of paths is empty, nothing to add to the matching...break
            if len(self._dfs_paths) == 0:
                break

            # if not, we swap the matched and unmatched edges in the paths formed and add them to the existing matching.
            # the paths are augmenting implies the first and start vertices are free. Edges 1, 3, 5, .. are thus matched
            for path in self._dfs_paths:
                for i in range(len(path)):
                    if i % 2 == 0:
                        self._matching[path[i]] = path[i+1]
                        self._matching[path[i+1]] = path[i]
        if keys_only:
            self._matching = {k: v for k,
                              v in self._matching.items() if k in self._left}
        return self._matching


# my code here
# basic DFS that fills a region starting from cordinate r, c, with parity p, and
# makes the region have value v
def floodfill(r, c, p, v):
    global region, n, m
    ret = False
    if 0 <= r <= n-1 and 0 <= c <= m-1 and region[r][c] == -1 and table[r][c] == p:
        ret = True
        region[r][c] = v
        floodfill(r-1, c, p, v)
        floodfill(r+1, c, p, v)
        floodfill(r, c-1, p, v)
        floodfill(r, c+1, p, v)
    return ret

# returns true if two regions are linkable


def linkable(r, c, r1, c1):
    return region[r1][c1] >= 0 and table[r][c] != table[r1][c1]

# links two regions with a double edge


def link(r1, r2):
    global graph
    graph[r1].add(r2)
    graph[r2].add(r1)


# get input store parity values in table and
# make region -1 for regions that have not been mapped
n, m = map(int, input().split())
table = []
region = []
for _ in range(n):
    table.append(input())
    region.append([-1 for _ in range(m)])

# flood fill border regions
#top and bottom
count = 0
for c in range(m):
    if floodfill(0, c, table[0][c], -2):
        count += 1
    if floodfill(n-1, c, table[n-1][c], -2):
        count += 1

#right and left
for r in range(n):
    if floodfill(r, 0, table[r][0], -2):
        count += 1
    if floodfill(r, m-1, table[r][m-1], -2):
        count += 1

# make the regions for the interior
nodeNum = 0
for r in range(1, n-1):
    for c in range(1, m-1):
        if floodfill(r, c, table[r][c], nodeNum):
            nodeNum += 1

# setup the interior graph
graph = {}
for r in range(0, nodeNum):
    graph[r] = set()

# link regions together if they can be linked
for r in range(1, n-1):
    for c in range(1, m-1):
        if region[r][c] >= 0:
            if linkable(r, c, r-1, c):
                link(region[r-1][c], region[r][c])
            if linkable(r, c, r, c-1):
                link(region[r][c-1], region[r][c])

# run HopcroftKarp, divide by 2 because it returns a dict with edges
# that are doubled becaus this is a undirected graph
print(count + len(HopcroftKarp(graph).maximum_matching())//2)
