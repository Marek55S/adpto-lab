from .types import EdgeList


def logn_approx(graph: EdgeList) -> set[int]:
    """
    Approximation algorithm for the Vertex Cover problem, which takes the vertex
    with the highest degree and adds it to the solution.

    Approximation factor: log(n)

    :param graph: graph represented as a list of edges
    :return: set of vertices that approximate the cover
    """
    cover = set()
    degrees = {}
    for u,v in graph:
        degrees[u] = degrees.get(u, 0) + 1
        degrees[v] = degrees.get(v, 0) + 1

    while graph:
        max_degree_vertex = max(degrees, key=degrees.get)
        cover.add(max_degree_vertex)

        graph = [edge for edge in graph if max_degree_vertex not in edge]

        degrees.pop(max_degree_vertex)
        for u,v in graph:
            if u == max_degree_vertex or v == max_degree_vertex:
                continue
            if u in degrees:
                degrees[u] -= 1
            if v in degrees:
                degrees[v] -= 1

    return cover