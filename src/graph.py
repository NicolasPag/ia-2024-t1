"""Implementação de uma estrutura de grafo."""

import sys


def read_graph(filename: str):
    """Le uma estrutura de grafo de um arquivo e retorna a estrutura."""
    graph = []
    with open(filename, "rt", encoding="utf-8") as inputFile:
        vertexCount = int(inputFile.readline().strip())
        for _ in range(vertexCount):
            index, latitude, longitude = inputFile.readline().strip().split()

            index, latitude, longitude = [
                int(index),
                float(latitude),
                float(longitude)
            ]

            graph.append([(latitude, longitude), {}])
            
        edgeCount = int(inputFile.readline().strip())

        for _ in range(edgeCount):
            fromVertex, toVertex, cost = (
                inputFile.readline().strip().split()
            )

            fromVertex, toVertex, cost = [
                int(fromVertex),
                int(toVertex),
                float(cost)
            ]
            
            graph[fromVertex][1][toVertex] = cost
    
    return graph
