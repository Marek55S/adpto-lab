# recursive solution with O(1.618^k) time complexity

from typing import Optional
from lab1_vertex_cover.vertex_cover.types import VertexSets, EdgeList

def recursive_v2(num_vertices: int, graph:VertexSets, k: int, selected: set[int]) -> Optional[set[int]]:

    if k<0:
        return None

    if not any(graph):
        return selected

    if k ==0:
        return None

    new_vertex = None

    for i in range(1, num_vertices):
        if graph[i]:
            new_vertex = i
            break

    if new_vertex is None:
        return selected

    graph1 = {graph[i].copy() for i in range(1, num_vertices)}

    for i in range(1, num_vertices):
        if new_vertex in graph1[i]:
            graph1[i].remove(new_vertex)

    s1 = recursive_v2(num_vertices, )