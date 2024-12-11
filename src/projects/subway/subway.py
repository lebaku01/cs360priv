#!/usr/bin/env python3
# encoding: UTF-8
"""Torn to pieces"""

from pythonds3.graphs import Graph

from pathlib import Path


def read_file(filename: str) -> tuple[Graph, str, str]:
    """
    Read graph from file

    Return the graph object and two vertices: start and destination
    """
    file = open(filename, "r")
    lines = file.readlines()
    graph = Graph()
    for line in lines[1:-1]:

        mapping = line.strip("\n").split(" ")

        if mapping[0] not in graph:
            graph.set_vertex(mapping[0])

        vertex = graph.get_vertex(mapping[0])

        for adjacent in mapping[1:]:

            if adjacent not in graph:
                neighbor = graph.set_vertex(adjacent)

            neighbor = graph.get_vertex(adjacent)
            graph.add_edge(vertex.get_key(), adjacent)
            graph.add_edge(adjacent, vertex.get_key())
    src, dst = lines[-1].strip("\n").split(" ")
    for each in graph:
        print(each.get_key())
        for every in list(each.get_neighbors()):
            print("----"+every.get_key())
    return graph, src, dst


def find_routes(g: Graph, src: str, dst: str) -> str:
    """Find the path between two stations"""
    """somewhere in between the previous fn and this one the source looses / never gains any edges????!?!?!?!?!"""
    start = g.get_vertex(src)
    g.bfs(start)
    path = []
    vertex = g.get_vertex(dst)
    start.set_previous(None)
    while vertex is not None:
        path.insert(0, vertex.get_key())
        vertex = vertex.previous
    return " ".join(path)

def main():
    """This is the main function"""
    data_dir = "data/projects/subway/"
    for file in sorted(Path(data_dir).glob("*.in")):
        read_file(file.name)
        print()



if __name__ == "__main__":
    main()
