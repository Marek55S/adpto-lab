# recursive solution with O(2^k) time complexity

from typing import Optional
from lab1_vertex_cover.vertex_cover.types import VertexSets, EdgeList

def recursive_v1(num_vertices: int, edge_list: EdgeList, k: int, selected: set[int]) -> Optional[set[int]]:

    new_edge = None

    while edge_list:
        new_edge = edge_list.pop()
        if not (new_edge[0] in selected or new_edge[1] in selected):
            break
    
    if new_edge is None:
        return selected
    
    s1 = recursive_v1(num_vertices, edge_list.copy(), k-1, selected.union({new_edge[0]}))
    s2 = recursive_v1(num_vertices, edge_list.copy(), k-1, selected.union({new_edge[1]}))

    if s1 is not None:
        return s1
    if s2 is not None:
        return s2
