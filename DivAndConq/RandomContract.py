"""
Undirected graph
"""

import uuid


class Vertex:

    def __init__(self, code: str):
        self.code = code
        self.edges = {}

    def __str__(self):
        return self.code


class Edge:

    def __init__(self, vertex_one: Vertex, vertex_two: Vertex):
        self.code = str(uuid.uuid4())
        self.vertex_one = vertex_one
        self.vertex_two = vertex_two

        self.union_code = Edge.get_union_code(vertex_one.code, vertex_two.code)

    @staticmethod
    def get_union_code(vertex_code_one: str, vertex_code_two: str) -> str:
        """
        Vertex code is a help to identify the two vertices of an edge

        :param vertex_code_one:
        :param vertex_code_two:
        :return:
        """
        if vertex_code_one <= vertex_code_two:
            union_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, vertex_code_one + '-' + vertex_code_two))
        else:
            union_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, vertex_code_two + '-' + vertex_code_one))
        return union_code


class UndirectedGraph:
    """
    Graph representation by Adjacency Lists
        1. An array containing the graph’s vertices.
        2. An array containing the graph’s edges.
        3. For each edge, a pointer to each of its two endpoints.
        4. For each vertex, a pointer to each of the incident edges.
    """

    def __init__(self):
        self.vertices = []
        self.edges = []

    def find_vertex_by_code(self, vertex_code: str):
        for v in reversed(self.vertices):
            if v.code == vertex_code:
                return v

        return None

    def find_edge_by_vertices_code(self, vertex_code_one: str, vertex_code_two: str):
        """
        Search a edge by the vertices

        :param vertex_code_one:
        :param vertex_code_two:
        :return:
        """
        union_code = Edge.get_union_code(vertex_code_one, vertex_code_two)
        for e in self.edges:
            if e.union_code == union_code:
                return e
        return None

    def add_vertices(self, vertex_code_one: str, vertex_code_two: str):
        """
        Find vertices, if not found then create and append to list

        :param vertex_code_one: code of first vertex
        :param vertex_code_two: code of second vertex
        :return:
        """

        # Find or create vertices
        v1 = self.find_vertex_by_code(vertex_code_one)
        if not v1:
            v1 = Vertex(vertex_code_one)
            self.vertices.append(v1)

        v2 = self.find_vertex_by_code(vertex_code_two)
        if not v2:
            v2 = Vertex(vertex_code_two)
            self.vertices.append(v2)

        # Find or create Edge
        edge = self.find_edge_by_vertices_code(v1.code, v2.code)
        if not edge:
            edge = Edge(v1, v2)
            self.edges.append(edge)
            v1.edges[edge.union_code] = edge
            v2.edges[edge.union_code] = edge

    def print_graph(self):
        for v in self.vertices:
            print(f'Vertex {v.code}, connections:')
            for e in v.edges:
                print(f'{v.edges[e].vertex_one.code if v.edges[e].vertex_one.code != v.code else v.edges[e].vertex_two.code},')
            print()


if __name__ == '__main__':

    graph = UndirectedGraph()
    graph.add_vertices('1', '2')
    graph.add_vertices('1', '10')
    graph.add_vertices('1', '5')
    graph.add_vertices('2', '3')

    graph.add_vertices('2', '3')
    graph.add_vertices('2', '3')
    graph.add_vertices('2', '3')
    graph.add_vertices('5', '1')
    graph.add_vertices('5', '1')
    graph.add_vertices('5', '10')
    graph.print_graph()

