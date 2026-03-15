from itertools import combinations
from typing import Optional

from lab1_vertex_cover.vertex_cover.types import VertexSets, EdgeList
from lab1_vertex_cover.utils.dimacs import isVC


def brute_force(num_vertices: int, edge_list: EdgeList, k: int) -> Optional[set[int]]:
    vertices = range(1, num_vertices)

    for combination in combinations(vertices,k):
        cover_candidate = set(combination)
        if isVC(edge_list, cover_candidate):
            return cover_candidate
    return None