#!/usr/bin/env python
"""Implementation of the Partition data structure"""

from xml.dom import minidom
from collections import namedtuple

Vertex = namedtuple("Vertex", ["id", "x", "y", "key"])
Edge = namedtuple("Edge", ["src", "dst", "weight"])


class Partition:
    """Partition"""
    def __init__(self, size):
        self._forest = [x for x in range(size)]

    @property
    def forest(self):
        """Return the forest"""
        return self._forest

    def add(self, edge: Edge):
        """
        Add an edge to the partition

        Find the root of the source vertex tree
        Find the root of the destination vertex tree
        If they are different, set root of the destination vertex tree to the root of the source vertex tree
        """
        # make two calls to find_root method
        source = self._find_root(edge.src)
        destination = self._find_root(edge.dst)
        if source != destination:
            self._forest[destination] = source

    def _find_root(self, node: int) -> int:
        """
        Find root of a node

        The root of a tree is a node that has its value matching the index in the forest
        """
        "assume that the fn returns the index of the first element in the forest that matches the index in the forest"
        while self._forest[node] != node:
            node = self._forest[node]
        return node

    def __str__(self) -> str:
        """Stringify the forest"""
        return str(self._forest)

    def __iter__(self):
        """Iterate over the forest"""
        return iter(self._forest)


def read_xml(filename: str) -> tuple:
    """Read XML representation of the graph"""
    vertices: dict[int, Vertex] = {}
    edges: list[Edge] = []

    xml_doc = minidom.parse(filename)
    xml_graph = xml_doc.getElementsByTagName("Graph")[0]
    xml_vertices = xml_graph.getElementsByTagName("Vertices")[0].getElementsByTagName(
        "Vertex"
    )
    xml_edges = xml_graph.getElementsByTagName("Edges")[0].getElementsByTagName("Edge")

    for vertex in xml_vertices:
        vertices[int(vertex.getAttribute("id"))] = Vertex(
            int(vertex.getAttribute("id")),
            float(vertex.getAttribute("x")),
            float(vertex.getAttribute("y")),
            vertex.getAttribute("label")
        )

    for edge in xml_edges:
        edges.append(
            Edge(
                int(edge.getAttribute("source")),
                int(edge.getAttribute("destination")),
                float(edge.getAttribute("weight"))
            )
        )
    return vertices, edges


def main():
    """Main function"""
    vertices, edges = read_xml("data/exercises/partition/neia.xml")
    partition = Partition(len(vertices))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    for edge in sorted(edges, key=lambda e: e.weight):
        partition.add(edge)
        print(", ".join([f"{x:2}" for x in partition]))
    print(", ".join([f"{x:2}" for x in range(len(vertices))]))
    print(partition.forest)


if __name__ == "__main__":
    main()
