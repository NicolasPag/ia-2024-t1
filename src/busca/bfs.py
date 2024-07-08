"""Implementação da busca em profundidade."""

from queue import deque as Queue

#from util import reverse_path


def bfs(graph, start: int, goal: int) -> (int, float, [int]):
    """Busca um caminho entre start e goal usando busca em largura."""
    
    stack = [(start, None)]
    visitedNodes = {}

    countNodes = 0

    while stack:
        currNode, predecessor = stack.pop(0)

        if goal == currNode:
            path = [currNode]
            totalCost = 0

            while predecessor is not None:
                path.append(predecessor)
                totalCost += graph[predecessor][1][currNode]
                currNode = predecessor
                predecessor = visitedNodes.get(currNode)

            path.reverse()

            break

        if currNode not in visitedNodes:

            countNodes += 1
            visitedNodes[currNode] = predecessor

            for neighbor, _ in graph[currNode][1].items():
                if neighbor not in visitedNodes:
                    stack.append((neighbor, currNode))

    return ((countNodes, totalCost, path))